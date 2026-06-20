# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_osx_android_utf8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'e:é, euro:€, non-bmp:\U0010ffff'.encode('utf-8')
    code = 'import sys; print(ascii(sys.argv[1]))'
    decoded = text.decode('utf-8', 'surrogateescape')
    expected = ascii(decoded).encode('ascii') + b'\n'
    env = os.environ.copy()
    env['LC_ALL'] = 'C'
    p = subprocess.Popen((sys.executable, '-c', code, text), stdout=subprocess.PIPE, env=env)
    (stdout, stderr) = p.communicate()
    self.assertEqual(stdout, expected)
    self.assertEqual(p.returncode, 0)
