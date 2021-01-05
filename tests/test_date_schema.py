import unittest
from datetime import datetime

from donttrust.schema import Schema


class Test(unittest.TestCase):
    def test_1(self):
        schema = Schema("test1").date().required().min('today').max("2022-12-31")

        self.assertTrue(schema.validate_without_exception("2021-04-01"))
        self.assertFalse(schema.validate_without_exception(None))
        self.assertFalse(schema.validate_without_exception("2020-12-10"))
        self.assertFalse(schema.validate_without_exception("dsa"))
        self.assertFalse(schema.validate_without_exception("2023-01-01"))

    def test_2(self):
        schema = Schema().date()
        schema.field = "asdasd"

        self.assertFalse(schema.validate_without_exception("dasdsadasd"))

    def test_3(self):
        schema = Schema().date().default("2020-10-10")

        self.assertEqual(schema.validate_without_exception(None), datetime.fromisoformat("2020-10-10"))


if __name__ == '__main__':
    unittest.main()
