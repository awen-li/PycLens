# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_undecodable_env

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (key, value) in (('test', 'abc\udcff'), ('test\udcff', '42')):
        encoded_value = value.encode('ascii', 'surrogateescape')
        script = 'import os; print(ascii(os.getenv(%s)))' % repr(key)
        env = os.environ.copy()
        env[key] = value
        env['LC_ALL'] = 'C'
        decoded_value = value
        stdout = subprocess.check_output([sys.executable, '-c', script], env=env)
        stdout = stdout.rstrip(b'\n\r')
        self.assertEqual(stdout.decode('ascii'), ascii(decoded_value))
        key = key.encode('ascii', 'surrogateescape')
        script = 'import os; print(ascii(os.getenvb(%s)))' % repr(key)
        env = os.environ.copy()
        env[key] = encoded_value
        stdout = subprocess.check_output([sys.executable, '-c', script], env=env)
        stdout = stdout.rstrip(b'\n\r')
        self.assertEqual(stdout.decode('ascii'), ascii(encoded_value))
