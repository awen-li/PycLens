# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HeaderTests_test_invalid_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    conn = client.HTTPConnection('example.com')
    conn.sock = FakeSocket('')
    conn.putrequest('GET', '/')
    cases = ((b'Invalid\r\nName', b'ValidValue'), (b'Invalid\rName', b'ValidValue'), (b'Invalid\nName', b'ValidValue'), (b'\r\nInvalidName', b'ValidValue'), (b'\rInvalidName', b'ValidValue'), (b'\nInvalidName', b'ValidValue'), (b' InvalidName', b'ValidValue'), (b'\tInvalidName', b'ValidValue'), (b'Invalid:Name', b'ValidValue'), (b':InvalidName', b'ValidValue'), (b'ValidName', b'Invalid\r\nValue'), (b'ValidName', b'Invalid\rValue'), (b'ValidName', b'Invalid\nValue'), (b'ValidName', b'InvalidValue\r\n'), (b'ValidName', b'InvalidValue\r'), (b'ValidName', b'InvalidValue\n'))
    for (name, value) in cases:
        with self.subTest((name, value)):
            with self.assertRaisesRegex(ValueError, 'Invalid header'):
                conn.putheader(name, value)
