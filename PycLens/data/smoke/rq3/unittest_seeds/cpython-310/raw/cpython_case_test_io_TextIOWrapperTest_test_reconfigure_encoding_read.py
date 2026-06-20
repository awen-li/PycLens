# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_reconfigure_encoding_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = 'abcé\n'.encode('latin1') + 'déf\n'.encode('utf8')
    raw = self.BytesIO(data)
    txt = self.TextIOWrapper(raw, encoding='latin1', newline='\n')
    self.assertEqual(txt.readline(), 'abcé\n')
    with self.assertRaises(self.UnsupportedOperation):
        txt.reconfigure(encoding='utf-8')
    with self.assertRaises(self.UnsupportedOperation):
        txt.reconfigure(newline=None)
