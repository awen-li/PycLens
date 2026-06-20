# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_find

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'mississippi')
    i = 105
    w = 119
    self.assertEqual(b.find(b'ss'), 2)
    self.assertEqual(b.find(b'w'), -1)
    self.assertEqual(b.find(b'mississippian'), -1)
    self.assertEqual(b.find(i), 1)
    self.assertEqual(b.find(w), -1)
    self.assertEqual(b.find(b'ss', 3), 5)
    self.assertEqual(b.find(b'ss', 1, 7), 2)
    self.assertEqual(b.find(b'ss', 1, 3), -1)
    self.assertEqual(b.find(i, 6), 7)
    self.assertEqual(b.find(i, 1, 3), 1)
    self.assertEqual(b.find(w, 1, 3), -1)
    for index in (-1, 256, sys.maxsize + 1):
        self.assertRaisesRegex(ValueError, 'byte must be in range\\(0, 256\\)', b.find, index)
