# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_parameter_detection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(List[T].__parameters__, (T,))
    self.assertEqual(List[List[T]].__parameters__, (T,))

    class A:
        __parameters__ = (T,)
    for a in (List, list):
        for b in (int, TypeVar, ParamSpec, types.GenericAlias, types.UnionType):
            with self.subTest(generic=a, sub=b):
                with self.assertRaisesRegex(TypeError, '.* is not a generic class|no type variables left'):
                    a[b][str]
    self.assertEqual(list[A()].__parameters__, (T,))
