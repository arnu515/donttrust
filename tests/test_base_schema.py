import unittest
from donttrust.schema import Schema


class Test(unittest.TestCase):
    def test_schema_1(self):
        schema = Schema("test1").required().allow("testing", "man", "1")
        self.assertTrue(schema.validate_without_exception("man"))
        self.assertFalse(schema.validate_without_exception("asd"))
        self.assertFalse(schema.validate_without_exception(None))

    def test_schema_2(self):
        schema = Schema("test2").disallow(1, "sada", False)
        self.assertTrue(schema.validate_without_exception(None))
        self.assertTrue(schema.validate_without_exception("test"))
        self.assertFalse(schema.validate_without_exception(False))
        self.assertFalse(schema.validate_without_exception(1))

    def test_schema_3(self):
        schema = Schema("test3").required()
        self.assertFalse(schema.validate_without_exception(None))
        self.assertTrue(schema.validate_without_exception("asodkpasodk"))
        self.assertTrue(schema.validate_without_exception(""))


if __name__ == '__main__':
    unittest.main()
