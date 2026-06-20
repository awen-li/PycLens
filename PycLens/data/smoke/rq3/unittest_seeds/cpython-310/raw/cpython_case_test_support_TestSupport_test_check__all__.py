# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_check__all__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    extra = {'tempdir'}
    not_exported = {'template'}
    support.check__all__(self, tempfile, extra=extra, not_exported=not_exported)
    extra = {'TextTestResult', 'installHandler'}
    not_exported = {'load_tests', 'TestProgram', 'BaseTestSuite'}
    support.check__all__(self, unittest, ('unittest.result', 'unittest.case', 'unittest.suite', 'unittest.loader', 'unittest.main', 'unittest.runner', 'unittest.signals', 'unittest.async_case'), extra=extra, not_exported=not_exported)
    self.assertRaises(AssertionError, support.check__all__, self, unittest)
