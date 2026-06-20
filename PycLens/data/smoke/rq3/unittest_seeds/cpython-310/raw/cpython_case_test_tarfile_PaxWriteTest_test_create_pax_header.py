# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: PaxWriteTest_test_create_pax_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = tarfile.TarInfo()
    t.name = 'foo'
    t.mtime = 1000.1
    t.size = 100
    t.uid = 123
    t.gid = 124
    info = t.get_info()
    header = t.create_pax_header(info, encoding='iso8859-1')
    self.assertEqual(info['name'], 'foo')
    self.assertIsInstance(info['mtime'], int)
    self.assertEqual(info['mtime'], 1000)
    self.assertEqual(info['size'], 100)
    self.assertEqual(info['uid'], 123)
    self.assertEqual(info['gid'], 124)
    self.assertEqual(header, b'././@PaxHeader' + bytes(86) + b'0000000\x000000000\x000000000\x0000000000020\x0000000000000\x00010205\x00 x' + bytes(100) + b'ustar\x0000' + bytes(247) + b'16 mtime=1000.1\n' + bytes(496) + b'foo' + bytes(97) + b'0000644\x000000173\x000000174\x0000000000144\x0000000001750\x00006516\x00 0' + bytes(100) + b'ustar\x0000' + bytes(247))
    t = tarfile.TarInfo()
    t.name = 'foo㍴'
    t.mtime = 10 ** 10
    t.size = 10 ** 10
    t.uid = 8 ** 8
    t.gid = 8 ** 8 + 1
    info = t.get_info()
    header = t.create_pax_header(info, encoding='iso8859-1')
    self.assertEqual(info['name'], 'foo㍴')
    self.assertEqual(info['mtime'], 0)
    self.assertEqual(info['size'], 0)
    self.assertEqual(info['uid'], 0)
    self.assertEqual(info['gid'], 0)
    self.assertEqual(header, b'././@PaxHeader' + bytes(86) + b'0000000\x000000000\x000000000\x0000000000130\x0000000000000\x00010207\x00 x' + bytes(100) + b'ustar\x0000' + bytes(247) + b'15 path=foo\xe3\x8d\xb4\n16 uid=16777216\n' + b'16 gid=16777217\n20 size=10000000000\n' + b'21 mtime=10000000000\n' + bytes(424) + b'foo?' + bytes(96) + b'0000644\x000000000\x000000000\x0000000000000\x0000000000000\x00006540\x00 0' + bytes(100) + b'ustar\x0000' + bytes(247))
