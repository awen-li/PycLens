# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: FormatterTest_test_issue_89047

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = logging.Formatter(fmt='{asctime}.{msecs:03.0f} {message}', style='{', datefmt='%Y-%m-%d %H:%M:%S')
    for i in range(2500):
        time.sleep(0.0004)
        r = logging.makeLogRecord({'msg': 'Message %d' % (i + 1)})
        s = f.format(r)
        self.assertNotIn('.1000', s)
