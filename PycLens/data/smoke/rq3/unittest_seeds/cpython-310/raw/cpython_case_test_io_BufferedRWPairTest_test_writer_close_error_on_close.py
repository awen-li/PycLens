# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRWPairTest_test_writer_close_error_on_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def writer_close():
        writer_non_existing
    reader = self.MockRawIO()
    writer = self.MockRawIO()
    writer.close = writer_close
    pair = self.tp(reader, writer)
    with self.assertRaises(NameError) as err:
        pair.close()
    self.assertIn('writer_non_existing', str(err.exception))
    self.assertFalse(pair.closed)
    self.assertTrue(reader.closed)
    self.assertFalse(writer.closed)
    writer.close = lambda : None
    writer = None
    with support.catch_unraisable_exception():
        with support.catch_unraisable_exception():
            pair = None
            support.gc_collect()
        support.gc_collect()
