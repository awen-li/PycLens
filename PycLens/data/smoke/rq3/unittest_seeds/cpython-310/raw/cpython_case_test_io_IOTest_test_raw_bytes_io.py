# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_raw_bytes_io

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.BytesIO()
    self.write_ops(f)
    data = f.getvalue()
    self.assertEqual(data, b'hello world\n')
    f = self.BytesIO(data)
    self.read_ops(f, True)
