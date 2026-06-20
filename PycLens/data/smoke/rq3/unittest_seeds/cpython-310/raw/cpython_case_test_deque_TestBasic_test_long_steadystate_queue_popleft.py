# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_long_steadystate_queue_popleft

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for size in (0, 1, 2, 100, 1000):
        d = deque(range(size))
        (append, pop) = (d.append, d.popleft)
        for i in range(size, BIG):
            append(i)
            x = pop()
            if x != i - size:
                self.assertEqual(x, i - size)
        self.assertEqual(list(d), list(range(BIG - size, BIG)))
