# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_errors_in_command

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    commands = '\n'.join(['print(', 'debug print(', 'debug doesnotexist', 'c'])
    (stdout, _) = self.run_pdb_script('pass', commands + '\n')
    self.assertEqual(stdout.splitlines()[1:], ['-> pass', "(Pdb) *** SyntaxError: '(' was never closed", '(Pdb) ENTERING RECURSIVE DEBUGGER', "*** SyntaxError: '(' was never closed", 'LEAVING RECURSIVE DEBUGGER', '(Pdb) ENTERING RECURSIVE DEBUGGER', '> <string>(1)<module>()', "((Pdb)) *** NameError: name 'doesnotexist' is not defined", 'LEAVING RECURSIVE DEBUGGER', '(Pdb) '])
