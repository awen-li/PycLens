# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_getslice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def by(s):
        return self.type2test(map(ord, s))
    b = by('Hello, world')
    self.assertEqual(b[:5], by('Hello'))
    self.assertEqual(b[1:5], by('ello'))
    self.assertEqual(b[5:7], by(', '))
    self.assertEqual(b[7:], by('world'))
    self.assertEqual(b[7:12], by('world'))
    self.assertEqual(b[7:100], by('world'))
    self.assertEqual(b[:-7], by('Hello'))
    self.assertEqual(b[-11:-7], by('ello'))
    self.assertEqual(b[-7:-5], by(', '))
    self.assertEqual(b[-5:], by('world'))
    self.assertEqual(b[-5:12], by('world'))
    self.assertEqual(b[-5:100], by('world'))
    self.assertEqual(b[-100:5], by('Hello'))
