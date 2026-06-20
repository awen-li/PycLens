# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: UnpackIteratorTest_test_construct

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _check_iterator(it):
        self.assertIsInstance(it, abc.Iterator)
        self.assertIsInstance(it, abc.Iterable)
    s = struct.Struct('>ibcp')
    it = s.iter_unpack(b'')
    _check_iterator(it)
    it = s.iter_unpack(b'1234567')
    _check_iterator(it)
    with self.assertRaises(struct.error):
        s.iter_unpack(b'123456')
    with self.assertRaises(struct.error):
        s.iter_unpack(b'12345678')
    s = struct.Struct('>')
    with self.assertRaises(struct.error):
        s.iter_unpack(b'')
    with self.assertRaises(struct.error):
        s.iter_unpack(b'12')
