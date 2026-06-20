# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: StrTest_test_encode_utf32

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        return self.basic_encode_test(size, 'utf32', expectedsize=4 * size + 4)
    except MemoryError:
        pass
