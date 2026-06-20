# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_insert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elements = 'ABCDEFGHI'
    for i in range(-5 - len(elements) * 2, 5 + len(elements) * 2):
        d = deque('ABCDEFGHI')
        s = list('ABCDEFGHI')
        d.insert(i, 'Z')
        s.insert(i, 'Z')
        self.assertEqual(list(d), s)
