# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: DocTests_test_doc_tests

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (failed, tried) = doctest.testmod(statistics, optionflags=doctest.ELLIPSIS)
    self.assertGreater(tried, 0)
    self.assertEqual(failed, 0)
