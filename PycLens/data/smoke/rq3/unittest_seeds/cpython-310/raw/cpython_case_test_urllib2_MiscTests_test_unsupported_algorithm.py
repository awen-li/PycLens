# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: MiscTests_test_unsupported_algorithm

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler = AbstractDigestAuthHandler()
    with self.assertRaises(ValueError) as exc:
        handler.get_algorithm_impls('invalid')
    self.assertEqual(str(exc.exception), "Unsupported digest authentication algorithm 'invalid'")
