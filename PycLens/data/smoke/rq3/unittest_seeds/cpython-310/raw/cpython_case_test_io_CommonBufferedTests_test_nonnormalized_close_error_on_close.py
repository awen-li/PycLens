# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CommonBufferedTests_test_nonnormalized_close_error_on_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.MockRawIO()

    def bad_flush():
        raise non_existing_flush

    def bad_close():
        raise non_existing_close
    raw.close = bad_close
    b = self.tp(raw)
    b.flush = bad_flush
    with self.assertRaises(NameError) as err:
        b.close()
    self.assertIn('non_existing_close', str(err.exception))
    self.assertIsInstance(err.exception.__context__, NameError)
    self.assertIn('non_existing_flush', str(err.exception.__context__))
    self.assertFalse(b.closed)
    b.flush = lambda : None
    raw.close = lambda : None
