# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_issue42383

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_cwd() as cwd:
        with open('foo.py', 'w') as f:
            s = textwrap.dedent('\n                    print(\'The correct file was executed\')\n\n                    import os\n                    os.chdir("subdir")\n                ')
            f.write(s)
        subdir = os.path.join(cwd, 'subdir')
        os.mkdir(subdir)
        os.mkdir(os.path.join(subdir, 'subdir'))
        wrong_file = os.path.join(subdir, 'foo.py')
        with open(wrong_file, 'w') as f:
            f.write('print("The wrong file was executed")')
        (stdout, stderr) = self._run_pdb(['foo.py'], 'c\nc\nq')
        expected = '(Pdb) The correct file was executed'
        self.assertEqual(stdout.split('\n')[6].rstrip('\r'), expected)
