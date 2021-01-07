import unittest

from donttrust.schema import Schema


class Test(unittest.TestCase):
    def test_1(self):
        schema = Schema("test1").required().email().allow_tlds("com").allow_mail_providers("gmail", "outlook")

        self.assertEqual(schema.validate("test@gmail.com"), "test@gmail.com")
        self.assertEqual(schema.validate_without_exception("test@outlook.com"), "test@outlook.com")

        self.assertFalse(schema.validate_without_exception("test@gmail.net"))
        self.assertFalse(schema.validate_without_exception("test@example.com"))

    def test_2(self):
        schema = Schema("test2").required().email()

        self.assertEqual(schema.validate_without_exception("test.man_1234@example13.com"), "test.man_1234@example13.com")

        self.assertFalse(schema.validate_without_exception(None))
        self.assertFalse(schema.validate_without_exception(2312))
        self.assertFalse(schema.validate_without_exception("te$t@gmail.com"))
        self.assertFalse(schema.validate_without_exception("testtest"))
        self.assertFalse(schema.validate_without_exception("test@gmail"))

    def test_3(self):
        schema = Schema("test3").email().disallow_tlds("net").disallow_mail_providers("gmail")

        self.assertEqual(schema.validate_without_exception(None), None)
        self.assertEqual(schema.validate_without_exception("abc@def.ghi"), "abc@def.ghi")
        self.assertEqual(schema.validate_without_exception("test@example.com"), "test@example.com")

        self.assertFalse(schema.validate_without_exception("hello@gmail.com"))
        self.assertFalse(schema.validate_without_exception("test@website.net"))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
