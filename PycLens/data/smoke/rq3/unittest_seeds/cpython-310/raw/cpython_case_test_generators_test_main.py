# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    from test import support, test_generators
    support.run_unittest(__name__)
    support.run_doctest(test_generators, verbose)
