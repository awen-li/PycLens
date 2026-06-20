# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_insert_bug_26194

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = 'ABC'
    d = deque(data, maxlen=len(data))
    with self.assertRaises(IndexError):
        d.insert(2, None)
    elements = 'ABCDEFGHI'
    for i in range(-len(elements), len(elements)):
        d = deque(elements, maxlen=len(elements) + 1)
        d.insert(i, 'Z')
        if i >= 0:
            self.assertEqual(d[i], 'Z')
        else:
            self.assertEqual(d[i - 1], 'Z')
