Changelog
---------

(unreleased)

- Drop support for Python 3.3. Version 2.7 and >=3.4 are supported.

2.0.0 (2015-12-28)
++++++++++++++++++

- Fix compatibility with webargs>=0.16.0.
- Remove redundant implementation of ``ValidationError``. ``marshmallow-validators`` will import the ``ValidationError`` from ``webargs`` if it is available, falling back on ``marshmallow.ValidationError``.

1.0.0 (2015-08-30)
++++++++++++++++++

- First release.
- Supports conversion of WTForms and colander validators.
- ``ValidationError`` that inherits from both webargs' ``ValidationError`` (if webargs is installed) and marshmallow's  ``ValidationError``.
