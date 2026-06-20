# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_newlines_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    testdata = b'AAA\nBB\x00B\nCCC\rDDD\rEEE\r\nFFF\r\nGGG'
    normalized = testdata.replace(b'\r\n', b'\n').replace(b'\r', b'\n')
    for (newline, expected) in [(None, normalized.decode('ascii').splitlines(keepends=True)), ('', testdata.decode('ascii').splitlines(keepends=True)), ('\n', ['AAA\n', 'BB\x00B\n', 'CCC\rDDD\rEEE\r\n', 'FFF\r\n', 'GGG']), ('\r\n', ['AAA\nBB\x00B\nCCC\rDDD\rEEE\r\n', 'FFF\r\n', 'GGG']), ('\r', ['AAA\nBB\x00B\nCCC\r', 'DDD\r', 'EEE\r', '\nFFF\r', '\nGGG'])]:
        buf = self.BytesIO(testdata)
        txt = self.TextIOWrapper(buf, encoding='ascii', newline=newline)
        self.assertEqual(txt.readlines(), expected)
        txt.seek(0)
        self.assertEqual(txt.read(), ''.join(expected))
