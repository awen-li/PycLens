# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TupleTests_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        issubclass(Tuple, Tuple[int, str])
    with self.assertRaises(TypeError):
        issubclass(tuple, Tuple[int, str])

    class TP(tuple):
        ...
    self.assertIsSubclass(tuple, Tuple)
    self.assertIsSubclass(TP, Tuple)
