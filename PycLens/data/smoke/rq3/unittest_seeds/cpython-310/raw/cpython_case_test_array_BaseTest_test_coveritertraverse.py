# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_coveritertraverse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        import gc
    except ImportError:
        self.skipTest('gc module not available')
    a = array.array(self.typecode)
    l = [iter(a)]
    l.append(l)
    gc.collect()
