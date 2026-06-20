# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_issue_35321

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _frozen_importlib_external
    self.assertEqual(_frozen_importlib_external.__spec__.origin, 'frozen')
    import _frozen_importlib
    self.assertEqual(_frozen_importlib.__spec__.origin, 'frozen')
