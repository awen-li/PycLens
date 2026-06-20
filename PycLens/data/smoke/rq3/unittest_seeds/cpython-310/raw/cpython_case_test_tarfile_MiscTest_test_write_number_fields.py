# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscTest_test_write_number_fields

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(tarfile.itn(1), b'0000001\x00')
    self.assertEqual(tarfile.itn(2097151), b'7777777\x00')
    self.assertEqual(tarfile.itn(2097152, format=tarfile.GNU_FORMAT), b'\x80\x00\x00\x00\x00 \x00\x00')
    self.assertEqual(tarfile.itn(4294967295, format=tarfile.GNU_FORMAT), b'\x80\x00\x00\x00\xff\xff\xff\xff')
    self.assertEqual(tarfile.itn(-1, format=tarfile.GNU_FORMAT), b'\xff\xff\xff\xff\xff\xff\xff\xff')
    self.assertEqual(tarfile.itn(-100, format=tarfile.GNU_FORMAT), b'\xff\xff\xff\xff\xff\xff\xff\x9c')
    self.assertEqual(tarfile.itn(-72057594037927936, format=tarfile.GNU_FORMAT), b'\xff\x00\x00\x00\x00\x00\x00\x00')
    self.assertEqual(tarfile.itn(-100.0, format=tarfile.GNU_FORMAT), b'\xff\xff\xff\xff\xff\xff\xff\x9c')
    self.assertEqual(tarfile.itn(8 ** 12 + 0.0, format=tarfile.GNU_FORMAT), b'\x80\x00\x00\x10\x00\x00\x00\x00')
    self.assertEqual(tarfile.nti(tarfile.itn(-0.1, format=tarfile.GNU_FORMAT)), 0)
