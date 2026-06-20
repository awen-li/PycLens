# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_inplace_encoding_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    temp_file = self.writeTmp(b'Initial text \x88', mode='wb')
    with FileInput(temp_file, inplace=True, encoding='ascii', errors='replace') as fobj:
        line = fobj.readline()
        self.assertEqual(line, 'Initial text �')
        print('New line \x88')
    with open(temp_file, 'rb') as f:
        self.assertEqual(f.read().rstrip(b'\r\n'), b'New line ?')
