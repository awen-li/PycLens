# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: StateTestCase_test_skip_with_no_name_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bdb = Bdb(skip=['anything*'])
    self.assertIs(bdb.is_skipped_module(None), False)
