# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_readline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb') as f:
        f.write(b'A\nB\r\nC\r')
        f.write(b'123456789\n' * 1000)
        f.write(b'\x80')
    self.addCleanup(safe_unlink, TESTFN)
    with FileInput(files=TESTFN, openhook=hook_encoded('ascii')) as fi:
        try:
            self.assertEqual(fi.readline(), 'A\n')
            self.assertEqual(fi.readline(), 'B\n')
            self.assertEqual(fi.readline(), 'C\n')
        except UnicodeDecodeError:
            self.fail('Read to end of file')
        with self.assertRaises(UnicodeDecodeError):
            list(fi)
        self.assertEqual(fi.readline(), '')
        self.assertEqual(fi.readline(), '')
