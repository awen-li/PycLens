# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    from doctest import DocFileSuite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MathTests))
    suite.addTest(unittest.makeSuite(IsCloseTests))
    suite.addTest(DocFileSuite('ieee754.txt'))
    run_unittest(suite)
