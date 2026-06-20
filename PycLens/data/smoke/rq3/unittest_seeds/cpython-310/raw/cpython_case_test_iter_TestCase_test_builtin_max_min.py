# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_builtin_max_min

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(max(SequenceClass(5)), 4)
    self.assertEqual(min(SequenceClass(5)), 0)
    self.assertEqual(max(8, -1), 8)
    self.assertEqual(min(8, -1), -1)
    d = {'one': 1, 'two': 2, 'three': 3}
    self.assertEqual(max(d), 'two')
    self.assertEqual(min(d), 'one')
    self.assertEqual(max(d.values()), 3)
    self.assertEqual(min(iter(d.values())), 1)
    f = open(TESTFN, 'w', encoding='utf-8')
    try:
        f.write('medium line\n')
        f.write('xtra large line\n')
        f.write('itty-bitty line\n')
    finally:
        f.close()
    f = open(TESTFN, 'r', encoding='utf-8')
    try:
        self.assertEqual(min(f), 'itty-bitty line\n')
        f.seek(0, 0)
        self.assertEqual(max(f), 'xtra large line\n')
    finally:
        f.close()
        try:
            unlink(TESTFN)
        except OSError:
            pass
