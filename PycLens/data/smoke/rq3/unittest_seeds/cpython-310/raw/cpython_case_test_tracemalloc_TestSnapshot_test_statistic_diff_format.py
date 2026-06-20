# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestSnapshot_test_statistic_diff_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (snapshot, snapshot2) = create_snapshots()
    stats = snapshot2.compare_to(snapshot, 'lineno')
    stat = stats[0]
    self.assertEqual(str(stat), 'a.py:5: size=5002 B (+5000 B), count=2 (+1), average=2501 B')
