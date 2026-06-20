# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_issue42384

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = textwrap.dedent("\n            import sys\n            print('sys.path[0] is', sys.path[0])\n        ")
    commands = 'c\nq'
    with os_helper.temp_cwd() as cwd:
        expected = f'(Pdb) sys.path[0] is {os.path.realpath(cwd)}'
        (stdout, stderr) = self.run_pdb_script(script, commands)
        self.assertEqual(stdout.split('\n')[2].rstrip('\r'), expected)
