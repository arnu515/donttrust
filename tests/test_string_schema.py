import unittest
import re

from donttrust.schema import Schema


class Test(unittest.TestCase):
    def test_1(self):
        schema = Schema("test1").string().required().lower().alphanum()
        self.assertEqual(schema.validate_without_exception("isatisfyalltests123"), "isatisfyalltests123")

    def test_2(self):
        schema = Schema("test2").required().disallow("testing13", 32).string().disallow("abc").strip()
        self.assertEqual(schema.validate_without_exception("                this_should_be_stripped"),
                         "this_should_be_stripped")
        self.assertEqual(schema.validate_without_exception("  ST rip agai n               "), "ST rip agai n")
        self.assertFalse(schema.validate_without_exception("testing13"))
        self.assertFalse(schema.validate_without_exception("abc"))

    def test_3(self):
        schema = Schema("test3").required().string().upper().regex(r"[\w-]+").flags(re.I).strip().to_lower()
        self.assertEqual(schema.validate_without_exception("                        ARNU515"), "arnu515")
        self.assertFalse(schema.validate_without_exception("!NV4L1D"))
        self.assertFalse(schema.validate_without_exception("invalid"))
        self.assertFalse(schema.validate_without_exception(None))
        self.assertFalse(schema.validate_without_exception(69))


if __name__ == '__main__':
    unittest.main()
