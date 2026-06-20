# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: QuotingTests_test_quoting_plus

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(urllib.parse.quote_plus('alpha+beta gamma'), 'alpha%2Bbeta+gamma')
    self.assertEqual(urllib.parse.quote_plus('alpha+beta gamma', '+'), 'alpha+beta+gamma')
    self.assertEqual(urllib.parse.quote_plus(b'alpha+beta gamma'), 'alpha%2Bbeta+gamma')
    self.assertEqual(urllib.parse.quote_plus('alpha+beta gamma', b'+'), 'alpha+beta+gamma')
