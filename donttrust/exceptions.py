class DontTrustBaseException(Exception):
    __message: str
    field: str

    def __init__(self, field: str, message: str):
        """
        BaseException used by Schemas. Handle all exceptions (except ``donttrust.ValidationError``) by handling this
        exception.

        :param field: Field causing the issue.
        :param message: Custom message. Formatted with the field using ``str.format()``.
        """
        self.field = field
        self.__message = message

    def __dict__(self):
        """
        :return: Returns a JSON serializable dictionary.
        """
        return dict({self.field: self.message})

    @property
    def message(self):
        """
        :return: Formatted message
        """
        return self.__message


class RequiredException(DontTrustBaseException):
    def __init__(self, field: str):
        self.field = field
        self.__message = "\"{}\" is a required field, but is missing"

    @property
    def message(self):
        return self.__message.format(self.field)


class DisallowedValueException(DontTrustBaseException):
    value: str

    def __init__(self, field: str, value: str):
        self.field = field
        self.value = value
        self.__message = "\"{}\" is not allowed as a value of \"{}\"."

    @property
    def message(self):
        return self.__message.format(self.value, self.field)


class LengthException(DontTrustBaseException):
    length: int
    min_max: bool

    def __init__(self, field: str, length: int, min_max=True):
        self.field = field
        self.length = length
        self.min_max = min_max
        if self.min_max:
            self.__message = "\"{}\" must be {} characters or less"
        else:
            self.__message = "\"{}\" must be {} characters or more"

    @property
    def message(self):
        return self.__message.format(self.field, self.length)


class CharacterException(DontTrustBaseException):
    charset: str

    def __init__(self, field: str, charset: str):
        self.field = field
        self.charset = charset
        self.__message = "\"{}\" should only contain {}"

    @property
    def message(self):
        return self.__message.format(self.field, self.charset)


class RegexException(CharacterException):
    def __init__(self, field: str, charset: str):
        super().__init__(field, charset)
        self.__message = "\"{}\" does not satisfy the regex {}"


class TypeException(DontTrustBaseException):
    type: str

    def __init__(self, field: str, type_: str):
        self.field = field
        self.type = type_
        self.__message = "\"{}\" should be of type {}"

    @property
    def message(self):
        return self.__message.format(self.field, self.type)


class SizeException(LengthException):
    def __init__(self, field: str, length: int, min_max: bool):
        super().__init__(field, length, min_max)
        if self.min_max:
            self.__message = "\"{}\" should be greater than {}"
        else:
            self.__message = "\"{}\" should be less than {}"


class MultipleException(DontTrustBaseException):
    num: int

    def __init__(self, field: str, num: int):
        self.field = field
        self.num = num
        self.__message = "\"{}\" should be a multiple of {}"

    @property
    def message(self):
        return self.__message.format(self.field, self.num)


class IsNotBooleanException(DontTrustBaseException):
    def __init__(self, field: str):
        self.field = field
        self.__message = "\"{}\" should be a boolean, i.e. it should be either True or False"


class InvalidEmailException(DontTrustBaseException):
    def __init__(self, field: str, message: str):
        self.field = field
        self.__message = message

    @property
    def message(self):
        return self.__message.format(self.field)


class InvalidDateException(DontTrustBaseException):
    def __init__(self, field: str, message: str):
        self.field = field
        self.__message = message

    @property
    def message(self):
        return self.__message.format(self.field)
