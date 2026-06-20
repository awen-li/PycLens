# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_illegal_patma_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):

        class Both(Collection):
            __abc_tpflags__ = Sequence.__flags__ | Mapping.__flags__
