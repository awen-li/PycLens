# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_items_symmetric_difference

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rr = random.randrange
    for _ in range(100):
        left = {x: rr(3) for x in range(20) if rr(2)}
        right = {x: rr(3) for x in range(20) if rr(2)}
        with self.subTest(left=left, right=right):
            expected = set(left.items()) ^ set(right.items())
            actual = left.items() ^ right.items()
            self.assertEqual(actual, expected)
