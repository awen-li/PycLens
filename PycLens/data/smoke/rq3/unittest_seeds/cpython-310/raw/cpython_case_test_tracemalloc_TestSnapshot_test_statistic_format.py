# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestSnapshot_test_statistic_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (snapshot, snapshot2) = create_snapshots()
    stats = snapshot.statistics('lineno')
    stat = stats[0]
    self.assertEqual(str(stat), 'b.py:1: size=66 B, count=1, average=66 B')
