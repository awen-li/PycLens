# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_run_pdb_with_pdb

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    commands = '\n            c\n            quit\n        '
    (stdout, stderr) = self._run_pdb(['-m', 'pdb'], commands)
    self.assertIn(pdb._usage, stdout.replace('\r', ''))
