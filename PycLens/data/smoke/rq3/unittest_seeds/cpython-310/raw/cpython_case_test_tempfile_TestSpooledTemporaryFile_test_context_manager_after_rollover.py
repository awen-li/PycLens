# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestSpooledTemporaryFile_test_context_manager_after_rollover

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = tempfile.SpooledTemporaryFile(max_size=1)
    f.write(b'abc\n')
    f.flush()
    self.assertTrue(f._rolled)
    with f:
        self.assertFalse(f.closed)
    self.assertTrue(f.closed)

    def use_closed():
        with f:
            pass
    self.assertRaises(ValueError, use_closed)
