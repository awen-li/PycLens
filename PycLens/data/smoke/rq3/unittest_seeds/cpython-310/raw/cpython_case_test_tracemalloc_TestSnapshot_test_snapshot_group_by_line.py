# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestSnapshot_test_snapshot_group_by_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (snapshot, snapshot2) = create_snapshots()
    tb_0 = traceback_lineno('<unknown>', 0)
    tb_a_2 = traceback_lineno('a.py', 2)
    tb_a_5 = traceback_lineno('a.py', 5)
    tb_b_1 = traceback_lineno('b.py', 1)
    tb_c_578 = traceback_lineno('c.py', 578)
    stats1 = snapshot.statistics('lineno')
    self.assertEqual(stats1, [tracemalloc.Statistic(tb_b_1, 66, 1), tracemalloc.Statistic(tb_a_2, 30, 3), tracemalloc.Statistic(tb_0, 7, 1), tracemalloc.Statistic(tb_a_5, 2, 1)])
    stats2 = snapshot2.statistics('lineno')
    self.assertEqual(stats2, [tracemalloc.Statistic(tb_a_5, 5002, 2), tracemalloc.Statistic(tb_c_578, 400, 1), tracemalloc.Statistic(tb_a_2, 30, 3)])
    statistics = snapshot2.compare_to(snapshot, 'lineno')
    self.assertEqual(statistics, [tracemalloc.StatisticDiff(tb_a_5, 5002, 5000, 2, 1), tracemalloc.StatisticDiff(tb_c_578, 400, 400, 1, 1), tracemalloc.StatisticDiff(tb_b_1, 0, -66, 0, -1), tracemalloc.StatisticDiff(tb_0, 0, -7, 0, -1), tracemalloc.StatisticDiff(tb_a_2, 30, 0, 3, 0)])
