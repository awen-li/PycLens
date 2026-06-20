# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF7Test_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [(b'\xffb', '�b'), (b'a\xffb', 'a�b'), (b'a\xff\xffb', 'a��b'), (b'a+IK', 'a�'), (b'a+IK-b', 'a�b'), (b'a+IK,b', 'a�b'), (b'a+IKx', 'a€�'), (b'a+IKx-b', 'a€�b'), (b'a+IKwgr', 'a€�'), (b'a+IKwgr-b', 'a€�b'), (b'a+IKwgr,', 'a€�'), (b'a+IKwgr,-b', 'a€�-b'), (b'a+IKwgrB', 'a€€�'), (b'a+IKwgrB-b', 'a€€�b'), (b'a+/,+IKw-b', 'a�€b'), (b'a+//,+IKw-b', 'a�€b'), (b'a+///,+IKw-b', 'a\uffff�€b'), (b'a+////,+IKw-b', 'a\uffff�€b'), (b'a+IKw-b\xff', 'a€b�'), (b'a+IKw\xffb', 'a€�b'), (b'a+@b', 'a�b')]
    for (raw, expected) in tests:
        with self.subTest(raw=raw):
            self.assertRaises(UnicodeDecodeError, codecs.utf_7_decode, raw, 'strict', True)
            self.assertEqual(raw.decode('utf-7', 'replace'), expected)
