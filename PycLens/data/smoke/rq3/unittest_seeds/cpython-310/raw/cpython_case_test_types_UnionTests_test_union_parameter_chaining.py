# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_union_parameter_chaining

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = typing.TypeVar('T')
    S = typing.TypeVar('S')
    self.assertEqual((float | list[T])[int], float | list[int])
    self.assertEqual(list[int | list[T]].__parameters__, (T,))
    self.assertEqual(list[int | list[T]][str], list[int | list[str]])
    self.assertEqual((list[T] | list[S]).__parameters__, (T, S))
    self.assertEqual((list[T] | list[S])[int, T], list[int] | list[T])
    self.assertEqual((list[T] | list[S])[int, int], list[int])
