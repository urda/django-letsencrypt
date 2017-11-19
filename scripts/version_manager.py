#!/usr/bin/env python

"""
Copyright 2017 Peter Urda

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import datetime
import sys
from argparse import ArgumentParser
from collections import (
    Counter,
    OrderedDict,
)
from os.path import (
    dirname,
    join,
)


class FileVersionInfo(object):
    def __init__(
            self,
            key_name: str,
            file_path: str,
            magic_line: str,
            strip_end_chars: int = 0,
    ):
        """
        A simple python object that is used to extract and
        (eventually) update version values across the project

        The 'magic_line' is the first part of a file line that
        is before the version number. So for example, if the version
        is stored on a line such as '__version__=1' your magic line
        will be '__version__='. If you need to remove any extra characters
        at the end of the version line, increase the 'strip_end_chars'
        property on this object.

        :param key_name: The key name, or reference name, for this file
        :param file_path: The path to the file
        :param magic_line: The "magic line" to search for
        :param strip_end_chars: The number of characters to strip off the end
        """

        self.key_name = key_name
        self.file_path = file_path
        self.magic_line = magic_line
        self.strip_end_chars = strip_end_chars

    def get_version(self) -> str:
        """
        Open the file referenced in this object, and scrape the version.

        :return:
            The version as a string, an empty string if there is no match
            to the magic_line, or any file exception messages encountered.
        """

        try:
            f = open(self.file_path, 'r')
            lines = f.readlines()
            f.close()
        except Exception as e:
            return str(e)

        result = ''

        for line in lines:
            if self.magic_line in line:
                start = len(self.magic_line)
                end = len(line) - self.strip_end_chars
                result = line[start:end]
                break

        return result

    def set_version(self, new_version: str):
        """
        Set the version for this given file.

        :param new_version: The new version string to set.
        """

        try:
            f = open(self.file_path, 'r')
            lines = f.readlines()
            f.close()
        except Exception as e:
            print(str(e))
            return

        for idx, line in enumerate(lines):
            if self.magic_line in line:
                start = len(self.magic_line)
                end = len(line) - self.strip_end_chars

                start_str = line[0:start]
                end_str = line[end:]
                lines[idx] = start_str + new_version + end_str

        try:
            f = open(self.file_path, 'w')
            f.writelines(lines)
            f.close()
        except Exception as e:
            print(str(e))
            return


class FileVersionResult(object):
    def __init__(
            self,
            uniform: bool,
            version_details: dict,
            version_result: str
    ):
        """
        Object to contain results about the project's version

        :param uniform: True if versions are the same, False otherwise
        :param version_details: Full details on each file and reported version
        :param version_result: The project's version as a single string.
        """

        self.uniform = uniform
        self.version_details = version_details
        self.version_result = version_result


curr_location = dirname(__file__)
version_objects = [
    FileVersionInfo(
        key_name='package',
        file_path=join(curr_location, '../letsencrypt/__init__.py'),
        magic_line="__version__ = '",
        strip_end_chars=2,
    ),
    FileVersionInfo(
        key_name='setup.py',
        file_path=join(curr_location, '../setup.py'),
        magic_line="    version='",
        strip_end_chars=3,
    ),
]


def get_versions() -> FileVersionResult:
    """
    Search specific project files and extract versions to check.

    :return: A FileVersionResult object for reporting.
    """

    version_counter = Counter()
    versions_match = False
    version_str = None
    versions_discovered = OrderedDict()

    for version_obj in version_objects:
        discovered = version_obj.get_version()
        versions_discovered[version_obj.key_name] = discovered
        version_counter.update([discovered])

    if len(version_counter) == 1:
        versions_match = True
        version_str = list(version_counter.keys())[0]

    return FileVersionResult(
        uniform=versions_match,
        version_details=versions_discovered,
        version_result=version_str,
    )


def set_versions(new_version: str):
    """
    Update all known version objects with a new version string.

    :param new_version: The new version string to set in the project.
    """

    for version_obj in version_objects:
        version_obj.set_version(new_version)


def get_version_without_beta(version_info: FileVersionResult) -> str:
    """
    Get the project's version string *without* any test or beta build labels.

    :param version_info: The current version_info of the project.
    :return: The current version string, without any beta build string values.
    """

    if not version_info:
        raise TypeError("version_info cannot be 'None'!")

    if not version_info.uniform:
        raise ValueError("version_info is not uniform!")

    beta_flag = ".123."
    current_version = version_info.version_result

    # We can just split and take the first value since:
    #
    #  - If the flag *is not there*, we get the entire string back.
    #
    #    OR
    #
    #  - If the flag *is there*, we want everything before it,
    #    AKA the first value.
    #
    return current_version.split(beta_flag)[0]


def get_version_with_beta(version_info: FileVersionResult) -> str:
    """
    Get the project's version string *with* a beta build label based on UTC.

    :param version_info: The current version_info of the project.
    :return: The project's version string, with a beta build number.
    """

    if not version_info:
        raise TypeError("version_info cannot be 'None'!")

    if not version_info.uniform:
        raise ValueError("version_info is not uniform!")

    # Capture datetime as UTC for build timestamp
    utc_datetime = datetime.datetime.utcnow()

    # Setup version string information
    beta_flag = ".123."
    build_number = utc_datetime.strftime("%Y%m%d.%H%M%S")
    cleaned_version = get_version_without_beta(version_info)

    # Return the new version string for the build.
    return "{base}{flag}{build}".format(
        base=cleaned_version,
        flag=beta_flag,
        build=build_number,
    )


if __name__ == '__main__':
    parser = ArgumentParser()

    understood_commands = [
        'check',
        'get-version-only',
        'set-beta-build',
        'unset-beta-build',
        'update',
    ]

    warning_banner = "/!\\/!\\/!\\/!\\/!\\/!\\/!\\/!\\/!\\/!\\/!\\/!\\/!\\/!\\"
    warning_version_mismatch = "Versions DO NOT MATCH across the project!"

    sp = parser.add_subparsers(dest="command")
    for command in understood_commands:
        sp.add_parser(command)

    args = parser.parse_args()

    if args.command == "check" or args.command is None:
        version_data = get_versions()

        for key, version_val in version_data.version_details.items():
            print("{0:.<20} {1}".format(key + " ", version_val))

        print("")

        if version_data.uniform:
            print("Versions look OK across the project")
            print("Version is '{}'".format(version_data.version_result))
        else:
            print(warning_banner)
            print(warning_version_mismatch)
            print(warning_banner)
            sys.exit(1)

    elif args.command == "get-version-only":
        version_data = get_versions()

        if not version_data.uniform:
            sys.exit(1)

        print(version_data.version_result)

    elif args.command == "set-beta-build":
        version_data = get_versions()

        # Halt operations if versions do not match across project
        if not version_data.uniform:
            print(warning_banner)
            print("Unable to set beta build on project version!")
            print(warning_version_mismatch)
            print(warning_banner)
            sys.exit(1)

        build_version = get_version_with_beta(version_data)
        print("Setting beta build version as: '{}'".format(build_version))
        set_versions(build_version)

    elif args.command == "unset-beta-build":
        version_data = get_versions()

        # Halt operations if versions do not match across project
        if not version_data.uniform:
            print(warning_banner)
            print("Unable to unset beta build on project version!")
            print(warning_version_mismatch)
            print(warning_banner)
            sys.exit(1)

        clean_version = get_version_without_beta(version_data)
        print("Resetting version as: '{}'".format(clean_version))
        set_versions(clean_version)

    elif args.command == "update":
        new_version_str = input('New version string > ')
        set_versions(new_version_str)

    sys.exit(0)
