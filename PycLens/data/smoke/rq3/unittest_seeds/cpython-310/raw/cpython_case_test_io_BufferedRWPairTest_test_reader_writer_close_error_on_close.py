# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRWPairTest_test_reader_writer_close_error_on_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def reader_close():
        reader_non_existing

    def writer_close():
        writer_non_existing
    reader = self.MockRawIO()
    reader.close = reader_close
    writer = self.MockRawIO()
    writer.close = writer_close
    pair = self.tp(reader, writer)
    with self.assertRaises(NameError) as err:
        pair.close()
    self.assertIn('reader_non_existing', str(err.exception))
    self.assertIsInstance(err.exception.__context__, NameError)
    self.assertIn('writer_non_existing', str(err.exception.__context__))
    self.assertFalse(pair.closed)
    self.assertFalse(reader.closed)
    self.assertFalse(writer.closed)
    reader.close = lambda : None
    writer.close = lambda : None
