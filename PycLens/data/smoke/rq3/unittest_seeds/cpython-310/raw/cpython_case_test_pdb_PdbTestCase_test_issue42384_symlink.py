# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_issue42384_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = textwrap.dedent("\n            import sys\n            print('sys.path[0] is', sys.path[0])\n        ")
    commands = 'c\nq'
    with os_helper.temp_cwd() as cwd:
        cwd = os.path.realpath(cwd)
        dir_one = os.path.join(cwd, 'dir_one')
        dir_two = os.path.join(cwd, 'dir_two')
        expected = f'(Pdb) sys.path[0] is {dir_one}'
        os.mkdir(dir_one)
        with open(os.path.join(dir_one, 'foo.py'), 'w') as f:
            f.write(script)
        os.mkdir(dir_two)
        os.symlink(os.path.join(dir_one, 'foo.py'), os.path.join(dir_two, 'foo.py'))
        (stdout, stderr) = self._run_pdb([os.path.join('dir_two', 'foo.py')], commands)
        self.assertEqual(stdout.split('\n')[2].rstrip('\r'), expected)
