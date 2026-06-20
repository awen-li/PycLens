# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestSnapshot_test_snapshot_group_by_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (snapshot, snapshot2) = create_snapshots()
    tb_0 = traceback_filename('<unknown>')
    tb_a = traceback_filename('a.py')
    tb_b = traceback_filename('b.py')
    tb_c = traceback_filename('c.py')
    stats1 = snapshot.statistics('filename')
    self.assertEqual(stats1, [tracemalloc.Statistic(tb_b, 66, 1), tracemalloc.Statistic(tb_a, 32, 4), tracemalloc.Statistic(tb_0, 7, 1)])
    stats2 = snapshot2.statistics('filename')
    self.assertEqual(stats2, [tracemalloc.Statistic(tb_a, 5032, 5), tracemalloc.Statistic(tb_c, 400, 1)])
    diff = snapshot2.compare_to(snapshot, 'filename')
    self.assertEqual(diff, [tracemalloc.StatisticDiff(tb_a, 5032, 5000, 5, 1), tracemalloc.StatisticDiff(tb_c, 400, 400, 1, 1), tracemalloc.StatisticDiff(tb_b, 0, -66, 0, -1), tracemalloc.StatisticDiff(tb_0, 0, -7, 0, -1)])
