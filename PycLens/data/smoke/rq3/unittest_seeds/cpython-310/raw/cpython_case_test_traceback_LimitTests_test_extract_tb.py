# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: LimitTests_test_extract_tb

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        self.last_raises5()
    except Exception:
        (exc_type, exc_value, tb) = sys.exc_info()

    def extract(**kwargs):
        return traceback.extract_tb(tb, **kwargs)
    with support.swap_attr(sys, 'tracebacklimit', 1000):
        nolim = extract()
        self.assertEqual(len(nolim), 5 + 1)
        self.assertEqual(extract(limit=2), nolim[:2])
        self.assertEqual(extract(limit=10), nolim)
        self.assertEqual(extract(limit=-2), nolim[-2:])
        self.assertEqual(extract(limit=-10), nolim)
        self.assertEqual(extract(limit=0), [])
        del sys.tracebacklimit
        self.assertEqual(extract(), nolim)
        sys.tracebacklimit = 2
        self.assertEqual(extract(), nolim[:2])
        self.assertEqual(extract(limit=3), nolim[:3])
        self.assertEqual(extract(limit=-3), nolim[-3:])
        sys.tracebacklimit = 0
        self.assertEqual(extract(), [])
        sys.tracebacklimit = -1
        self.assertEqual(extract(), [])
