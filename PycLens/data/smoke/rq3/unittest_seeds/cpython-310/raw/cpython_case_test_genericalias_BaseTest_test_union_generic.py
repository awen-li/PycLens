# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_union_generic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = typing.Union[list[T], tuple[T, ...]]
    self.assertEqual(a.__args__, (list[T], tuple[T, ...]))
    self.assertEqual(a.__parameters__, (T,))
