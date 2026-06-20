# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: BasicTest_test_prefixes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rmtree(self.env_dir)
    self.run_with_capture(venv.create, self.env_dir)
    envpy = os.path.join(self.env_dir, self.bindir, self.exe)
    cmd = [envpy, '-c', None]
    for (prefix, expected) in (('prefix', self.env_dir), ('exec_prefix', self.env_dir), ('base_prefix', sys.base_prefix), ('base_exec_prefix', sys.base_exec_prefix)):
        cmd[2] = 'import sys; print(sys.%s)' % prefix
        (out, err) = check_output(cmd)
        self.assertEqual(out.strip(), expected.encode())
