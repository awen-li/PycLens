# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_netrc.py
# case: NetrcTestCase_test_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nrc = self.make_nrc('            machine host1.domain.com login log1 password pass1 account acct1\n            default login log2 password pass2\n            ')
    self.assertEqual(nrc.hosts['host1.domain.com'], ('log1', 'acct1', 'pass1'))
    self.assertEqual(nrc.hosts['default'], ('log2', None, 'pass2'))
    nrc2 = self.make_nrc(nrc.__repr__())
    self.assertEqual(nrc.hosts, nrc2.hosts)
