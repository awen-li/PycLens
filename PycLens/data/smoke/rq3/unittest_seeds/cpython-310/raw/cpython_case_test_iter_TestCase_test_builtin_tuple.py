# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_builtin_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(tuple(SequenceClass(5)), (0, 1, 2, 3, 4))
    self.assertEqual(tuple(SequenceClass(0)), ())
    self.assertEqual(tuple([]), ())
    self.assertEqual(tuple(()), ())
    self.assertEqual(tuple('abc'), ('a', 'b', 'c'))
    d = {'one': 1, 'two': 2, 'three': 3}
    self.assertEqual(tuple(d), tuple(d.keys()))
    self.assertRaises(TypeError, tuple, list)
    self.assertRaises(TypeError, tuple, 42)
    f = open(TESTFN, 'w', encoding='utf-8')
    try:
        for i in range(5):
            f.write('%d\n' % i)
    finally:
        f.close()
    f = open(TESTFN, 'r', encoding='utf-8')
    try:
        self.assertEqual(tuple(f), ('0\n', '1\n', '2\n', '3\n', '4\n'))
        f.seek(0, 0)
        self.assertEqual(tuple(f), ('0\n', '1\n', '2\n', '3\n', '4\n'))
    finally:
        f.close()
        try:
            unlink(TESTFN)
        except OSError:
            pass
