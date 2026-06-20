# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: BasicTest_test_executable_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rmtree(self.env_dir)
    builder = venv.EnvBuilder(clear=True, symlinks=True)
    builder.create(self.env_dir)
    envpy = os.path.join(os.path.realpath(self.env_dir), self.bindir, self.exe)
    (out, err) = check_output([envpy, '-c', 'import sys; print(sys.executable)'])
    self.assertEqual(out.strip(), envpy.encode())
