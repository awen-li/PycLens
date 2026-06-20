# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if isinstance(FlagStooges, Exception):
        raise FlagStooges
    test_pickle_dump_load(self.assertIs, FlagStooges.CURLY | FlagStooges.MOE)
    test_pickle_dump_load(self.assertIs, FlagStooges)
