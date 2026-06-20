# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_all_repr_eq_any

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    objs = (getattr(typing, el) for el in typing.__all__)
    for obj in objs:
        self.assertNotEqual(repr(obj), '')
        self.assertEqual(obj, obj)
        if getattr(obj, '__parameters__', None) and len(obj.__parameters__) == 1:
            self.assertEqual(obj[Any].__args__, (Any,))
        if isinstance(obj, type):
            for base in obj.__mro__:
                self.assertNotEqual(repr(base), '')
                self.assertEqual(base, base)
