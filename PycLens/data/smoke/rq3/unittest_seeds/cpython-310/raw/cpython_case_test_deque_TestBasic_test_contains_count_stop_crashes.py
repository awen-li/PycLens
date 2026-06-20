# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_contains_count_stop_crashes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def __eq__(self, other):
            d.clear()
            return NotImplemented
    d = deque([A(), A()])
    with self.assertRaises(RuntimeError):
        _ = 3 in d
    d = deque([A(), A()])
    with self.assertRaises(RuntimeError):
        _ = d.count(3)
