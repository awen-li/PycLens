# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_big_queue_popleft

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pass
    d = deque()
    (append, pop) = (d.append, d.popleft)
    for i in range(BIG):
        append(i)
    for i in range(BIG):
        x = pop()
        if x != i:
            self.assertEqual(x, i)
