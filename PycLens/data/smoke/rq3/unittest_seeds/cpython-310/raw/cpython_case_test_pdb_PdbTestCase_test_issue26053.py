# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_issue26053

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = "print('hello')"
    commands = '\n            continue\n            run a b c\n            run d e f\n            quit\n        '
    (stdout, stderr) = self.run_pdb_script(script, commands)
    res = '\n'.join([x.strip() for x in stdout.splitlines()])
    self.assertRegex(res, 'Restarting .* with arguments:\na b c')
    self.assertRegex(res, 'Restarting .* with arguments:\nd e f')
