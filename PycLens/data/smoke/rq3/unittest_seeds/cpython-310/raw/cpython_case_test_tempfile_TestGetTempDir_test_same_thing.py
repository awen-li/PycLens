# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestGetTempDir_test_same_thing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = tempfile.gettempdir()
    b = tempfile.gettempdir()
    c = tempfile.gettempdirb()
    self.assertTrue(a is b)
    self.assertNotEqual(type(a), type(c))
    self.assertEqual(a, os.fsdecode(c))
