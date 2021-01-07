import unittest,os

from donttrust import DontTrust, Schema


class Test(unittest.TestCase):
    def test_1(self):
        trust = DontTrust(username=Schema().string().alphanum().lower().required(), verified=Schema().boolean(),
                          password=Schema().string().required(), email=Schema().email().required().allow_tlds("com"),
                          access_token=Schema().string().alphanum().lower(), role=Schema().string().default("member"))
        self.assertTrue(trust.validate_without_exception(username="asdsad", password="sasdfghj", email="a@b.com"))
        self.assertFalse(trust.validate_without_exception(username="i"))
        self.assertTrue(trust.validate_without_exception(username="i", password="sadsdadsa", access_token="sadasdasd",
                                                          email="test@gmail.com", verified=True))
        self.assertFalse(trust.validate_without_exception(username="i", access_token="sadasdasd",
                                                          email="test@gmail.com", verified=True))

    def test2(self):
        trust = DontTrust(username=Schema().string().alphanum().lower().required().strip(),
                          password=Schema().string().required())
        self.assertTrue(trust.validate_without_exception({"username": "abcd", "password": "hello"}))
        self.assertFalse(trust.validate_without_exception({"username": "abcd"}))
        self.assertFalse(trust.validate_without_exception({"password": "abcd"}))


if __name__ == '__main__':
    unittest.main()
