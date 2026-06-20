# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_multiple_calls_to_get_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    loader = imp._LoadSourceCompatibility('imp', imp.__file__, open(imp.__file__, encoding='utf-8'))
    loader.get_data(imp.__file__)
    loader.get_data(imp.__file__)
