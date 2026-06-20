# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_popitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for copymode in (-1, +1):
        for log2size in range(12):
            size = 2 ** log2size
            a = {}
            b = {}
            for i in range(size):
                a[repr(i)] = i
                if copymode < 0:
                    b[repr(i)] = i
            if copymode > 0:
                b = a.copy()
            for i in range(size):
                (ka, va) = ta = a.popitem()
                self.assertEqual(va, int(ka))
                (kb, vb) = tb = b.popitem()
                self.assertEqual(vb, int(kb))
                self.assertFalse(copymode < 0 and ta != tb)
            self.assertFalse(a)
            self.assertFalse(b)
    d = {}
    self.assertRaises(KeyError, d.popitem)
