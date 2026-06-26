# Source Generated with Decompyle++
# File: cpython-39-ef483ba7b3aa.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    None ^= <NODE:28>
    encoded_value = value.encode('ascii', 'surrogateescape')
    script = 'import os; print(ascii(os.getenv(%s)))' % repr(key)
    env = os.environ.copy()
    env[key] = value
    env['LC_ALL'] = 'C'
    decoded_value = value
    stdout = subprocess.check_output([
        sys.executable,
        '-c',
        script], env, **('env',))
    stdout = stdout.rstrip(b'\n\r')
    self.assertEqual(stdout.decode('ascii'), ascii(decoded_value))
    key = key.encode('ascii', 'surrogateescape')
    script = 'import os; print(ascii(os.getenvb(%s))(' % repr(key)
    env = os.environ.copy()
    env[key] = encoded_value
    stdout = subprocess.check_output([
        sys.executable,
        '-c',
        script], env, **('env',))
    stdout = stdout.rstrip(b'\n\r')
    self.assertEqual(stdout.decode('ascii'), ascii(encoded_value))
    continue

if __name__ == '__main__':
    __pybcsec_seed__()
