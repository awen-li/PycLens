# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: test_compute_rollover

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    rh = logging.handlers.TimedRotatingFileHandler(self.fn, encoding='utf-8', when=when, interval=1, backupCount=0, utc=True)
    currentTime = 0.0
    actual = rh.computeRollover(currentTime)
    if exp != actual:
        if when == 'MIDNIGHT':
            try:
                if rh.utc:
                    t = time.gmtime(currentTime)
                else:
                    t = time.localtime(currentTime)
                currentHour = t[3]
                currentMinute = t[4]
                currentSecond = t[5]
                r = logging.handlers._MIDNIGHT - ((currentHour * 60 + currentMinute) * 60 + currentSecond)
                result = currentTime + r
                print('t: %s (%s)' % (t, rh.utc), file=sys.stderr)
                print('currentHour: %s' % currentHour, file=sys.stderr)
                print('currentMinute: %s' % currentMinute, file=sys.stderr)
                print('currentSecond: %s' % currentSecond, file=sys.stderr)
                print('r: %s' % r, file=sys.stderr)
                print('result: %s' % result, file=sys.stderr)
            except Exception as e:
                print('exception in diagnostic code: %s' % e, file=sys.stderr)
    self.assertEqual(exp, actual)
    rh.close()
