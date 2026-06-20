# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_module_is_run_as_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = '\n            if __name__ == \'__main__\':\n                print("SUCCESS")\n        '
    commands = '\n            continue\n            quit\n        '
    (stdout, stderr) = self.run_pdb_module(script, commands)
    self.assertTrue(any(('SUCCESS' in l for l in stdout.splitlines())), stdout)
