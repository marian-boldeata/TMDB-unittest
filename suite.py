import unittest

import HtmlTestRunner

from test_login import Test_Login
from test_search import Test_Search

class TestSuite(unittest.TestCase):

    lista_teste = unittest.TestSuite()
    lista_teste.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Test_Login),
                        unittest.defaultTestLoader.loadTestsFromTestCase(Test_Search))

    runner  = HtmlTestRunner.HTMLTestRunner(combine_reports=True,report_title='Raport', report_name="Rezultate Test")

    runner.run(lista_teste)
