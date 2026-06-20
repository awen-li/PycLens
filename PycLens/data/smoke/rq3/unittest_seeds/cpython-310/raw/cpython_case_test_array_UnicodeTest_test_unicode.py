# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: UnicodeTest_test_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, array.array, 'b', 'foo')
    a = array.array('u', '\xa0Âሴ')
    a.fromunicode(' ')
    a.fromunicode('')
    a.fromunicode('')
    a.fromunicode('\x11abcÿሴ')
    s = a.tounicode()
    self.assertEqual(s, '\xa0Âሴ \x11abcÿሴ')
    self.assertEqual(a.itemsize, sizeof_wchar)
    s = '\x00="\'a\\b\x80ÿ\x00\x01ሴ'
    a = array.array('u', s)
    self.assertEqual(repr(a), 'array(\'u\', \'\\x00="\\\'a\\\\b\\x80ÿ\\x00\\x01ሴ\')')
    self.assertRaises(TypeError, a.fromunicode)
