# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_pickle_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if isinstance(FloatStooges, Exception):
        raise FloatStooges
    test_pickle_dump_load(self.assertIs, FloatStooges.CURLY)
    test_pickle_dump_load(self.assertIs, FloatStooges)
