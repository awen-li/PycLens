# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: BasicTest_test_macos_env

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rmtree(self.env_dir)
    builder = venv.EnvBuilder()
    builder.create(self.env_dir)
    envpy = os.path.join(os.path.realpath(self.env_dir), self.bindir, self.exe)
    (out, err) = check_output([envpy, '-c', 'import os; print("__PYVENV_LAUNCHER__" in os.environ)'])
    self.assertEqual(out.strip(), 'False'.encode())
