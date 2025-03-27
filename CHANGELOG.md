# django-letsencrypt CHANGELOG

## v5.1.0

There are no major project changes or code updates. This release aligns with
recent Django releases and Python releases.

- Internal Updates:
  - Brought `tox` up-to-date with the current supported Django+Python versions.
  - Brought GitHub actions up-to-date with the current supported Django+Python versions.
  - This project will no longer use the "sign" feature of PyPi.
    - See also: https://blog.pypi.org/posts/2023-05-23-removing-pgp/
- Dependency Updates:
  - `pytz` version `2025.2` or greater now required.
- General Updates:
  - Updated `README` with supported version information.

## v4.1.0

There are no major project changes or code updates. This release aligns with
recent Django releases and Python releases.

- Internal Updates:
  - `urls.url` replaced with `urls.re_path`.
    - See commit `d8e823ed5d4dac9a8be885b1f616d7425681d7f7`.
  - Address `models.W042` warning for `letsencrypt.AcmeChallenge`.
    - See commit `5d644e7e0ec3b5db9e9a28d3b662cc9bab15b188`.
- Dependency Updates:
  - `pytz` version `2021.3` or greater now required.
- Project Updates
  - Testing and other related automations have moved to GitHub Actions.
  - Updated `.python-version` file for latest releases.
- No longer supported:
  - Python `3.6`.
  - Travis CI has been dropped from the project.
- General Updates:
  - General `README` updates.
  - Updated copyright headers.
  - We still try and follow the supported versions as detailed:
    - [Django supported versions](https://www.djangoproject.com/download/#supported-versions)
    - [Django supported Python versions](https://docs.djangoproject.com/en/4.0/faq/install/#what-python-version-can-i-use-with-django)

## v4.0.0

- Breaking Changes
  - This was made as an overall major version bump due to the drastic supported
    version changes. However, the project and code mostly remain the same. This
    version sync allows the project to be easily kept up to date and upgraded.
  - As per the [Django Project Docs](https://www.djangoproject.com/download/).
    This project does a major version upgrade to only support:
    - Release Series `3.1` starting with version `3.1.2`.
    - Release Series `3.0` starting with version `3.0.10`.
    - Release Series `2.2 LTS` starting with version `2.2.16`.
  - This project supports the following python versions:
    - Python `3.6`
    - Python `3.7`
    - Python `3.8`
  - `pytz>=2020.1` is now required.
  - Travis Updates:
    - For the time being, we will continue to use `travis`.
    - Updated to support target versions as detailed for both Django and Python.
  - Operational Excellence Changes:
    - Updated `.python-version` file to latest values.
    - Dropping `slack` notification (for now).
    - Updated the `example_project` `requirements.txt` versions.
  - General Updates:
    - General `README` updates.
    - Updated copyright headers.

## v3.0.1

- Breaking Changes
  - `Django 1.8` support has been dropped. `v3.0.0` is the last supported
    version for users still on `Django 1.8`.
- Documentation Changes
  - Update the `ACME challenge` link in `README.rst`.
- Project Changes
  - Disable `universal` wheel creation in `setup.cfg`.
  - Add a `python_requires` entry into `setup.py`.
    - You can learn more about this feature by reading
    [this](https://packaging.python.org/tutorials/distributing-packages/#python-requires)
    document.
  - Bumped to the latest `pytz`, version `2018.4`.
  - Switched from `reStructuredText` to `Markdown`.
- Internal Changes
  - Bumped `DJANGO_VERSION` targets in `.travis.yml`.
- Thanks to Contributors:
  - [michael-k](https://github.com/michael-k)
  - [Paolo Dina](https://github.com/paolodina)

## v3.0.0

- New Features
  - `django-letsencrypt` now supports `Django 2.0`!
- Breaking Changes
  - `python2` support has been dropped. `v2.0.1` is the last supported `python2`
    version for this package.
  - `Django 1.10` support has been dropped. `v2.0.1` is the last supported
    version for users still on `Django 1.10`.
- Project Changes
  - Make Travis CI install the proper `django` version first, before installing
    the rest of `requirements.txt` during building. Thanks to
    [michael-k](https://github.com/michael-k) for providing a pull request.
      - [GH-54](https://github.com/urda/django-letsencrypt/pull/54)
      - [GH-55](https://github.com/urda/django-letsencrypt/pull/55)
  - `django` tested version bump.
    - `1.11.7` to `1.11.8`.
  - Added `tox` to the project to test multiple versions of `python` and
    `django` together.

## v2.0.1

- Internal Changes
  - Bumped `DJANGO_VERSION` targets in `.travis.yml`.
  - Bumped to the latest `pytz`, version `2017.3`.
  - Updated `requirements.txt` to separate requirement needs.
  - Updated `classifiers` in `setup.py`.
  - Organized and updated `Makefile` for easier reference and use.
  - Configured `Makefile` to support uploading to `Test PyPi`.

## v2.0.0

- Breaking Changes
  - Django `1.9` support has been dropped. There will be no further updates
    to fix any issues that may arise from using `django-letsencrypt` with
    `1.9`.
- Internal Changes
  - `django-letsencrypt` now supports Django `1.11`.
  - Updated builds to use the latest `1.8`, `1.10` releases.
  - Bumped to the latest `pytz`, version `2017.2`.
  - Updated `setup.py` marking any Django `1.9` releases as incompatible.
  - Removed Python `nightly` from Travis builds and testing.
  - Removed `squashed` migrations from the project. **PLEASE NOTE:** If you
    are on an older `v1.x` release of this project, please make sure to
    **UPGRADE** to `v1.1.1` and **migrate** your database. Failure to do so
    will cause a lot of problems, since this release **only** has the single
    migration file.

## v1.1.1

- Internal Changes
  - Removed the need to render `ACME` responses through a template. Instead
    responses are now passed through a `HttpResponse` with a `content_type` of
    `text/plain`. Thanks to [Peter Curet](https://github.com/petercuret)
    for providing a pull request.
    - [GH-29](https://github.com/urda/django-letsencrypt/pull/29)
    - [GH-30](https://github.com/urda/django-letsencrypt/pull/30)
- Corrected `Copyright` dates across the project
- Thanks to Contributors:
  - [Peter Curet](https://github.com/petercuret)

## v1.1.0

- Project Changes
  - Admin `ordering` for the Django admin page is now down by `challenge`
  - Removed `created_ts` and `updated_ts` from model
  - Switched `challenge` and `response` from `TextField` to `CharField`
- Internal Changes
  - Added testing for `detail` view for `ACME` objects
  - Removed `migrations.py` thanks to existing `example_project`'s manage.py

## v1.0.8

- Project Changes
  - Require `pytz` for SQLite users.
  - Update `travis` branch build targets.

## v1.0.7

- Project Changes
  - Final "feature" release of the 1.x branch. 2.0 will support `mysql`.
    This had to be done due to certain model upcoming model changes, and
    will result in a new set of migrations.

## v1.0.6

- Internal Changes
  - Started using `twine`
  - Started uploading `bdist_wheel`

## v1.0.5

- Internal Changes
  - Start using `--sign`, such as: `python setup.py sdist upload --sign -r pypi`

## v1.0.4

- Bump YEAR in LICENSE
- Rework some of the wording in the `README.rst`
- Added `English` as a `Natural Language` `classifier`
- Internal Changes
  - Added a simple version manager script
  - Added version check to `make test`
  - Bump `travis` tests for `1.10.4` to `1.10.5`

## v1.0.3

- Python 3.6 support

## v1.0.2

- The `challenge` field has been made `unique` on `AcmeChallenge`
  objects
- Migrations added to this release
  - A data migration will remove duplicate challenges in this release.
    As with any Django migration, be sure to backup your database first.
- Fixed issues:
  - [GH-2](https://github.com/urda/django-letsencrypt/issues/2)
  - [GH-4](https://github.com/urda/django-letsencrypt/issues/4)

## v1.0.1

- Migrations added to this release
  - **This means v1.0.0 WILL NOT WORK. Use this version instead!**

## v1.0.0

- Production ready model, admin interface, and app usage is released.

## v0.9.3 (Beta Release)

- Made some minor fixes to the `README` file to work on Pypi

## v0.9.2 (Beta Release)

- Made some minor fixes to the `README` file to work on Pypi

## v0.9.1 (Beta Release)

- Made some minor fixes to the `README` file to work on Pypi

## v0.9.0 (Beta Release)

- Initial Release! 🎉
- Django packaged app
- `pypi` upload
