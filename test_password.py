import unittest
import tune_password as tp


class TestPassword(unittest.TestCase):

    def test_special_symbols(self):
        password = '63fFZ-6wUnj_C_fDSFfVQeT2uM9KGD54AQpa1NrL2nlBVzIba7LdUSYj7O-AkHoe0J1SkYG95q2p5XAwKsfUYI5s5Zsn1ak5I2HDD5nq0-A'
        password_without_underscore_and_dash = '63fFZ6wUnjCfDSFfVQeT2uM9KGD54AQpa1NrL2nlBVzIba7LdUSYj7OAkHoe0J1SkYG95q2p5XAwKsfUYI5s5Zsn1ak5I2HDD5nq0A'

        self.assertTrue(tp.checkslash(password, 0), password_without_underscore_and_dash)

    def test_up_low_dig(self):
        password = '63fFZ-6wUnj_C_fDSFfVQeT2uM9KGD54AQpa1NrL2nlBVzIba7LdUSYj7O-AkHoe0J1SkYG95q2p5XAwKsfUYI5s5Zsn1ak5I2HDD5nq0-A'
        password_without_digits_and_lower = '6FFZ-WUNJ_C_FDSFFVQETUMKGDAQPANRLNLBVZIBALDUSYJO-AKHOEJSKYGQPXAWKSFUYISZSNAKIHDDNQ-A'

        self.assertTrue(tp.up_low_dig(password, 0), password_without_digits_and_lower)


if __name__ == '__main__':
    unittest.main()
