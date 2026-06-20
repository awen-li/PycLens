# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_run_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = 'print("SUCCESS")'
    commands = '\n            continue\n            quit\n        '
    (stdout, stderr) = self.run_pdb_module(script, commands)
    self.assertTrue(any(('SUCCESS' in l for l in stdout.splitlines())), stdout)
