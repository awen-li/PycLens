# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_unpack_with_buffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data1 = array.array('B', b'\x124Vx')
    data2 = memoryview(b'\x124Vx')
    for data in [data1, data2]:
        (value,) = struct.unpack('>I', data)
        self.assertEqual(value, 305419896)
