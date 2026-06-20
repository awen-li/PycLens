# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading_local.py
# case: test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    suite = unittest.TestSuite()
    suite.addTest(DocTestSuite('_threading_local'))
    suite.addTest(unittest.makeSuite(ThreadLocalTest))
    suite.addTest(unittest.makeSuite(PyThreadingLocalTest))
    local_orig = _threading_local.local

    def setUp(test):
        _threading_local.local = _thread._local

    def tearDown(test):
        _threading_local.local = local_orig
    suite.addTest(DocTestSuite('_threading_local', setUp=setUp, tearDown=tearDown))
    support.run_unittest(suite)
