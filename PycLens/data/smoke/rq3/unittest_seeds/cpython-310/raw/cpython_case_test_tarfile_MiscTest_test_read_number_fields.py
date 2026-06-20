# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscTest_test_read_number_fields

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(tarfile.nti(b'0000001\x00'), 1)
    self.assertEqual(tarfile.nti(b'7777777\x00'), 2097151)
    self.assertEqual(tarfile.nti(b'\x80\x00\x00\x00\x00 \x00\x00'), 2097152)
    self.assertEqual(tarfile.nti(b'\x80\x00\x00\x00\xff\xff\xff\xff'), 4294967295)
    self.assertEqual(tarfile.nti(b'\xff\xff\xff\xff\xff\xff\xff\xff'), -1)
    self.assertEqual(tarfile.nti(b'\xff\xff\xff\xff\xff\xff\xff\x9c'), -100)
    self.assertEqual(tarfile.nti(b'\xff\x00\x00\x00\x00\x00\x00\x00'), -72057594037927936)
    self.assertEqual(tarfile.nti(b'\x00'), 0)
    self.assertEqual(tarfile.nti(b'       \x00'), 0)
