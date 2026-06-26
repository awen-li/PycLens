# Source Generated with Decompyle++
# File: cpython-311-5759b93de53b.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    testdata = b'AAA\nBB\x00B\nCCC\rDDD\rEEE\r\nFFF\r\nGGG'
    normalized = testdata.replace(b'\r\n', b'\n').replace(b'\r', b'\n')
    for newline, expected in ((None, None(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, normalized.decode, 'ascii').splitlines(keepends = True)), ('', testdata.decode('ascii').splitlines(keepends = True)), ('\n', [
        'AAA\n',
        'BB\x00B\n',
        'CCC\rDDD\rEEE\r\n',
        'FFF\r\n',
        'GGG']), ('\r\n', [
        'AAA\nBB\x00B\nCCC\rDDD\rEEE\r\n',
        'FFF\r\n',
        'GGG']), ('\r', [
        'AAA\nBB\x00B\nCCC\r',
        'DDD\r',
        'EEE\r',
        '\nFFF\r',
        '\nGGG'])):
        buf = self.BytesIO(testdata)
        self.TextIOWrapper
        txt = None(buf, encoding = 'ascii', newline = newline)
        txt.readlines
        None(self.assertEqual(), expected)
        txt.seek(0)
        self.assertEqual(txt.read(), ''.join(expected))

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
