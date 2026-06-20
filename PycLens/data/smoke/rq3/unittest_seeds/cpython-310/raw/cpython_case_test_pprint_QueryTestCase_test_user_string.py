# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_user_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = collections.UserString('')
    self.assertEqual(pprint.pformat(d, width=1), "''")
    d = collections.UserString('the quick brown fox jumped over a lazy dog')
    self.assertEqual(pprint.pformat(d, width=20), "('the quick brown '\n 'fox jumped over '\n 'a lazy dog')")
    self.assertEqual(pprint.pformat({1: d}, width=20), "{1: 'the quick '\n    'brown fox '\n    'jumped over a '\n    'lazy dog'}")
