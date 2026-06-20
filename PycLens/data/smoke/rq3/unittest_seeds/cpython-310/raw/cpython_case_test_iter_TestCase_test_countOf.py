# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_countOf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from operator import countOf
    self.assertEqual(countOf([1, 2, 2, 3, 2, 5], 2), 3)
    self.assertEqual(countOf((1, 2, 2, 3, 2, 5), 2), 3)
    self.assertEqual(countOf('122325', '2'), 3)
    self.assertEqual(countOf('122325', '6'), 0)
    self.assertRaises(TypeError, countOf, 42, 1)
    self.assertRaises(TypeError, countOf, countOf, countOf)
    d = {'one': 3, 'two': 3, 'three': 3, 1j: 2j}
    for k in d:
        self.assertEqual(countOf(d, k), 1)
    self.assertEqual(countOf(d.values(), 3), 3)
    self.assertEqual(countOf(d.values(), 2j), 1)
    self.assertEqual(countOf(d.values(), 1j), 0)
    f = open(TESTFN, 'w', encoding='utf-8')
    try:
        f.write('a\nb\nc\nb\n')
    finally:
        f.close()
    f = open(TESTFN, 'r', encoding='utf-8')
    try:
        for (letter, count) in (('a', 1), ('b', 2), ('c', 1), ('d', 0)):
            f.seek(0, 0)
            self.assertEqual(countOf(f, letter + '\n'), count)
    finally:
        f.close()
        try:
            unlink(TESTFN)
        except OSError:
            pass
