# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_reversed_new

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    klass = type(reversed(deque()))
    for s in ('abcd', range(2000)):
        self.assertEqual(list(klass(deque(s))), list(reversed(s)))
