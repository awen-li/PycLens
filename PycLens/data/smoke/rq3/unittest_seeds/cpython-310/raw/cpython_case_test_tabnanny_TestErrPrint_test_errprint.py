# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestErrPrint_test_errprint

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [(['first', 'second'], 'first second\n'), (['first'], 'first\n'), ([1, 2, 3], '1 2 3\n'), ([], '\n')]
    for (args, expected) in tests:
        with self.subTest(arguments=args, expected=expected):
            with captured_stderr() as stderr:
                tabnanny.errprint(*args)
            self.assertEqual(stderr.getvalue(), expected)
