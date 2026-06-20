# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: UnquotingTests_test_unquoting_mixed_case

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = '%Ab%eA'
    expect = b'\xab\xea'
    result = urllib.parse.unquote_to_bytes(given)
    self.assertEqual(expect, result, 'using unquote_to_bytes(): %r != %r' % (expect, result))
