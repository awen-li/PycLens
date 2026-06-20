# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_inplace_binary_write_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    temp_file = self.writeTmp(b'Initial text.', mode='wb')
    with FileInput(temp_file, mode='rb', inplace=True) as fobj:
        line = fobj.readline()
        self.assertEqual(line, b'Initial text.')
        sys.stdout.write(b'New line.')
    with open(temp_file, 'rb') as f:
        self.assertEqual(f.read(), b'New line.')
