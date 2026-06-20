# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_big_stack_right

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = deque()
    (append, pop) = (d.append, d.pop)
    for i in range(BIG):
        append(i)
    for i in reversed(range(BIG)):
        x = pop()
        if x != i:
            self.assertEqual(x, i)
    self.assertEqual(len(d), 0)
