# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestSnapshot_test_snapshot_group_by_cumulative

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (snapshot, snapshot2) = create_snapshots()
    tb_0 = traceback_filename('<unknown>')
    tb_a = traceback_filename('a.py')
    tb_b = traceback_filename('b.py')
    tb_a_2 = traceback_lineno('a.py', 2)
    tb_a_5 = traceback_lineno('a.py', 5)
    tb_b_1 = traceback_lineno('b.py', 1)
    tb_b_4 = traceback_lineno('b.py', 4)
    stats = snapshot.statistics('filename', True)
    self.assertEqual(stats, [tracemalloc.Statistic(tb_b, 98, 5), tracemalloc.Statistic(tb_a, 32, 4), tracemalloc.Statistic(tb_0, 7, 1)])
    stats = snapshot.statistics('lineno', True)
    self.assertEqual(stats, [tracemalloc.Statistic(tb_b_1, 66, 1), tracemalloc.Statistic(tb_b_4, 32, 4), tracemalloc.Statistic(tb_a_2, 30, 3), tracemalloc.Statistic(tb_0, 7, 1), tracemalloc.Statistic(tb_a_5, 2, 1)])
