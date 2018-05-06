**********************
marshmallow-validators
**********************

.. image:: https://badge.fury.io/py/marshmallow-validators.svg
    :target: http://badge.fury.io/py/marshmallow-validators
    :alt: Latest version

.. image:: https://img.shields.io/travis/marshmallow-code/marshmallow-validators/pypi.svg
    :target: https://travis-ci.org/marshmallow-code/marshmallow-validators
    :alt: Travis-CI

.. image:: https://img.shields.io/badge/marshmallow-3-blue.svg
    :target: https://marshmallow.readthedocs.io/en/latest/upgrading.html
    :alt: marshmallow 3 compatible

Homepage: https://marshmallow-validators.readthedocs.io/

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

Full documentation is available at https://marshmallow-validators.readthedocs.io/ .

Project Links
=============

- Docs: https://marshmallow-validators.readthedocs.io/
- Changelog: https://marshmallow-validators.readthedocs.io/en/latest/changelog.html
- PyPI: https://pypi.python.org/pypi/marshmallow-validators
- Issues: https://github.com/marshmallow-code/marshmallow-validators/issues

License
=======

MIT licensed. See the bundled `LICENSE <https://github.com/marshmallow-code/marshmallow-validators/blob/pypi/LICENSE>`_ file for more details.
