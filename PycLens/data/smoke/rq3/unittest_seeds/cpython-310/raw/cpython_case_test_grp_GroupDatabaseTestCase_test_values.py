# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grp.py
# case: GroupDatabaseTestCase_test_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    entries = grp.getgrall()
    for e in entries:
        self.check_value(e)
