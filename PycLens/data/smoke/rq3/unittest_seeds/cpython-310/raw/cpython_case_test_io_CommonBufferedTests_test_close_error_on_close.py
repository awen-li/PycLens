# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CommonBufferedTests_test_close_error_on_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.MockRawIO()

    def bad_flush():
        raise OSError('flush')

    def bad_close():
        raise OSError('close')
    raw.close = bad_close
    b = self.tp(raw)
    b.flush = bad_flush
    with self.assertRaises(OSError) as err:
        b.close()
    self.assertEqual(err.exception.args, ('close',))
    self.assertIsInstance(err.exception.__context__, OSError)
    self.assertEqual(err.exception.__context__.args, ('flush',))
    self.assertFalse(b.closed)
    raw.close = lambda : None
    b.flush = lambda : None
