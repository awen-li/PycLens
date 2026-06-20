# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sched.py
# case: TestCase_test_priority

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = []
    fun = lambda x: l.append(x)
    scheduler = sched.scheduler(time.time, time.sleep)
    cases = [([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), ([2, 5, 3, 1, 4], [1, 2, 3, 4, 5]), ([1, 2, 3, 2, 1], [1, 1, 2, 2, 3])]
    for (priorities, expected) in cases:
        with self.subTest(priorities=priorities, expected=expected):
            for priority in priorities:
                scheduler.enterabs(0.01, priority, fun, (priority,))
            scheduler.run()
            self.assertEqual(l, expected)
            self.assertTrue(scheduler.empty())
            l.clear()
