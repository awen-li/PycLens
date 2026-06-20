# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_isolatedmode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.verify_valid_flag('-I')
    self.verify_valid_flag('-IEs')
    (rc, out, err) = assert_python_ok('-I', '-c', 'from sys import flags as f; print(f.no_user_site, f.ignore_environment, f.isolated)', dummyvar='')
    self.assertEqual(out.strip(), b'1 1 1')
    with os_helper.temp_cwd() as tmpdir:
        fake = os.path.join(tmpdir, 'uuid.py')
        main = os.path.join(tmpdir, 'main.py')
        with open(fake, 'w', encoding='utf-8') as f:
            f.write("raise RuntimeError('isolated mode test')\n")
        with open(main, 'w', encoding='utf-8') as f:
            f.write('import uuid\n')
            f.write("print('ok')\n")
        self.assertRaises(subprocess.CalledProcessError, subprocess.check_output, [sys.executable, main], cwd=tmpdir, stderr=subprocess.DEVNULL)
        out = subprocess.check_output([sys.executable, '-I', main], cwd=tmpdir)
        self.assertEqual(out.strip(), b'ok')
