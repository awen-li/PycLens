# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: UnionTests_test_cannot_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):

        class C(Union):
            pass
    with self.assertRaises(TypeError):

        class C(type(Union)):
            pass
    with self.assertRaises(TypeError):

        class C(Union[int, str]):
            pass
