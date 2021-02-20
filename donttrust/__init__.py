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
    _items: Dict[str, Schema]

    def __init__(self, **items: Schema):
        """
        Creates a DontTrust Object. Each item in the object should be a valid ``donttrust.schema.Schema``.

        Fieldname is inferred automatically.

        Example usage::

            trust = DontTrust(test=Schema().string())
            # Here, the test Schema will automatically have the field set to "test".

        :param items: A kwargs object with each item being a ``donttrust.schema.Schema`` object.
        """
        self._items = dict()

        for key in items.keys():
            self._items[key] = items[key]
            self._items[key].field = key

    def validate(self, dict_=None, **items):
        """
        Validates all schema in this object and throws a ``donttrust.ValidationError`` if validation fails.
        To not raise an error and return ``False`` if validation fails, use ``validate_without_exception``.

        :param dict_: The dictionary of items to validate. Use either this or kwargs
        :param kwargs: The items to validate. It should be a kwargs object with the same fields as the schema.
        :returns: Returns a dictionary with the validated items.
        :raises: Raises ``donttrust.ValidationError`` if validation fails
        """
        final = dict()
        try:
            if dict_ is None:
                for key in self._items.keys():
                    final[key] = self._items[key].validate(items.get(key))
            else:
                for key in self._items.keys():
                    final[key] = self._items[key].validate(dict_.get(key))
            return final
        except DontTrustBaseException as e:
            raise ValidationError(e.field, e.message)

    def validate_and_return_json_object(self, dict_=None, **items) -> dict:
        """
        Same as ``validate``, but returns a dictionary instead of throwing errors.

        Returns ``{"data": data}`` if validation succeedes, or ``{"error": message, "field": fieldname}`` if validation fails

        :param dict_: The dictionary of items to validate. Use either this or kwargs
        :param items: The items to validate. It should be a kwargs object with the same fields as the schema.
        :returns: The dictionary
        """
        try:
            final = self.validate(dict_, **items)
            return {"data": final}
        except ValidationError as e:
            return {"error": e.message, "field": e.field}

    def validate_without_exception(self, dict_=None, **items):
        """
        Same as ``validate``, but returns ``False`` if validation fails

        :param dict_: The dictionary of items to validate. Use either this or kwargs
        :param items: The items to validate. It should be a kwargs object with the same fields as the schema.
        :return: Returns a dictionary with validated data if validation succeeds, else returns False
        """
        try:
            return self.validate(dict_, **items)
        except ValidationError:
            return False
