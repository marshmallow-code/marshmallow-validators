**********************
marshmallow-validators
**********************

Release v\ |version| (:ref:`Changelog <changelog>`)

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

Get it now
==========
::

   pip install -U marshmallow-validators


WTForms support
===============

.. automodule:: marshmallow_validators.wtforms
    :members:

colander support
================

.. automodule:: marshmallow_validators.colander
    :members:


Base converter class
====================

.. autoclass:: marshmallow_validators.core.BaseConverter
    :members:


ValidationError with optional webargs support
=============================================

.. autoexception:: marshmallow_validators.ValidationError

Project Info
============

.. toctree::
   :maxdepth: 1

   changelog
   license
