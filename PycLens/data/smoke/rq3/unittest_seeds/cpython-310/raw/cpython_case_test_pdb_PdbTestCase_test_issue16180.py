# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_issue16180

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = 'def f: pass\n'
    commands = ''
    expected = 'SyntaxError:'
    (stdout, stderr) = self.run_pdb_script(script, commands)
    self.assertIn(expected, stdout, '\n\nExpected:\n{}\nGot:\n{}\nFail to handle a syntax error in the debuggee.'.format(expected, stdout))
