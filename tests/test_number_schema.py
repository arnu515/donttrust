import unittest

from donttrust.schema import Schema


class Test(unittest.TestCase):
    def test_1(self):
        schema = Schema("test1").required().number().allow(1, 2, 3)
        self.assertEqual(schema.multiply(5).validate_without_exception(15 // 5), 15)
        self.assertFalse(schema.validate_without_exception(5))
        self.assertFalse(schema.validate_without_exception(None))
        self.assertFalse(schema.validate_without_exception("abcd"))

    def test_2(self):
        schema = Schema("test2").number().disallow(15).min(5).max(500).float().multiply(3)
        self.assertEqual(schema.validate_without_exception(5.0), 15)
        self.assertFalse(schema.validate_without_exception(50000.0))
        self.assertFalse(schema.validate_without_exception(3.0))
        self.assertFalse(schema.validate_without_exception(19))
        self.assertFalse(schema.validate_without_exception(None), None)

    def test_3(self):
        schema = Schema("test2.1").number()
        self.assertFalse(schema.validate_without_exception("okaobkeokboerkoek"))
        self.assertEqual(schema.validate_without_exception(None), None)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
