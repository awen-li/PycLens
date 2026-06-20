# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_write_non_blocking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.MockNonBlockWriterIO()
    bufio = self.tp(raw, 8)
    self.assertEqual(bufio.write(b'abcd'), 4)
    self.assertEqual(bufio.write(b'efghi'), 5)
    raw.block_on(b'k')
    self.assertEqual(bufio.write(b'jklmn'), 5)
    raw.block_on(b'0')
    try:
        bufio.write(b'opqrwxyz0123456789')
    except self.BlockingIOError as e:
        written = e.characters_written
    else:
        self.fail('BlockingIOError should have been raised')
    self.assertEqual(written, 16)
    self.assertEqual(raw.pop_written(), b'abcdefghijklmnopqrwxyz')
    self.assertEqual(bufio.write(b'ABCDEFGHI'), 9)
    s = raw.pop_written()
    self.assertTrue(s.startswith(b'01234567A'), s)
