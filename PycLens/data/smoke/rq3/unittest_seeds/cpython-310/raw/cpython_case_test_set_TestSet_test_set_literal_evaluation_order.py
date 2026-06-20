# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_set_literal_evaluation_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    events = []

    def record(obj):
        events.append(obj)
    s = {record(1), record(2), record(3)}
    self.assertEqual(events, [1, 2, 3])
