# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: RunFuncTestCase_test_run_with_pathlike_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    prog = 'tree.com' if mswindows else 'ls'
    path = shutil.which(prog)
    if path is None:
        self.skipTest(f'{prog} required for this test')
    path = FakePath(path)
    res = subprocess.run(path, stdout=subprocess.DEVNULL)
    self.assertEqual(res.returncode, 0)
    with self.assertRaises(TypeError):
        subprocess.run(path, stdout=subprocess.DEVNULL, shell=True)
