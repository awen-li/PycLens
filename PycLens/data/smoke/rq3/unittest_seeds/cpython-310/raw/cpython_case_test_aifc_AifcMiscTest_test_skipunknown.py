# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AifcMiscTest_test_skipunknown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = aifc.open(findfile('Sine-1000Hz-300ms.aif'))
    f.close()
