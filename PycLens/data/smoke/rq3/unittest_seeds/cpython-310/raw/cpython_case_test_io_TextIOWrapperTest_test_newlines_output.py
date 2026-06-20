# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_newlines_output

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    testdict = {'': b'AAA\nBBB\nCCC\nX\rY\r\nZ', '\n': b'AAA\nBBB\nCCC\nX\rY\r\nZ', '\r': b'AAA\rBBB\rCCC\rX\rY\r\rZ', '\r\n': b'AAA\r\nBBB\r\nCCC\r\nX\rY\r\r\nZ'}
    tests = [(None, testdict[os.linesep])] + sorted(testdict.items())
    for (newline, expected) in tests:
        buf = self.BytesIO()
        txt = self.TextIOWrapper(buf, encoding='ascii', newline=newline)
        txt.write('AAA\nB')
        txt.write('BB\nCCC\n')
        txt.write('X\rY\r\nZ')
        txt.flush()
        self.assertEqual(buf.closed, False)
        self.assertEqual(buf.getvalue(), expected)
