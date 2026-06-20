# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestSniffer_test_delimiters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(self.sample3)
    self.assertIn(dialect.delimiter, self.sample3)
    dialect = sniffer.sniff(self.sample3, delimiters='?,')
    self.assertEqual(dialect.delimiter, '?')
    dialect = sniffer.sniff(self.sample3, delimiters='/,')
    self.assertEqual(dialect.delimiter, '/')
    dialect = sniffer.sniff(self.sample4)
    self.assertEqual(dialect.delimiter, ';')
    dialect = sniffer.sniff(self.sample5)
    self.assertEqual(dialect.delimiter, '\t')
    dialect = sniffer.sniff(self.sample6)
    self.assertEqual(dialect.delimiter, '|')
    dialect = sniffer.sniff(self.sample7)
    self.assertEqual(dialect.delimiter, '|')
    self.assertEqual(dialect.quotechar, "'")
    dialect = sniffer.sniff(self.sample8)
    self.assertEqual(dialect.delimiter, '+')
    dialect = sniffer.sniff(self.sample9)
    self.assertEqual(dialect.delimiter, '+')
    self.assertEqual(dialect.quotechar, "'")
