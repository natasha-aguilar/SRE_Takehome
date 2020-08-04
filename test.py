# -*- coding: utf-8 -*-
import unittest


target = __import__("password_validator")
check_char_min_len = target.check_char_min_len
check_char_max_len = target.check_char_max_len
check_is_ascii = target.check_is_ascii
check_is_common_pwd = target.check_is_common_pwd

class TestPasswordMin(unittest.TestCase):
    def test_pwd_below_min(self):
        """
        Test that input password is below 8 character min
        """
        inputPwd = '$hikhar'
        result = check_char_min_len(inputPwd)
        self.assertFalse(result, False)

    def test_pwd_above_min(self):
        """
        Test that input password meets 8 character min
        """
        inputPwd = '#sr08cs009'
        result = check_char_min_len(inputPwd)
        self.assertTrue(result, True)
    
    def test_pwd_below_max(self):
        """
        Test that input password is below 64 character max
        """
        inputPwd = '#sr08cs009'
        result = check_char_max_len(inputPwd)
        self.assertTrue(result, True)

    def test_pwd_above_max(self):
        """
        Test that input password is above 64 character max
        """
        inputPwd = 'asdfsadasdfsfsdfsdfsdfdsfsdfsdfsdfsdfsdfsdf2352345asdfsadasdfsfsdfsdfsdfdsfsdfsdfsdfsdfsdfsdf2352345'
        result = check_char_max_len(inputPwd)
        self.assertFalse(result, False)

    def test_pwd_is_ascii(self):
        """
        Test that input password is ascii
        """
        inputPwd = '09   sdfsdf'
        result = check_is_ascii(inputPwd)
        self.assertTrue(result, True)

    def test_pwd_is_not_ascii(self):
        """
        Test that input password is not ascii
        """
        self.string_utf8 = '¡¡¡§§'
        result = check_is_ascii(self.string_utf8)
        self.assertFalse(result, False)

    def test_pwd_is_not_common(self):
        """
        Test that input password is not common
        """
        weak_pwds = ['password1', 'watermelon', 'texans']
        result = check_is_common_pwd('P@$s->word', weak_pwds)
        self.assertFalse(result, False)

    def test_pwd_is_common(self):
        """
        Test that input password is common
        """
        weak_pwds = ['password1', 'watermelon', 'texans']
        result = check_is_common_pwd('password1', weak_pwds)
        self.assertTrue(result, True)



if __name__ == '__main__':
    unittest.main()