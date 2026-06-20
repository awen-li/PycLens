# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_reindent_multi

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(timeit.reindent('print()\npass\nbreak', 0), 'print()\npass\nbreak')
    self.assertEqual(timeit.reindent('print()\npass\nbreak', 4), 'print()\n    pass\n    break')
