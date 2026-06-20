# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TupleTests_test_tuple_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyTuple(tuple):
        pass
    self.assertIsSubclass(MyTuple, Tuple)
    self.assertIsSubclass(Tuple, Tuple)
    self.assertIsSubclass(tuple, Tuple)
