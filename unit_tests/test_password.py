import unittest
import filecmp
from pathlib import Path
from tune_password.tune_logic import tune_special_symbols, sanitize_password, add_comments
from save_password.save_logic import default_save, user_path_save
from what_send_ds.what_send_logic import add_new_path, whole_path_list, choose_the_path
from learn_password.learn_logic import letter_to_word


class TestPassword(unittest.TestCase):
    """
    just UnitTests
    """

    # MAKING A PASSWORD BLOCK
    def test_tune_special_symbols(self):
        passw = '63fFZ-6wUnj_C_fDSF4A-AkHoe5nq0-A'
        pass_underscore_dash = '63fFZ6wUnjCfDSF4AAkHoe5nq0A'

        self.assertEqual(tune_special_symbols(passw, '_-'), pass_underscore_dash)

    def test_sanitize_password(self):
        passw = '63fFZ-6wUnj_C_T2uM9KGD54AQpa1NrL2n7-0J15q2p5Xs5s5Zsn1ak5Inq0-A'
        pass_digits_lower = 'FFZ-WUNJ_C_TUMKGDAQPANRLN-JQPXSSZSNAKINQ-A'

        self.assertEqual(sanitize_password(passw, 'diglow'), pass_digits_lower)

    def test_add_comments(self):
        password = 'STEAMX1RWIQ6FWN1ZJZ'
        comment = 'barak -lenobama'
        password_with_comment = 'STEAMX1RWIQ6FWN1ZJZ barak obama // length - 19'

        self.assertEqual(add_comments(password, comment), password_with_comment)

    # LEARN PASSWORD BLOCK
    def test_learn_letter_to_word(self):
        password = 'dIhEapWDK'
        res_should_be = 'drip IPHONE hulu EGG apple park WALMART DRIP KOREAN'
        res_we_have = letter_to_word(password)
        self.assertEqual(res_should_be, res_we_have)

    # SAVE A PASSWORD BLOCK
    def test_default_save(self):
        def_path_start = Path(__file__).parent / r'default_file_test\default_save_start.txt'
        def_path_end = Path(__file__).parent / r'default_file_test\default_save_end.txt'
        password = 'STEAMX1RWIQ6FWN1ZJZXXHH7S6LZS3'

        open(def_path_start, "w").close()

        # file 1 *working with it
        # file 2 *already has the pass inside*
        default_save(password, def_path_start)

        self.assertTrue(filecmp.cmp(def_path_start, def_path_end))

    def test_user_path_save(self):
        user_path_start = Path(__file__).parent / r'user_path_save_test\user_save_start.txt'
        user_path_end = Path(__file__).parent / r'user_path_save_test\user_save_end.txt'
        password = 'STEAMX1RWIQ6FWN1ZJZXXHH7S6LZS3'

        open(user_path_start, "w").close()

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

        open(save_pass_start, "w").close()
        add_new_path(save_pass_start, path)  # file 1
        add_new_path(save_pass_end, path)

        self.assertTrue(filecmp.cmp(save_pass_start, save_pass_end))


if __name__ == '__main__':
    unittest.main()
    # python -m unit_tests.test_password
