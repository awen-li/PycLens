# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_instance_dict_leak

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for _ in range(100):
        memio = self.ioclass()
        memio.foo = 1
