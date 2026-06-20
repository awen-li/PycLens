# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: GeneratorTest_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        yield 1
    g = f()
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.assertRaises((TypeError, pickle.PicklingError)):
            pickle.dumps(g, proto)
