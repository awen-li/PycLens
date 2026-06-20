# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_invalid_utf8_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import sys, os; s=os.fsencode(sys.argv[1]); print(ascii(s))'
    base_cmd = [sys.executable, '-c', code]

    def run_default(arg):
        cmd = [sys.executable, '-c', code, arg]
        return subprocess.run(cmd, stdout=subprocess.PIPE, text=True)

    def run_c_locale(arg):
        cmd = [sys.executable, '-c', code, arg]
        env = dict(os.environ)
        env['LC_ALL'] = 'C'
        return subprocess.run(cmd, stdout=subprocess.PIPE, text=True, env=env)

    def run_utf8_mode(arg):
        cmd = [sys.executable, '-X', 'utf8', '-c', code, arg]
        return subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    valid_utf8 = 'e:é, euro:€, non-bmp:\U0010ffff'.encode('utf-8')
    invalid_utf8 = b'\xff\xc3\xff\xc3\xa9\xed\xa0\x80\xfd\xbf\xbf\xbb\xba\xba'
    test_args = [valid_utf8, invalid_utf8]
    for run_cmd in (run_default, run_c_locale, run_utf8_mode):
        with self.subTest(run_cmd=run_cmd):
            for arg in test_args:
                proc = run_cmd(arg)
                self.assertEqual(proc.stdout.rstrip(), ascii(arg))
