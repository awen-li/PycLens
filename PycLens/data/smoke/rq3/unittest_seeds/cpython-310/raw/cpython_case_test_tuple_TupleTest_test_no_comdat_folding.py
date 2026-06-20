# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tuple.py
# case: TupleTest_test_no_comdat_folding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class T(tuple):
        pass
    with self.assertRaises(TypeError):
        [3] + T((1, 2))
