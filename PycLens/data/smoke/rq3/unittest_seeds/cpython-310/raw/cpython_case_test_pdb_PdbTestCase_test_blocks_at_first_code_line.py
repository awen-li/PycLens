# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_blocks_at_first_code_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = '\n                #This is a comment, on line 2\n\n                print("SUCCESS")\n        '
    commands = '\n            quit\n        '
    (stdout, stderr) = self.run_pdb_module(script, commands)
    self.assertTrue(any(('__main__.py(4)<module>()' in l for l in stdout.splitlines())), stdout)
