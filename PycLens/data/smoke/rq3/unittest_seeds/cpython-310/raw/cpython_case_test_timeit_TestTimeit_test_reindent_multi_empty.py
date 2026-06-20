# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_reindent_multi_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(timeit.reindent('\n\n', 0), '\n\n')
    self.assertEqual(timeit.reindent('\n\n', 4), '\n    \n    ')
