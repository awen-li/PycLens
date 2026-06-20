# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: Test_hook_encoded_test_modes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb') as f:
        f.write(b'A\nB\r\nC\rD+IKw-')
    self.addCleanup(safe_unlink, TESTFN)

    def check(mode, expected_lines):
        with FileInput(files=TESTFN, mode=mode, openhook=hook_encoded('utf-7')) as fi:
            lines = list(fi)
        self.assertEqual(lines, expected_lines)
    check('r', ['A\n', 'B\n', 'C\n', 'D€'])
    with self.assertWarns(DeprecationWarning):
        check('rU', ['A\n', 'B\n', 'C\n', 'D€'])
    with self.assertWarns(DeprecationWarning):
        check('U', ['A\n', 'B\n', 'C\n', 'D€'])
    with self.assertRaises(ValueError):
        check('rb', ['A\n', 'B\r\n', 'C\r', 'D€'])
