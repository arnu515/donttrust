from typing import Dict

from .exceptions import DontTrustBaseException
from .schema import Schema


class ValidationError(Exception):
    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message


class DontTrust:
    _items: Dict[str, Schema] = dict()

    def __init__(self, **items: Schema):
        for key in items.keys():
            self._items[key] = items[key]
            self._items[key].field = key

    def validate(self, **kwargs):
        final = dict()
        try:
            for key in self._items.keys():
                final[key] = self._items[key].validate(kwargs.get(key))
            return final
        except DontTrustBaseException as e:
            raise ValidationError(e.field, e.message)

    def validate_and_return_json_object(self, **kwargs) -> dict:
        try:
            final = self.validate(**kwargs)
            return {"data": final}
        except ValidationError as e:
            return {"error": e.message, "field": e.field}

    def validate_without_exception(self, **kwargs):
        try:
            return self.validate(**kwargs)
        except ValidationError:
            return False
