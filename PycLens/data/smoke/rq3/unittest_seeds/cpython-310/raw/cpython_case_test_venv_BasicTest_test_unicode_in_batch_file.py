# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: BasicTest_test_unicode_in_batch_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rmtree(self.env_dir)
    env_dir = os.path.join(os.path.realpath(self.env_dir), 'ϼўТλФЙ')
    builder = venv.EnvBuilder(clear=True)
    builder.create(env_dir)
    activate = os.path.join(env_dir, self.bindir, 'activate.bat')
    envpy = os.path.join(env_dir, self.bindir, self.exe)
    (out, err) = check_output([activate, '&', self.exe, '-c', 'print(0)'], encoding='oem')
    self.assertEqual(out.strip(), '0')
