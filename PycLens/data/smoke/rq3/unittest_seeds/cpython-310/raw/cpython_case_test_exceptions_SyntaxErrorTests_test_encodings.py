# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: SyntaxErrorTests_test_encodings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = '# -*- coding: cp437 -*-\n"┬ó┬ó┬ó┬ó┬ó┬ó" + f(4, x for x in range(1))\n'
    try:
        with open(TESTFN, 'w', encoding='cp437') as testfile:
            testfile.write(source)
        (rc, out, err) = script_helper.assert_python_failure('-Wd', '-X', 'utf8', TESTFN)
        err = err.decode('utf-8').splitlines()
        self.assertEqual(err[-3], '    "┬ó┬ó┬ó┬ó┬ó┬ó" + f(4, x for x in range(1))')
        self.assertEqual(err[-2], '                          ^^^^^^^^^^^^^^^^^^^')
    finally:
        unlink(TESTFN)
    source = '# -*- coding: ascii -*-\n\n(\n'
    try:
        with open(TESTFN, 'w', encoding='ascii') as testfile:
            testfile.write(source)
        (rc, out, err) = script_helper.assert_python_failure('-Wd', '-X', 'utf8', TESTFN)
        err = err.decode('utf-8').splitlines()
        self.assertEqual(err[-3], '    (')
        self.assertEqual(err[-2], '    ^')
    finally:
        unlink(TESTFN)
