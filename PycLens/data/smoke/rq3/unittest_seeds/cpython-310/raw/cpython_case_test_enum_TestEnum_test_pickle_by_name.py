# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_pickle_by_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ReplaceGlobalInt(IntEnum):
        ONE = 1
        TWO = 2
    ReplaceGlobalInt.__reduce_ex__ = enum._reduce_ex_by_name
    for proto in range(HIGHEST_PROTOCOL):
        self.assertEqual(ReplaceGlobalInt.TWO.__reduce_ex__(proto), 'TWO')
