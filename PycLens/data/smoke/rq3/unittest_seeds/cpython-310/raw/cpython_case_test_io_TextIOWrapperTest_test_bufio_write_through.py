# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_bufio_write_through

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (flush_called, write_called) = ([], [])

    class BufferedWriter(self.BufferedWriter):

        def flush(self, *args, **kwargs):
            flush_called.append(True)
            return super().flush(*args, **kwargs)

        def write(self, *args, **kwargs):
            write_called.append(True)
            return super().write(*args, **kwargs)
    rawio = self.BytesIO()
    data = b'a'
    bufio = BufferedWriter(rawio, len(data) * 2)
    textio = self.TextIOWrapper(bufio, encoding='ascii', write_through=True)
    text = data.decode('ascii')
    textio.write(text)
    self.assertFalse(flush_called)
    self.assertTrue(write_called)
    self.assertEqual(rawio.getvalue(), b'')
    write_called = []
    textio.write(text * 10)
    self.assertTrue(write_called)
    self.assertEqual(rawio.getvalue(), data * 11)
