# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_stdin_binary_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch('sys.stdin') as m_stdin:
        m_stdin.buffer = BytesIO(b'spam, bacon, sausage, and spam')
        fi = FileInput(files=['-'], mode='rb')
        lines = list(fi)
        self.assertEqual(lines, [b'spam, bacon, sausage, and spam'])
