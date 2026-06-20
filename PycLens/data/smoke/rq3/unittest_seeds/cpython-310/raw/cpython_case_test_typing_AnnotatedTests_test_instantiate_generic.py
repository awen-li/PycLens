# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: AnnotatedTests_test_instantiate_generic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    MyCount = Annotated[typing.Counter[T], 'my decoration']
    self.assertEqual(MyCount([4, 4, 5]), {4: 2, 5: 1})
    self.assertEqual(MyCount[int]([4, 4, 5]), {4: 2, 5: 1})
