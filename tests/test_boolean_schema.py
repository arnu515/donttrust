import unittest

from donttrust.schema import Schema


class Test(unittest.TestCase):
    def test_1(self):
        schema = Schema("test1").boolean().required().falsy("no").truthy("yes")
        self.assertTrue(schema.validate_without_exception(True))
        self.assertTrue(schema.validate_without_exception("yes"))
        self.assertFalse(schema.validate_without_exception(False))
        self.assertFalse(schema.validate_without_exception("no"))

        self.assertFalse(schema.validate_without_exception(None))

    def test_2(self):
        schema = Schema("test2").boolean().strict().default(True)

        self.assertTrue(schema.validate_without_exception(None))
        self.assertTrue(schema.validate_without_exception(True))
        self.assertFalse(schema.validate_without_exception(False))
        self.assertFalse(schema.validate_without_exception("True"))

    def test_3(self):
        schema = Schema("test3").boolean().strict().truthy("test")

        self.assertFalse(schema.validate_without_exception("test"))
        self.assertTrue(schema.validate_without_exception(True))
        self.assertFalse(schema.validate_without_exception(False))
        self.assertFalse(schema.validate_without_exception(None))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
