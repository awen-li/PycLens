# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_readline_binary_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb') as f:
        f.write(b'A\nB\r\nC\rD')
    self.addCleanup(safe_unlink, TESTFN)
    with FileInput(files=TESTFN, mode='rb') as fi:
        self.assertEqual(fi.readline(), b'A\n')
        self.assertEqual(fi.readline(), b'B\r\n')
        self.assertEqual(fi.readline(), b'C\rD')
        self.assertEqual(fi.readline(), b'')
        self.assertEqual(fi.readline(), b'')
