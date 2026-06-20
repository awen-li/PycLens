# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b32hexdecode_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [b'abc', b'ABCDEF==', b'==ABCDEF', b'c4======']
    prefixes = [b'M', b'ME', b'MFRA', b'MFRGG', b'MFRGGZA', b'MFRGGZDF']
    for i in range(0, 17):
        if i:
            tests.append(b'=' * i)
        for prefix in prefixes:
            if len(prefix) + i != 8:
                tests.append(prefix + b'=' * i)
    for data in tests:
        with self.subTest(to_decode=data):
            with self.assertRaises(binascii.Error):
                base64.b32hexdecode(data)
            with self.assertRaises(binascii.Error):
                base64.b32hexdecode(data.decode('ascii'))
