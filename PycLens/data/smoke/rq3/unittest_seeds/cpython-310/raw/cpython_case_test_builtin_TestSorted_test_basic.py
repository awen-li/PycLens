# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestSorted_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = list(range(100))
    copy = data[:]
    random.shuffle(copy)
    self.assertEqual(data, sorted(copy))
    self.assertNotEqual(data, copy)
    data.reverse()
    random.shuffle(copy)
    self.assertEqual(data, sorted(copy, key=lambda x: -x))
    self.assertNotEqual(data, copy)
    random.shuffle(copy)
    self.assertEqual(data, sorted(copy, reverse=True))
    self.assertNotEqual(data, copy)
