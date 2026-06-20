# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = deque(range(-5125, -5000))
    d.__init__(range(200))
    for i in range(200, 400):
        d.append(i)
    for i in reversed(range(-200, 0)):
        d.appendleft(i)
    self.assertEqual(list(d), list(range(-200, 400)))
    self.assertEqual(len(d), 600)
    left = [d.popleft() for i in range(250)]
    self.assertEqual(left, list(range(-200, 50)))
    self.assertEqual(list(d), list(range(50, 400)))
    right = [d.pop() for i in range(250)]
    right.reverse()
    self.assertEqual(right, list(range(150, 400)))
    self.assertEqual(list(d), list(range(50, 150)))
