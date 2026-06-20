# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_counter_subclass_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyCounter(typing.Counter[int]):
        pass
    d = MyCounter()
    self.assertIsInstance(d, MyCounter)
    self.assertIsInstance(d, typing.Counter)
    self.assertIsInstance(d, collections.Counter)
