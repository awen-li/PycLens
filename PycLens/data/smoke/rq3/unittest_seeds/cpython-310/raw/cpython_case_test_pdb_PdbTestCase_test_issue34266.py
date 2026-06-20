# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_issue34266

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(bad_arg, msg):
        commands = '\n'.join([f'run {bad_arg}', 'q'])
        (stdout, _) = self.run_pdb_script('pass', commands + '\n')
        self.assertEqual(stdout.splitlines()[1:], ['-> pass', f'(Pdb) *** Cannot run {bad_arg}: {msg}', '(Pdb) '])
    check('\\', 'No escaped character')
    check('"', 'No closing quotation')
