# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_writelines_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass()

    def error_gen():
        yield self.buftype('spam')
        raise KeyboardInterrupt
    self.assertRaises(KeyboardInterrupt, memio.writelines, error_gen())
