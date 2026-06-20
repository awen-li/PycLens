# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: UnpackIteratorTest_test_uninstantiable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    iter_unpack_type = type(struct.Struct('>ibcp').iter_unpack(b''))
    self.assertRaises(TypeError, iter_unpack_type)
