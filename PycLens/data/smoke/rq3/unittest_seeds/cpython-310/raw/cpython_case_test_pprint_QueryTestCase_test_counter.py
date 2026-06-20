# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_counter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = collections.Counter()
    self.assertEqual(pprint.pformat(d, width=1), 'Counter()')
    d = collections.Counter('senselessness')
    self.assertEqual(pprint.pformat(d, width=40), "Counter({'s': 6,\n         'e': 4,\n         'n': 2,\n         'l': 1})")
