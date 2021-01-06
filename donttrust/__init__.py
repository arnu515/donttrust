from typing import Dict

from .exceptions import DontTrustBaseException
from .schema import Schema


class ValidationError(Exception):
    """
    Error raised when validation of a DontTrust object has failed.
    """

    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message


class DontTrust:
    _items: Dict[str, Schema] = dict()

    def __init__(self, **items: Schema):
        """
        Creates a DontTrust Object. Each item in the object should be a valid ``donttrust.schema.Schema``.

        Fieldname is inferred automatically.

        Example usage::

            trust = DontTrust(test=Schema().string())
            # Here, the test Schema will automatically have the field set to "test".

        :param items: A kwargs object with each item being a ``donttrust.schema.Schema`` object.
        """

        for key in items.keys():
            self._items[key] = items[key]
            self._items[key].field = key

    def validate(self, **kwargs):
        """
        Validates all schema in this object and throws a ``donttrust.ValidationError`` if validation fails.
        To not raise an error and return ``False`` if validation fails, use ``validate_without_exception``.

        :param kwargs: The items to validate. It should be a kwargs object with the same fields as the schema.
        :returns: Returns a dictionary with the validated items.
        :raises: Raises ``donttrust.ValidationError` if validation fails
        """
        final = dict()
        try:
            for key in self._items.keys():
                final[key] = self._items[key].validate(kwargs.get(key))
            return final
        except DontTrustBaseException as e:
            raise ValidationError(e.field, e.message)

    def validate_and_return_json_object(self, **kwargs) -> dict:
        """
        Same as ``validate``, but returns a dictionary instead of throwing errors.

        :param kwargs: The items to validate. It should be a kwargs object with the same fields as the schema.
        :returns: A dictionary with a "data" field containing validated data if validation succeeds, or a dictionary
        with "error" and "field" fields if validation fails.
        """
        try:
            final = self.validate(**kwargs)
            return {"data": final}
        except ValidationError as e:
            return {"error": e.message, "field": e.field}

    def validate_without_exception(self, **kwargs):
        """
        Same as ``validate``, but returns ``False`` if validation fails
        :param kwargs: The items to validate. It should be a kwargs object with the same fields as the schema.
        :return: Returns a dictionary with validated data if validation succeeds, else returns False
        """
        try:
            return self.validate(**kwargs)
        except ValidationError:
            return False
