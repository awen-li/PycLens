# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_builtin_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(SequenceClass(5)), list(range(5)))
    self.assertEqual(list(SequenceClass(0)), [])
    self.assertEqual(list(()), [])
    d = {'one': 1, 'two': 2, 'three': 3}
    self.assertEqual(list(d), list(d.keys()))
    self.assertRaises(TypeError, list, list)
    self.assertRaises(TypeError, list, 42)
    f = open(TESTFN, 'w', encoding='utf-8')
    try:
        for i in range(5):
            f.write('%d\n' % i)
    finally:
        f.close()
    f = open(TESTFN, 'r', encoding='utf-8')
    try:
        self.assertEqual(list(f), ['0\n', '1\n', '2\n', '3\n', '4\n'])
        f.seek(0, 0)
        self.assertEqual(list(f), ['0\n', '1\n', '2\n', '3\n', '4\n'])
    finally:
        f.close()
        try:
            unlink(TESTFN)
        except OSError:
            pass
