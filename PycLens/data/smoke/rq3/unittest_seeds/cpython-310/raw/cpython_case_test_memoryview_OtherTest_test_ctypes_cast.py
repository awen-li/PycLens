# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: OtherTest_test_ctypes_cast

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctypes = import_helper.import_module('ctypes')
    p6 = bytes(ctypes.c_double(0.6))
    d = ctypes.c_double()
    m = memoryview(d).cast('B')
    m[:2] = p6[:2]
    m[2:] = p6[2:]
    self.assertEqual(d.value, 0.6)
    for format in 'Bbc':
        with self.subTest(format):
            d = ctypes.c_double()
            m = memoryview(d).cast(format)
            m[:2] = memoryview(p6).cast(format)[:2]
            m[2:] = memoryview(p6).cast(format)[2:]
            self.assertEqual(d.value, 0.6)
