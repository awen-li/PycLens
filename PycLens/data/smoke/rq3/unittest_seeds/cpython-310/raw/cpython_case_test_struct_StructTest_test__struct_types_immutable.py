# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test__struct_types_immutable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Struct = struct.Struct
    unpack_iterator = type(struct.iter_unpack('b', b'x'))
    for cls in (Struct, unpack_iterator):
        with self.subTest(cls=cls):
            with self.assertRaises(TypeError):
                cls.x = 1
