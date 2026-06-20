# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: TimedRotatingFileHandlerTest_test_compute_rollover_daily_attime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    currentTime = 0
    atTime = datetime.time(12, 0, 0)
    rh = logging.handlers.TimedRotatingFileHandler(self.fn, encoding='utf-8', when='MIDNIGHT', interval=1, backupCount=0, utc=True, atTime=atTime)
    try:
        actual = rh.computeRollover(currentTime)
        self.assertEqual(actual, currentTime + 12 * 60 * 60)
        actual = rh.computeRollover(currentTime + 13 * 60 * 60)
        self.assertEqual(actual, currentTime + 36 * 60 * 60)
    finally:
        rh.close()
