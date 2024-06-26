# -*- coding: utf-8 -*-
"""
File with unittests.
"""
import filecmp
import unittest
from pathlib import Path

from learn_password.learn_logic import letter_to_word

from save_password.save_logic import default_save, user_path_save

from tune_password.tune_logic import add_comments, sanitize_password, tune_special_symbols

from what_send_ds.what_send_logic import add_new_path, choose_the_path, whole_path_list


class TestPassword(unittest.TestCase):
    """Just UnitTests."""

    # MAKING A PASSWORD BLOCK
    def test_tune_special_symbols(self):
        passw: str = '63fFZ-6wUnj_C_fDSF4A-AkHoe5nq0-A'
        pass_underscore_dash: str = '63fFZ6wUnjCfDSF4AAkHoe5nq0A'

        self.assertEqual(tune_special_symbols(passw, '_-'), pass_underscore_dash)

    def test_sanitize_password(self):
        passw: str = '63fFZ-6wUnj_C_TuM9KGDAQpa1NrL2n7-0J15q2pXs5s5Zsnak5Inq0-A'
        pass_digits_lower: str = 'FFZ-WUNJ_C_TUMKGDAQPANRLN-JQPXSSZSNAKINQ-A'

        self.assertEqual(sanitize_password(passw, 'diglow'), pass_digits_lower)

    def test_add_comments(self):
        password: str = 'STEAMX1RWIQ6F'
        comment: str = 'barak -lenobama'
        password_with_comment: str = 'STEAMX1RWIQ6F barak obama // length - 13'

        self.assertEqual(add_comments(password, comment), password_with_comment)

    # LEARN PASSWORD BLOCK
    def test_learn_letter_to_word(self):
        password: str = 'dhEapWDK'
        res_should_be: str = 'drip hulu EGG apple park WALMART DRIP KOREAN'
        res_we_have: str = letter_to_word(password)
        self.assertEqual(res_should_be, res_we_have)

    # SAVE A PASSWORD BLOCK
    def test_default_save(self):
        def_path_start = Path(__file__).parent / r'default_file_test\default_save_start.txt'
        def_path_end = Path(__file__).parent / r'default_file_test\default_save_end.txt'
        password = 'STEAMX1RWIQ6FWN1ZJZXXHH7S6LZS3'

        open(def_path_start, "w", encoding="UTF-8").close()

        # file 1 *working with it
        # file 2 *already has the pass inside*
        default_save(password, def_path_start)

        self.assertTrue(filecmp.cmp(def_path_start, def_path_end))

    def test_user_path_save(self):
        user_path_start = Path(__file__).parent / r'user_path_save_test\user_save_start.txt'
        user_path_end = Path(__file__).parent / r'user_path_save_test\user_save_end.txt'
        password = 'STEAMX1RWIQ6FWN1ZJZXXHH7S6LZS3'

        open(user_path_start, "w", encoding="UTF-8").close()

        # file 1 *working with it
        # file 2 *already has the pass inside*
        user_path_save(password, user_path_start)
        user_path_save(password * 2, user_path_start)

        self.assertTrue(filecmp.cmp(user_path_start, user_path_end))

    # SEND TO DISCORD BLOCK
    def test_add_new_path(self):
        save_pass_start = Path(__file__).parent / r'paths_to_txt_ds\test_pass_ways.txt'
        save_pass_end = Path(__file__).parent / r'paths_to_txt_ds\test_pass_ways2.txt'
        path = r'D:\gabe\csgo\moment'

        open(save_pass_start, "w", encoding="UTF-8").close()
        add_new_path(save_pass_start, path)  # file 1
        add_new_path(save_pass_end, path)

        self.assertTrue(filecmp.cmp(save_pass_start, save_pass_end))


if __name__ == '__main__':
    unittest.main()
    # python -m unit_tests.test_password
