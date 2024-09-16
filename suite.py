import unittest

import HtmlTestRunner

from test_login import Test_Login
from test_search import Test_Search
from test_translate import Test_Translate
from test_signup import Test_Signup
from test_watchlist import Test_Watchlist


class TestSuite(unittest.TestCase):

    def run_suite(self):

        lista_teste = unittest.TestSuite()
        lista_teste.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Test_Login),
                        unittest.defaultTestLoader.loadTestsFromTestCase(Test_Search),
                        unittest.defaultTestLoader.loadTestsFromTestCase(Test_Translate),

                        unittest.defaultTestLoader.loadTestsFromTestCase(Test_Watchlist)])
        # removed unittest.defaultTestLoader.loadTestsFromTestCase(Test_Signup) because if chapta


        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True,report_title='Raport', report_name="Rezultate Test")

        runner.run(lista_teste)

if __name__ == "__main__":
    suite = TestSuite()
    suite.run_suite()
