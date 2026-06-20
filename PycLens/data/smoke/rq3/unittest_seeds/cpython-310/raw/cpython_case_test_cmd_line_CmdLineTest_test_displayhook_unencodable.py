# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_displayhook_unencodable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for encoding in ('ascii', 'latin-1', 'utf-8'):
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = encoding
        p = subprocess.Popen([sys.executable, '-i'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)
        text = 'a=é b=\udc80 c=𐀀 d=\U0010ffff'
        p.stdin.write(ascii(text).encode('ascii') + b'\n')
        p.stdin.write(b'exit()\n')
        data = kill_python(p)
        escaped = repr(text).encode(encoding, 'backslashreplace')
        self.assertIn(escaped, data)
