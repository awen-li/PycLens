# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: Test_hook_encoded_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb') as f:
        f.write(b'\x80abc')
    self.addCleanup(safe_unlink, TESTFN)

    def check(errors, expected_lines):
        with FileInput(files=TESTFN, mode='r', openhook=hook_encoded('utf-8', errors=errors)) as fi:
            lines = list(fi)
        self.assertEqual(lines, expected_lines)
    check('ignore', ['abc'])
    with self.assertRaises(UnicodeDecodeError):
        check('strict', ['abc'])
    check('replace', ['�abc'])
    check('backslashreplace', ['\\x80abc'])
