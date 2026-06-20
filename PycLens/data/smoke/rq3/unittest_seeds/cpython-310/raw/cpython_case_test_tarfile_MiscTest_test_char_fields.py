# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscTest_test_char_fields

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(tarfile.stn('foo', 8, 'ascii', 'strict'), b'foo\x00\x00\x00\x00\x00')
    self.assertEqual(tarfile.stn('foobar', 3, 'ascii', 'strict'), b'foo')
    self.assertEqual(tarfile.nts(b'foo\x00\x00\x00\x00\x00', 'ascii', 'strict'), 'foo')
    self.assertEqual(tarfile.nts(b'foo\x00bar\x00', 'ascii', 'strict'), 'foo')
