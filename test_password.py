import unittest
from tune_password.tune_logic import tune_symbols, up_low_dig, add_comments


class TestPassword(unittest.TestCase):

    def test_special_symbols(self):
        password = '63fFZ-6wUnj_C_fDSFfVQeT2uM9KGD54AQpa1NrL2nlBVzIba7LdUSYj7O-AkHoe0J1SkYG95q2p5XAwKsfUYI5s5Zsn1ak5I2HDD5nq0-A'
        password_without_underscore_and_dash = '63fFZ6wUnjCfDSFfVQeT2uM9KGD54AQpa1NrL2nlBVzIba7LdUSYj7OAkHoe0J1SkYG95q2p5XAwKsfUYI5s5Zsn1ak5I2HDD5nq0A'

        self.assertTrue(tune_symbols(password, '_-'), password_without_underscore_and_dash)

    def test_up_low_dig(self):
        password = '63fFZ-6wUnj_C_fDSFfVQeT2uM9KGD54AQpa1NrL2nlBVzIba7LdUSYj7O-AkHoe0J1SkYG95q2p5XAwKsfUYI5s5Zsn1ak5I2HDD5nq0-A'
        password_without_digits_and_lower = '6FFZ-WUNJ_C_FDSFFVQETUMKGDAQPANRLNLBVZIBALDUSYJO-AKHOEJSKYGQPXAWKSFUYISZSNAKIHDDNQ-A'

        self.assertTrue(up_low_dig(password, 'diglow'), password_without_digits_and_lower)

    def test_comment(self):
        password = 'STEAMX1RWIQ6FWN1ZJZXXHH7S6LZS3'
        comment = 'barak -lenobama'
        password_with_comment = 'STEAMX1RWIQ6FWN1ZJZXXHH7S6LZS3 barak obama // length - 30'

        self.assertTrue(add_comments(password, comment), password_with_comment)


if __name__ == '__main__':
    unittest.main()
