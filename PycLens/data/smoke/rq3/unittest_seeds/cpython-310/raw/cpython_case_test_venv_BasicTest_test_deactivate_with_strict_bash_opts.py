# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: BasicTest_test_deactivate_with_strict_bash_opts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bash = shutil.which('bash')
    if bash is None:
        self.skipTest('bash required for this test')
    rmtree(self.env_dir)
    builder = venv.EnvBuilder(clear=True)
    builder.create(self.env_dir)
    activate = os.path.join(self.env_dir, self.bindir, 'activate')
    test_script = os.path.join(self.env_dir, 'test_strict.sh')
    with open(test_script, 'w') as f:
        f.write(f'set -euo pipefail\nsource {activate}\ndeactivate\n')
    (out, err) = check_output([bash, test_script])
    self.assertEqual(out, ''.encode())
    self.assertEqual(err, ''.encode())
