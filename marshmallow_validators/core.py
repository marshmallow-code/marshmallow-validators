# -*- coding: utf-8 -*-
# Use webargs' ValidationError if available. It is compatible with
# marshmallow's ValidationError.
try:
    from webargs import ValidationError
except ImportError:
    from marshmallow import ValidationError

__all__ = [
    'BaseConverter',
    'ValidationError',
]

class BaseConverter(object):
    """Base converter validator that converts a third-party validators into
    marshmallow validators. Concrete classes must implement `make_validator`.

    :param list validators: List of 3rd-party validator objects to convert.
    """

    def __init__(self, validators):
        self.validators = validators

    def make_validator(self, validator):
        """Receives a 3rd-party validator and converts it to a marshmallow validator
        function/callable.

        :param validator: A 3rd-party validator object
        :return: A callable marshmallow validator
        """
        raise NotImplementedError('Converter must implement make_validator')

    def __call__(self, val):
        errors = []
        for vendor_validator in self.validators:
            validator = self.make_validator(vendor_validator)
            try:
                validator(val)
            except ValidationError as err:
                errors.extend(err.messages)
        if errors:
            raise ValidationError(errors)
