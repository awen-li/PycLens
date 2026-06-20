# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: PyStringIOTest_test_lone_surrogates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass('\ud800')
    self.assertEqual(memio.read(), '\ud800')
    memio = self.ioclass()
    memio.write('\ud800')
    self.assertEqual(memio.getvalue(), '\ud800')
