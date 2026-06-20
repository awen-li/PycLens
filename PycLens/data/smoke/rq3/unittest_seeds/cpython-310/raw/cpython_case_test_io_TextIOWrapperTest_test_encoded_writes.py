# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_encoded_writes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = '1234567890'
    tests = ('utf-16', 'utf-16-le', 'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-be')
    for encoding in tests:
        buf = self.BytesIO()
        f = self.TextIOWrapper(buf, encoding=encoding)
        f.write(data)
        f.write(data)
        f.seek(0)
        self.assertEqual(f.read(), data * 2)
        f.seek(0)
        self.assertEqual(f.read(), data * 2)
        self.assertEqual(buf.getvalue(), (data * 2).encode(encoding))
