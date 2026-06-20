# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_indexOf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from operator import indexOf
    self.assertEqual(indexOf([1, 2, 2, 3, 2, 5], 1), 0)
    self.assertEqual(indexOf((1, 2, 2, 3, 2, 5), 2), 1)
    self.assertEqual(indexOf((1, 2, 2, 3, 2, 5), 3), 3)
    self.assertEqual(indexOf((1, 2, 2, 3, 2, 5), 5), 5)
    self.assertRaises(ValueError, indexOf, (1, 2, 2, 3, 2, 5), 0)
    self.assertRaises(ValueError, indexOf, (1, 2, 2, 3, 2, 5), 6)
    self.assertEqual(indexOf('122325', '2'), 1)
    self.assertEqual(indexOf('122325', '5'), 5)
    self.assertRaises(ValueError, indexOf, '122325', '6')
    self.assertRaises(TypeError, indexOf, 42, 1)
    self.assertRaises(TypeError, indexOf, indexOf, indexOf)
    self.assertRaises(ZeroDivisionError, indexOf, BadIterableClass(), 1)
    f = open(TESTFN, 'w', encoding='utf-8')
    try:
        f.write('a\nb\nc\nd\ne\n')
    finally:
        f.close()
    f = open(TESTFN, 'r', encoding='utf-8')
    try:
        fiter = iter(f)
        self.assertEqual(indexOf(fiter, 'b\n'), 1)
        self.assertEqual(indexOf(fiter, 'd\n'), 1)
        self.assertEqual(indexOf(fiter, 'e\n'), 0)
        self.assertRaises(ValueError, indexOf, fiter, 'a\n')
    finally:
        f.close()
        try:
            unlink(TESTFN)
        except OSError:
            pass
    iclass = IteratingSequenceClass(3)
    for i in range(3):
        self.assertEqual(indexOf(iclass, i), i)
    self.assertRaises(ValueError, indexOf, iclass, -1)
