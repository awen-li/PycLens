# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunModuleTestCase_test_invalid_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.expect_import_error('sys')
    self.expect_import_error('sys.imp.eric')
    self.expect_import_error('os.path.half')
    self.expect_import_error('a.bee')
    self.expect_import_error('.howard')
    self.expect_import_error('..eaten')
    self.expect_import_error('.test_runpy')
    self.expect_import_error('.unittest')
    self.expect_import_error('multiprocessing')
