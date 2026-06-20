# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_slice_and_getitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _('0123456789')
    sublen = len(SUBSTR)
    s = SUBSTR * (size // sublen)
    stepsize = len(s) // 100
    stepsize = stepsize - stepsize % sublen
    for i in range(0, len(s) - stepsize, stepsize):
        self.assertEqual(s[i], SUBSTR[0])
        self.assertEqual(s[i:i + sublen], SUBSTR)
        self.assertEqual(s[i:i + sublen:2], SUBSTR[::2])
        if i > 0:
            self.assertEqual(s[i + sublen - 1:i - 1:-3], SUBSTR[sublen::-3])
    self.assertEqual(s[len(s) - 1], SUBSTR[-1])
    self.assertEqual(s[-1], SUBSTR[-1])
    self.assertEqual(s[len(s) - 10], SUBSTR[0])
    self.assertEqual(s[-sublen], SUBSTR[0])
    self.assertEqual(s[len(s):], _(''))
    self.assertEqual(s[len(s) - 1:], SUBSTR[-1:])
    self.assertEqual(s[-1:], SUBSTR[-1:])
    self.assertEqual(s[len(s) - sublen:], SUBSTR)
    self.assertEqual(s[-sublen:], SUBSTR)
    self.assertEqual(len(s[:]), len(s))
    self.assertEqual(len(s[:len(s) - 5]), len(s) - 5)
    self.assertEqual(len(s[5:-5]), len(s) - 10)
    self.assertRaises(IndexError, operator.getitem, s, len(s))
    self.assertRaises(IndexError, operator.getitem, s, len(s) + 1)
    self.assertRaises(IndexError, operator.getitem, s, len(s) + 1 << 31)
