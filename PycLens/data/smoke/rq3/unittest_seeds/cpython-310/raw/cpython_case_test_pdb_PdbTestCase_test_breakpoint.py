# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_breakpoint

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = '\n            if __name__ == \'__main__\':\n                pass\n                print("SUCCESS")\n                pass\n        '
    commands = '\n            b 3\n            quit\n        '
    (stdout, stderr) = self.run_pdb_module(script, commands)
    self.assertTrue(any(('Breakpoint 1 at' in l for l in stdout.splitlines())), stdout)
    self.assertTrue(all(('SUCCESS' not in l for l in stdout.splitlines())), stdout)
