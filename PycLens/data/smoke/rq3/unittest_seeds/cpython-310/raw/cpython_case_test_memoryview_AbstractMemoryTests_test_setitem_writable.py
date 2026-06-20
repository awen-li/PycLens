# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_setitem_writable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not self.rw_type:
        self.skipTest('no writable type to test')
    tp = self.rw_type
    b = self.rw_type(self._source)
    oldrefcount = sys.getrefcount(b)
    m = self._view(b)
    m[0] = ord(b'1')
    self._check_contents(tp, b, b'1bcdef')
    m[0:1] = tp(b'0')
    self._check_contents(tp, b, b'0bcdef')
    m[1:3] = tp(b'12')
    self._check_contents(tp, b, b'012def')
    m[1:1] = tp(b'')
    self._check_contents(tp, b, b'012def')
    m[:] = tp(b'abcdef')
    self._check_contents(tp, b, b'abcdef')
    m[0:3] = m[2:5]
    self._check_contents(tp, b, b'cdedef')
    m[:] = tp(b'abcdef')
    m[2:5] = m[0:3]
    self._check_contents(tp, b, b'ababcf')

    def setitem(key, value):
        m[key] = tp(value)
    self.assertRaises(IndexError, setitem, 6, b'a')
    self.assertRaises(IndexError, setitem, -7, b'a')
    self.assertRaises(IndexError, setitem, sys.maxsize, b'a')
    self.assertRaises(IndexError, setitem, -sys.maxsize, b'a')
    self.assertRaises(TypeError, setitem, 0.0, b'a')
    self.assertRaises(TypeError, setitem, (0,), b'a')
    self.assertRaises(TypeError, setitem, (slice(0, 1, 1), 0), b'a')
    self.assertRaises(TypeError, setitem, (0, slice(0, 1, 1)), b'a')
    self.assertRaises(TypeError, setitem, (0,), b'a')
    self.assertRaises(TypeError, setitem, 'a', b'a')
    slices = (slice(0, 1, 1), slice(0, 1, 2))
    self.assertRaises(NotImplementedError, setitem, slices, b'a')
    exc = ValueError if m.format == 'c' else TypeError
    self.assertRaises(exc, setitem, 0, b'')
    self.assertRaises(exc, setitem, 0, b'ab')
    self.assertRaises(ValueError, setitem, slice(1, 1), b'a')
    self.assertRaises(ValueError, setitem, slice(0, 2), b'a')
    m = None
    self.assertEqual(sys.getrefcount(b), oldrefcount)
