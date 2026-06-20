# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_issue46434

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = '\n            def do_testcmdwithnodocs(self, arg):\n                pass\n\n            import pdb\n            pdb.Pdb.do_testcmdwithnodocs = do_testcmdwithnodocs\n        '
    commands = '\n            continue\n            help testcmdwithnodocs\n        '
    (stdout, stderr) = self.run_pdb_script(script, commands)
    output = (stdout or '') + (stderr or '')
    self.assertNotIn('AttributeError', output, 'Calling help on a command with no docs should be handled gracefully')
    self.assertIn("*** No help for 'testcmdwithnodocs'; __doc__ string missing", output, 'Calling help on a command with no docs should print an error')
