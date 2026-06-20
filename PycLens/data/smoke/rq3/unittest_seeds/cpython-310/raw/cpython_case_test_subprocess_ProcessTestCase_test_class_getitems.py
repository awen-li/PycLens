# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_class_getitems

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(subprocess.Popen[bytes], types.GenericAlias)
    self.assertIsInstance(subprocess.CompletedProcess[str], types.GenericAlias)
