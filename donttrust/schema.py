from typing import Any, Set, Optional, Union
import datetime
import re

from .exceptions import DontTrustBaseException, RequiredException, DisallowedValueException, CharacterException, \
    RegexException, LengthException, TypeException, SizeException, MultipleException, IsNotBooleanException, \
    InvalidEmailException, InvalidDateException


class Schema(object):
    field: Optional[str] = None
    _type = Any

    _required = False
    _default_value: Any = None

    _allowed_values: Set[Any] = set()
    _disallowed_values: Set[Any] = set()

    def __init__(self, id_: str = "field"):
        """
        The base schema of DontTrust. Usually used as a schema of another type

        :param id_: Field of the schema. Optional unless using a specific class of schema.
        """
        self.field = id_

    def required(self):
        """
        Makes the field required
        """
        self._required = True
        return self

    def default(self, value: Any):
        """
        Used as default value if the value is ``None``.

        Does NOT work with ``required``.

        :param value: Value used as default
        """
        self._default_value = value
        return self

    def allow(self, *values):
        """
        Allow (whitelist) certain values. Blacklist is preferred over this.

        If the validation value is not in allowed values, validation fails.

        :param values: Values to allow
        """
        self._allowed_values = self._allowed_values.union(set(values))
        return self

    def disallow(self, *values):
        """
        Disallow (blacklist) certain values. Preferred over whitelist

        If the validation value is in disallowed values, validation fails.

        :param values: Values to disallow
        """
        self._disallowed_values = self._disallowed_values.union(set(values))
        return self

    def reset_disallow(self):
        """
        Removes all items from blacklist
        """
        self._disallowed_values = set()
        return self

    def reset_allow(self):
        """
        Removes all items from whitelist
        """
        self._allowed_values = set()
        return self

    def validate(self, value):
        """
        Validates the Schema with ``value``.

        :param value: Value to validate
        :return: Returns the validated value, or throws an exception if validation fails.
        """
        if (self._type is not None and value is not None) and (self._type != Any and type(value) != self._type):
            raise TypeException(self.field, str(self._type))

        if self._default_value and value is None:
            value = self._default_value

        if self._required and value is None:
            raise RequiredException(self.field)
        if value in self._disallowed_values or (self._allowed_values and value not in self._allowed_values):
            raise DisallowedValueException(self.field, value)
        return value

    def validate_without_exception(self, value):
        """
        Same as validate, but doesn't throw an exception and just returns ``False`` if validation fails.

        :param value: Value to validate
        :return: Returns the validated value or returns ``False`` if validation fails
        """
        try:
            return self.validate(value)
        except DontTrustBaseException:
            return False

    def validate_and_get_message(self, value):
        """
        Validates and gets the exception message (Exception is auto handled)

        :param value: Value to validate
        :return: Validated value or message
        """
        try:
            return self.validate(value)
        except DontTrustBaseException as e:
            return e.message

    def string(self):
        """
        Creates a string schema

        :return: The StringSchema
        """
        s = StringSchema(self.field)
        s._required = self._required
        s._allowed_values = set(filter(lambda x: type(x) == str, self._allowed_values))
        s._disallowed_values = set(filter(lambda x: type(x) == str, self._disallowed_values))
        return s

    def number(self):
        """
        Creates a number schema

        :return: The NumberSchema
        """
        s = NumberSchema(self.field)
        s._required = self._required
        s._allowed_values = set(filter(lambda x: type(x) in [int, float, complex], self._allowed_values))
        s._disallowed_values = set(filter(lambda x: type(x) in [int, float, complex], self._disallowed_values))
        return s

    def boolean(self):
        """
        Creates a boolean schema

        :return: The BooleanSchema
        """
        s = BooleanSchema(self.field)
        s._required = self._required
        return s

    def email(self):
        """
        Creates an email schema

        :return: The EmailSchema
        """
        s = EmailSchema(self.field)
        s._required = self._required
        s._allowed_values = set(filter(lambda x: type(x) == str, self._allowed_values))
        s._disallowed_values = set(filter(lambda x: type(x) == str, self._disallowed_values))
        return s

    def date(self):
        """
        Creates an date schema

        :return: The DateSchema
        """
        s = DateSchema(self.field)
        s._required = self._required
        return s


class StringSchema(Schema):
    _type = str

    _allowed_values: Set[str] = set()
    _disallowed_values: Set[str] = set()

    _min_length: int = 1
    _max_length: Optional[int] = None

    _strip = False
    _to_upper = False
    _to_lower = False

    _lower = False
    _upper = False
    _al_num = False

    _pattern: Optional[str] = None
    _flag: int = None

    def validate(self, value: str):
        value = super().validate(value)

        if value is None and not self._required:
            return value

        if self._strip:
            value = value.strip()

        if len(value) < self._min_length or 0:
            raise LengthException(self.field, self._min_length, False)
        elif self._max_length and len(value) > self._max_length:
            raise LengthException(self.field, self._max_length)

        if self._lower and not value.islower():
            raise CharacterException(self.field, "lowercase characters")

        if self._upper and not value.isupper():
            raise CharacterException(self.field, "uppercase characters")

        if self._al_num and not value.isalnum():
            raise CharacterException(self.field, "alpha-numeric characters")

        if self._pattern and not re.fullmatch(self._pattern, value, self._flag):
            raise RegexException(self.field, self._pattern)

        if self._to_lower:
            value = value.lower()

        if self._to_upper:
            value = value.upper()

        return value

    def allow_empty(self):
        """
        Allows empty strings
        """
        self._min_length = 0
        return self

    def min(self, length: int):
        """
        Set minimum length of the string
        """
        if length < 0:
            raise ValueError("Provide a positive integer!")
        self._min_length = length
        return self

    def max(self, length: int):
        """
        Set maximum length of the string
        """
        if length < 0:
            raise ValueError("Provide a positive integer!")
        self._max_length = length
        return self

    def strip(self):
        """
        Strip the string (trim its end of whitespaces) after validation
        """
        self._strip = True
        return self

    def lower(self):
        """
        String should be lowercase
        """
        self._lower = True
        return self

    def upper(self):
        """
        String should be uppercase
        """
        self._upper = True
        return self

    def alphanum(self):
        """
        String should be alphanumeric
        """
        self._al_num = True
        return self

    def regex(self, pattern: str):
        """
        String should match with the regex pattern
        """
        self._pattern = pattern
        return self

    def flags(self, flag: int):
        """
        A regex flag to use when compiling the regex defined in the ``regex()`` function
        """
        self._flag = flag
        return self

    def to_lower(self):
        """
        Make the string lowercase upon validation
        """
        self._to_lower = True
        return self

    def to_upper(self):
        """
        Make the string uppercase upon validation
        """
        self._to_upper = True
        return self


class NumberSchema(Schema):
    _allowed_values: Set[int] = set()
    _disallowed_values: Set[int] = set()

    _min: Optional[int] = None
    _max: Optional[int] = None

    _type = int

    _multiple_of: int = 1

    _add: int = None
    _subtract: int = None
    _divide: int = None
    _multiply: int = None

    def validate(self, value: int):
        super().validate(value)

        if value is None and not self._required:
            return value

        if self._min and value < self._min:
            raise SizeException(self.field, self._min, False)

        if self._max and value > self._max:
            raise SizeException(self.field, self._max, True)

        if value % self._multiple_of != 0:
            raise MultipleException(self.field, self._multiple_of)

        if self._add:
            value += self._add

        if self._subtract:
            value -= self._subtract

        if self._multiply:
            value *= self._multiply

        if self._subtract:
            value /= self._divide

        return value

    def min(self, num: int):
        """
        Number should be atleast this value
        """
        self._min = num
        return self

    def max(self, num: int):
        """
        Number should be lesser than this value
        """
        self._max = num
        return self

    def port(self):
        """
        Number should be within the range of 0-65535
        """
        self.max(65535)
        self.min(0)
        return self

    def equals(self, num: int):
        """
        Number should equal this number
        """
        self.min(num)
        self.max(num)
        return self

    def positive(self):
        """
        Number should be positive (includes zero)
        """
        self.min(0)
        self._max = None
        return self

    def negative(self):
        """
        Number should be negative
        """
        self.max(-1)
        self._min = None
        return self

    def int(self):
        """
        Number should be of ``int`` datatype
        """
        self._type = int
        return self

    def float(self):
        """
        Number should be of ``float`` datatype
        """
        self._type = float
        return self

    def complex(self):
        """
        Number should be of ``complex`` datatype
        """
        self._type = complex
        return self

    def multiple(self, num: int):
        """
        Number should be a multiple of this number
        """
        self._multiple_of = num
        return self

    def divisible(self, num: int):
        """
        Alias of ``multiple``
        """
        return self.multiple(num)

    def add(self, num: int):
        """
        Add this number to the Number after validation
        """
        self._add = num
        return self

    def subtract(self, num: int):
        """
        Subtract this number from the Number after validation
        """
        self._subtract = num
        return self

    def multiply(self, num: int):
        """
        Multiply this number to the Number after validation
        """
        self._multiply = num
        return self

    def divide(self, num: int):
        """
        Divide the Number from this number after validation
        """
        self._divide = num
        return self


class BooleanSchema(Schema):
    _truthy_values: Set[any] = set()
    _falsy_values: Set[any] = set()

    _strict = False
    _default_value = False

    def validate(self, value):
        value = super().validate(value)

        if value is None and not self._required:
            return value

        if self._strict and value not in [True, False]:
            raise IsNotBooleanException(self.field)

        if type(value) == bool:
            return value

        if value in self._truthy_values:
            return True
        elif value in self._falsy_values:
            return False
        elif not self._strict:
            return bool(value)

    def __init__(self, id_: str):
        super().__init__(id_)
        self._truthy_values = {True}
        self._falsy_values = {False}

    def reset_disallow(self):
        pass

    def disallow_all(self):
        pass

    def reset_allow(self):
        pass

    def allow(self, *values):
        pass

    def disallow(self, *values):
        pass

    def truthy(self, value):
        """
        Add a value to be validated as ``True``
        """
        self._truthy_values.add(value)
        return self

    def falsy(self, value):
        """
        Add a value to be validated as ``False``
        """
        self._falsy_values.add(value)
        return self

    def strict(self):
        """
        Don't allow any values other than True or False
        """

        self._type = bool
        self._truthy_values = set()
        self._falsy_values = set()
        self._strict = True
        return self


class EmailSchema(Schema):
    _allowed_tlds: Set[str] = set()
    _disallowed_tlds: Set[str] = set()

    _allowed_mail_providers: Set[str] = set()
    _disallowed_mail_providers: Set[str] = set()

    _type = str

    def validate(self, value: str):
        value = super().validate(value)

        if value is None and not self._required:
            return value

        if not re.fullmatch(r"[\w._]+@[\w.]+\.[\w]+", value, re.I):
            raise InvalidEmailException(self.field, "\"{}\" is not in the format username@domain.tlds")

        try:
            username, domain = value.split("@")
        except ValueError:
            raise InvalidEmailException(self.field, "\"{}\" is not in the format username@domain.tlds")

        if not username or not domain:
            raise InvalidEmailException(self.field, "\"{}\" is not in the format username@domain.tlds")

        if '@' in username or '@' in domain:
            raise InvalidEmailException(self.field, "\"{}\" is not in the format username@domain.tlds")

        domain = domain.split(".")

        if len(domain) < 2:
            raise InvalidEmailException(self.field, "The domain of \"{}\" is not in the format domain.tlds")

        tlds = domain[-1]
        domain = ".".join(domain[:-1])

        if tlds in self._disallowed_tlds or (self._allowed_tlds and tlds not in self._allowed_tlds):
            raise InvalidEmailException(self.field, "The tlds of \"{}\" is not allowed")

        if domain in self._disallowed_mail_providers or (self._allowed_mail_providers and domain not in
                                                         self._allowed_mail_providers):
            raise InvalidEmailException(self.field, "The mail provider of \"{}\" is not allowed")

        return value

    def reset_disallow(self):
        pass

    def disallow_all(self):
        pass

    def reset_allow(self):
        pass

    def allow(self, *values):
        pass

    def disallow(self, *values):
        pass

    def allow_tlds(self, *tlds: str):
        """
        Only allow these top level domains (.com, .net) to be a part of the email
        """
        self._allowed_tlds = self._allowed_tlds.union(set(tlds))
        return self

    def disallow_tlds(self, *tlds: str):
        """
        Don't allow these top level domains (.com, .net) to be a part of the email
        """
        self._disallowed_tlds = self._disallowed_tlds.union(set(tlds))
        return self

    def disallow_mail_providers(self, *mail_providers: str):
        """
        Don't allow these mail providers (exluding the tlds)
        """
        self._disallowed_mail_providers = self._disallowed_mail_providers.union(set(mail_providers))
        return self

    def allow_mail_providers(self, *mail_providers: str):
        """
        Only allow these mail providers (exluding the tlds)
        """
        self._allowed_mail_providers = self._allowed_mail_providers.union(set(mail_providers))
        return self


class DateSchema(Schema):
    _min: Optional[datetime.datetime] = None
    _max: Optional[datetime.datetime] = None

    def validate(self, value: Union[datetime.datetime, str, int]):
        value = super().validate(value)

        if value is None and not self._required:
            return value

        date = self.__get_date(value, False)
        if self._min and date < self._min:
            raise InvalidDateException(self.field, "\"{}\" should be greater than " + self._max.strftime("%Y-%m-%d"))
        if self._max and date > self._max:
            raise InvalidDateException(self.field, "\"{}\" should be less than than " + self._max.strftime("%Y-%m-%d"))

        return date

    def __get_date(self, value: Union[datetime.datetime, str, int], allow_today=True) -> datetime.datetime:
        date = None
        if allow_today and value == "today":
            date = datetime.datetime.utcnow()
        elif type(value) == str:
            try:
                date = datetime.datetime.fromisoformat(value)
            except ValueError:
                raise InvalidDateException(self.field, "\"{}\" has an invalid date format. Correct format: YYYY-MM-DD")
        elif type(value) == int:
            date = datetime.datetime.fromtimestamp(value)
        return date

    def min(self, date: Union[datetime.datetime, str, int]):
        """
        The date should be atleast this date
        """
        self._min = self.__get_date(date)
        return self

    def max(self, date: Union[datetime.datetime, str, int]):
        """
        The date should be less than this date
        """
        self._max = self.__get_date(date)
        return self
