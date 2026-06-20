# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: DoubleTest_test_alloc_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from sys import maxsize
    a = array.array('d', [-1] * 65536)
    try:
        a *= maxsize // 65536 + 1
    except MemoryError:
        pass
    else:
        self.fail('Array of size > maxsize created - MemoryError expected')
    b = array.array('d', [2.71828183, 3.14159265, -1])
    try:
        b * (maxsize // 3 + 1)
    except MemoryError:
        pass
    else:
        self.fail('Array of size > maxsize created - MemoryError expected')
