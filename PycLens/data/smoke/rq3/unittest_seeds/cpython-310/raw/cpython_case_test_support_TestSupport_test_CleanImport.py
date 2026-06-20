# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_CleanImport

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import importlib
    with import_helper.CleanImport('pprint'):
        importlib.import_module('pprint')
