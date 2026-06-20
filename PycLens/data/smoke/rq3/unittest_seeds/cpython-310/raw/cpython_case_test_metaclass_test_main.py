# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_metaclass.py
# case: test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    from test import support
    from test import test_metaclass
    support.run_doctest(test_metaclass, verbose)
