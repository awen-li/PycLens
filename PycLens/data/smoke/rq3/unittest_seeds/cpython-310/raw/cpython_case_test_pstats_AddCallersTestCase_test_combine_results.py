# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pstats.py
# case: AddCallersTestCase_test_combine_results

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    target = {'a': (1, 2, 3, 4)}
    source = {'a': (1, 2, 3, 4), 'b': (5, 6, 7, 8)}
    new_callers = pstats.add_callers(target, source)
    self.assertEqual(new_callers, {'a': (2, 4, 6, 8), 'b': (5, 6, 7, 8)})
    target = {'a': 1}
    source = {'a': 1, 'b': 5}
    new_callers = pstats.add_callers(target, source)
    self.assertEqual(new_callers, {'a': 2, 'b': 5})
