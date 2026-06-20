# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: ChecklineTests_test_checkline_is_not_executable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = textwrap.dedent('\n            # Comment\n            """ docstring """\n            \'\'\' docstring \'\'\'\n\n        ')
    with open(os_helper.TESTFN, 'w') as f:
        f.write(s)
    num_lines = len(s.splitlines()) + 2
    with redirect_stdout(StringIO()):
        db = pdb.Pdb()
        for lineno in range(num_lines):
            self.assertFalse(db.checkline(os_helper.TESTFN, lineno))
