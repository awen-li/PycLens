# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: MiscIOTest_test_check_encoding_warning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mod = self.io.__name__
    filename = __file__
    code = textwrap.dedent(f'            import sys\n            from {mod} import open, TextIOWrapper\n            import pathlib\n\n            with open({filename!r}) as f:           # line 5\n                pass\n\n            pathlib.Path({filename!r}).read_text()  # line 8\n        ')
    proc = assert_python_ok('-X', 'warn_default_encoding', '-c', code)
    warnings = proc.err.splitlines()
    self.assertEqual(len(warnings), 2)
    self.assertTrue(warnings[0].startswith(b'<string>:5: EncodingWarning: '))
    self.assertTrue(warnings[1].startswith(b'<string>:8: EncodingWarning: '))
