# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestGetTempPrefix_test_sane_template

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = tempfile.gettempprefix()
    self.assertIsInstance(p, str)
    self.assertGreater(len(p), 0)
    pb = tempfile.gettempprefixb()
    self.assertIsInstance(pb, bytes)
    self.assertGreater(len(pb), 0)
