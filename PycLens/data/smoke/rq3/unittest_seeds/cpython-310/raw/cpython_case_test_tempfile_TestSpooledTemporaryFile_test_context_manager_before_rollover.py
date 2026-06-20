# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestSpooledTemporaryFile_test_context_manager_before_rollover

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tempfile.SpooledTemporaryFile(max_size=1) as f:
        self.assertFalse(f._rolled)
        self.assertFalse(f.closed)
    self.assertTrue(f.closed)

    def use_closed():
        with f:
            pass
    self.assertRaises(ValueError, use_closed)
