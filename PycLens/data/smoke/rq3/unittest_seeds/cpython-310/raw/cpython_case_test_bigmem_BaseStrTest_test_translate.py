# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_translate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _('aZz.z.Aaz.')
    trans = bytes.maketrans(b'.aZ', b'-!$')
    sublen = len(SUBSTR)
    repeats = size // sublen + 2
    s = SUBSTR * repeats
    s = s.translate(trans)
    self.assertEqual(len(s), repeats * sublen)
    self.assertEqual(s[:sublen], SUBSTR.translate(trans))
    self.assertEqual(s[-sublen:], SUBSTR.translate(trans))
    self.assertEqual(s.count(_('.')), 0)
    self.assertEqual(s.count(_('!')), repeats * 2)
    self.assertEqual(s.count(_('z')), repeats * 3)
