# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_spwd.py
# case: TestSpwdRoot_test_getspall

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    entries = spwd.getspall()
    self.assertIsInstance(entries, list)
    for entry in entries:
        self.assertIsInstance(entry, spwd.struct_spwd)
