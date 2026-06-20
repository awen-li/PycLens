# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: TimedRotatingFileHandlerTest_test_compute_rollover_weekly_attime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    currentTime = int(time.time())
    today = currentTime - currentTime % 86400
    atTime = datetime.time(12, 0, 0)
    wday = time.gmtime(today).tm_wday
    for day in range(7):
        rh = logging.handlers.TimedRotatingFileHandler(self.fn, encoding='utf-8', when='W%d' % day, interval=1, backupCount=0, utc=True, atTime=atTime)
        try:
            if wday > day:
                expected = 7 - wday + day
            else:
                expected = day - wday
            expected *= 24 * 60 * 60
            expected += 12 * 60 * 60
            expected += today
            actual = rh.computeRollover(today)
            if actual != expected:
                print('failed in timezone: %d' % time.timezone)
                print('local vars: %s' % locals())
            self.assertEqual(actual, expected)
            if day == wday:
                expected += 7 * 24 * 60 * 60
            actual = rh.computeRollover(today + 13 * 60 * 60)
            if actual != expected:
                print('failed in timezone: %d' % time.timezone)
                print('local vars: %s' % locals())
            self.assertEqual(actual, expected)
        finally:
            rh.close()
