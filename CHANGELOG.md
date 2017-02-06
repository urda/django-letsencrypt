# django-letsencrypt CHANGELOG

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
