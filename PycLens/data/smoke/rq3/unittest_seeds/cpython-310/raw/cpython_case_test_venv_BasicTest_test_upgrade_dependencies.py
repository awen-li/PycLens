# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: BasicTest_test_upgrade_dependencies

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    builder = venv.EnvBuilder()
    bin_path = 'Scripts' if sys.platform == 'win32' else 'bin'
    python_exe = os.path.split(sys.executable)[1]
    with tempfile.TemporaryDirectory() as fake_env_dir:
        expect_exe = os.path.normcase(os.path.join(fake_env_dir, bin_path, python_exe))
        if sys.platform == 'win32':
            expect_exe = os.path.normcase(os.path.realpath(expect_exe))

        def pip_cmd_checker(cmd, **kwargs):
            cmd[0] = os.path.normcase(cmd[0])
            self.assertEqual(cmd, [expect_exe, '-m', 'pip', 'install', '--upgrade', 'pip', 'setuptools'])
        fake_context = builder.ensure_directories(fake_env_dir)
        with patch('venv.subprocess.check_output', pip_cmd_checker):
            builder.upgrade_dependencies(fake_context)
