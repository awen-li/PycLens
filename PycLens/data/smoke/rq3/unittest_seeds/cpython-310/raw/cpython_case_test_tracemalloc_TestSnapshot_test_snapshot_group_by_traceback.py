# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestSnapshot_test_snapshot_group_by_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (snapshot, snapshot2) = create_snapshots()
    tb1 = traceback(('a.py', 2), ('b.py', 4))
    tb2 = traceback(('a.py', 5), ('b.py', 4))
    tb3 = traceback(('b.py', 1))
    tb4 = traceback(('<unknown>', 0))
    stats1 = snapshot.statistics('traceback')
    self.assertEqual(stats1, [tracemalloc.Statistic(tb3, 66, 1), tracemalloc.Statistic(tb1, 30, 3), tracemalloc.Statistic(tb4, 7, 1), tracemalloc.Statistic(tb2, 2, 1)])
    tb5 = traceback(('c.py', 578))
    stats2 = snapshot2.statistics('traceback')
    self.assertEqual(stats2, [tracemalloc.Statistic(tb2, 5002, 2), tracemalloc.Statistic(tb5, 400, 1), tracemalloc.Statistic(tb1, 30, 3)])
    diff = snapshot2.compare_to(snapshot, 'traceback')
    self.assertEqual(diff, [tracemalloc.StatisticDiff(tb2, 5002, 5000, 2, 1), tracemalloc.StatisticDiff(tb5, 400, 400, 1, 1), tracemalloc.StatisticDiff(tb3, 0, -66, 0, -1), tracemalloc.StatisticDiff(tb4, 0, -7, 0, -1), tracemalloc.StatisticDiff(tb1, 30, 0, 3, 0)])
    self.assertRaises(ValueError, snapshot.statistics, 'traceback', cumulative=True)
