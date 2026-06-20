# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: PicklingTests_test_object_reduce

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    object().__reduce__()
    with self.assertRaises(TypeError):
        object().__reduce__(0)
    object().__reduce_ex__(0)
    with self.assertRaises(TypeError):
        object().__reduce_ex__()
    with self.assertRaises(TypeError):
        object().__reduce_ex__(None)
