**********************
marshmallow-validators
**********************

.. image:: https://img.shields.io/pypi/v/marshmallow-validators.svg
    :target: https://pypi.python.org/pypi/marshmallow
    :alt: Latest version

.. image:: https://img.shields.io/travis/marshmallow-code/marshmallow-validators/pypi.svg
    :target: https://travis-ci.org/marshmallow-code/marshmallow
    :alt: Travis-CI

Homepage: http://marshmallow-validators.rtfd.org/

Use 3rd-party validators (e.g. from WTForms and colander) with marshmallow.

.. code-block:: python

    from marshmallow import Schema, fields
    from marshmallow_validators.wtforms import from_wtforms
    from wtforms.validators import Email, Length

    # Leverage WTForms il8n
    locales = ['de_DE', 'de']

    class UserSchema(Schema):
        email = fields.Str(
            validate=from_wtforms([Email()], locales=locales)
        )
        password = fields.Str(
            validate=from_wtforms([Length(min=8, max=300)], locales=locales)
        )

    UserSchema().validate({'email': 'invalid', 'password': 'abc'})
    # {'email': ['Ungültige Email-Adresse.'],
    # 'password': ['Feld muss zwischen 8 und 300 Zeichen beinhalten.']}

Get It Now
==========

::

    $ pip install -U marshmallow-validators


Documentation
=============

Full documentation is available at http://marshmallow-validators.rtfd.org/ .

Project Links
=============

- Docs: http://marshmallow-validators.rtfd.org/
- Changelog: http://marshmallow-validators.readthedocs.org/en/latest/changelog.html
- PyPI: https://pypi.python.org/pypi/marshmallow-validators
- Issues: https://github.com/marshmallow-code/marshmallow-validators/issues

License
=======

MIT licensed. See the bundled `LICENSE <https://github.com/marshmallow-code/marshmallow-validators/blob/pypi/LICENSE>`_ file for more details.
