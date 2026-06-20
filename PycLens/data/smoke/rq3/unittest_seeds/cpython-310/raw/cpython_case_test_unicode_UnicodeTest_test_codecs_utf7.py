# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_codecs_utf7

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    utfTests = [('A≢Α.', b'A+ImIDkQ.'), ('Hi Mom -☺-!', b'Hi Mom -+Jjo--!'), ('日本語', b'+ZeVnLIqe-'), ('Item 3 is £1.', b'Item 3 is +AKM-1.'), ('+', b'+-'), ('+-', b'+--'), ('+?', b'+-?'), ('\\?', b'+AFw?'), ('+?', b'+-?'), ('\\\\?', b'+AFwAXA?'), ('\\\\\\?', b'+AFwAXABc?'), ('++--', b'+-+---'), ('\U000abcde', b'+2m/c3g-'), ('/', b'/')]
    for (x, y) in utfTests:
        self.assertEqual(x.encode('utf-7'), y)
    self.assertEqual('\ud801'.encode('utf-7'), b'+2AE-')
    self.assertEqual('\ud801x'.encode('utf-7'), b'+2AE-x')
    self.assertEqual('\udc01'.encode('utf-7'), b'+3AE-')
    self.assertEqual('\udc01x'.encode('utf-7'), b'+3AE-x')
    self.assertEqual(b'+2AE-'.decode('utf-7'), '\ud801')
    self.assertEqual(b'+2AE-x'.decode('utf-7'), '\ud801x')
    self.assertEqual(b'+3AE-'.decode('utf-7'), '\udc01')
    self.assertEqual(b'+3AE-x'.decode('utf-7'), '\udc01x')
    self.assertEqual('\ud801\U000abcde'.encode('utf-7'), b'+2AHab9ze-')
    self.assertEqual(b'+2AHab9ze-'.decode('utf-7'), '\ud801\U000abcde')
    self.assertEqual(b'+\xc1'.decode('utf-7', 'ignore'), '')
    set_d = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'(),-./:?"
    set_o = '!"#$%&*;<=>@[]^_`{|}'
    for c in set_d:
        self.assertEqual(c.encode('utf7'), c.encode('ascii'))
        self.assertEqual(c.encode('ascii').decode('utf7'), c)
    for c in set_o:
        self.assertEqual(c.encode('ascii').decode('utf7'), c)
    with self.assertRaisesRegex(UnicodeDecodeError, 'ill-formed sequence'):
        b'+@'.decode('utf-7')
