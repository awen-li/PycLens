# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestNamedTemporaryFile_test_context_manager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tempfile.NamedTemporaryFile() as f:
        self.assertTrue(os.path.exists(f.name))
    self.assertFalse(os.path.exists(f.name))

    def use_closed():
        with f:
            pass
    self.assertRaises(ValueError, use_closed)
