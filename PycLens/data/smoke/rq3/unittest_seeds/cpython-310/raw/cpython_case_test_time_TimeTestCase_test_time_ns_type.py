# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_time_ns_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check_ns(sec, ns):
        self.assertIsInstance(ns, int)
        sec_ns = int(sec * 1000000000.0)
        self.assertLess(sec_ns - ns, 50 ** 6, (sec, ns))
    check_ns(time.time(), time.time_ns())
    check_ns(time.monotonic(), time.monotonic_ns())
    check_ns(time.perf_counter(), time.perf_counter_ns())
    check_ns(time.process_time(), time.process_time_ns())
    if hasattr(time, 'thread_time'):
        check_ns(time.thread_time(), time.thread_time_ns())
    if hasattr(time, 'clock_gettime'):
        check_ns(time.clock_gettime(time.CLOCK_REALTIME), time.clock_gettime_ns(time.CLOCK_REALTIME))
