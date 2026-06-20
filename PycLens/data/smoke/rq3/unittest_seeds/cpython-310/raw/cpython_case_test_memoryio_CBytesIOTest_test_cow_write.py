# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: CBytesIOTest_test_cow_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def mutation(memio):
        memio.seek(0)
        memio.write(b'foo')
    self._test_cow_mutation(mutation)
