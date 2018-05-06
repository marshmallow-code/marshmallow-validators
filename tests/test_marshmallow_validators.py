# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import pytest
from colander import ContainsOnly
from marshmallow import Schema, fields
from marshmallow.exceptions import \
    ValidationError as MarshmallowValidationError
from wtforms.validators import AnyOf, Length, NoneOf

from marshmallow_validators.colander import from_colander
from marshmallow_validators.wtforms import from_wtforms, make_converter

# WTForms

class TestWTFormsValidation:

    def test_from_wtforms(self):
        field = fields.Field(
            validate=from_wtforms([AnyOf(['red', 'blue'])])
        )

        assert field.deserialize('red') == 'red'
        with pytest.raises(MarshmallowValidationError) as excinfo:
            field.deserialize('green')
        assert 'Invalid value' in str(excinfo)

    def test_from_wtforms_multi(self):
        field = fields.Field(
            validate=from_wtforms(
                [
                    Length(min=4),
                    NoneOf(['nil', 'null', 'NULL'])
                ]
            )
        )
        assert field.deserialize('thisisfine') == 'thisisfine'
        with pytest.raises(MarshmallowValidationError) as excinfo:
            field.deserialize('bad')
        assert 'Field must be at least 4 characters long' in str(excinfo)
        with pytest.raises(MarshmallowValidationError) as excinfo:
            field.deserialize('null')
        assert "Invalid value, can't be any of: nil, null, NULL." in str(excinfo)

        with pytest.raises(MarshmallowValidationError) as excinfo:
            field.deserialize('nil')
        # both errors are returned
        assert "Invalid value, can't be any of: nil, null, NULL." in str(excinfo)
        assert 'Field must be at least 4 characters long' in str(excinfo)

    def test_from_wtforms_with_translation(self):
        field = fields.Field(
            validate=from_wtforms(
                [
                    Length(max=1)
                ],
                locales=['de_DE', 'de']
            )
        )
        with pytest.raises(MarshmallowValidationError) as excinfo:
            field.deserialize('toolong')
        # lol
        validation_msg = excinfo.value.args[0]
        assert 'Feld kann nicht l\xe4nger als 1 Zeichen sein.' in validation_msg

    def test_make_converter(self):
        f = make_converter(['de_DE', 'de'])
        field = fields.Field(
            validate=f(
                [
                    Length(max=1)
                ],
                locales=['de_DE', 'de']
            )
        )
        with pytest.raises(MarshmallowValidationError) as excinfo:
            field.deserialize('toolong')
        validation_msg = excinfo.value.args[0]
        assert 'Feld kann nicht l\xe4nger als 1 Zeichen sein.' in validation_msg

    def test_error_stored_on_field(self):
        class MySchema(Schema):
            foo = fields.Field(
                validate=from_wtforms(
                    [Length(max=1)]
                )
            )

        errors = MySchema().validate({'foo': 'invalid'})
        assert 'foo' in errors

# Colander


class TestColanderValidation:
    def test_from_colander(self):
        field = fields.Field(
            validate=from_colander([ContainsOnly([1])])
        )
        assert field.deserialize([1]) == [1]
        with pytest.raises(MarshmallowValidationError) as excinfo:
            field.deserialize([2])
        assert 'One or more of the choices you made was not acceptable' in str(excinfo)
