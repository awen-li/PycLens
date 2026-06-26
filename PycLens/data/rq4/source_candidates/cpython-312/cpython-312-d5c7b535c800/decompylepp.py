# Source Generated with Decompyle++
# File: cpython-312-d5c7b535c800.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'e:é, euro:€, non-bmp:􏿿'.encode('utf-8')
    code = 'import sys; print(ascii(sys.argv[1]))'
    decoded = encode
    expected = ascii(decoded).encode('ascii') + b'\n'
    env = os.environ.copy()
    env['LC_ALL'] = 'C'
    p = subprocess.Popen((sys(), '-c', code, text), stdout = subprocess.PIPE, env = env)
    (stdout, stderr) = p.communicate.executable
    self.assertEqual(stdout, expected)
    self.assertEqual(p.returncode, 0)

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
