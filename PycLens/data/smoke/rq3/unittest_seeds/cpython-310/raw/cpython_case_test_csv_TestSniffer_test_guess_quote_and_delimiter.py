# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestSniffer_test_guess_quote_and_delimiter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sniffer = csv.Sniffer()
    for header in (";'123;4';", "'123;4';", ";'123;4'", "'123;4'"):
        with self.subTest(header):
            dialect = sniffer.sniff(header, ',;')
            self.assertEqual(dialect.delimiter, ';')
            self.assertEqual(dialect.quotechar, "'")
            self.assertIs(dialect.doublequote, False)
            self.assertIs(dialect.skipinitialspace, False)
