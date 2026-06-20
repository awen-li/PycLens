# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: ImportSideEffectTests_test_setting_copyright

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(hasattr(builtins, 'copyright'))
    self.assertTrue(hasattr(builtins, 'credits'))
    self.assertTrue(hasattr(builtins, 'license'))
