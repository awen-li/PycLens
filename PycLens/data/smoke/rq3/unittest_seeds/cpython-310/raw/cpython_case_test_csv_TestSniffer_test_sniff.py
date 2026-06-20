# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestSniffer_test_sniff

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(self.sample1)
    self.assertEqual(dialect.delimiter, ',')
    self.assertEqual(dialect.quotechar, '"')
    self.assertIs(dialect.skipinitialspace, True)
    dialect = sniffer.sniff(self.sample2)
    self.assertEqual(dialect.delimiter, ':')
    self.assertEqual(dialect.quotechar, "'")
    self.assertIs(dialect.skipinitialspace, False)
