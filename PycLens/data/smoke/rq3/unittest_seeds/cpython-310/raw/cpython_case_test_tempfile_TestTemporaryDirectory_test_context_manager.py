# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryDirectory_test_context_manager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = self.do_create()
    with d as name:
        self.assertTrue(os.path.exists(name))
        self.assertEqual(name, d.name)
    self.assertFalse(os.path.exists(name))
