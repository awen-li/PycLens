# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: LimitTests_test_extract_stack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    frame = self.last_returns_frame5()

    def extract(**kwargs):
        return traceback.extract_stack(frame, **kwargs)

    def assertEqualExcept(actual, expected, ignore):
        self.assertEqual(actual[:ignore], expected[:ignore])
        self.assertEqual(actual[ignore + 1:], expected[ignore + 1:])
        self.assertEqual(len(actual), len(expected))
    with support.swap_attr(sys, 'tracebacklimit', 1000):
        nolim = extract()
        self.assertGreater(len(nolim), 5)
        self.assertEqual(extract(limit=2), nolim[-2:])
        assertEqualExcept(extract(limit=100), nolim[-100:], -5 - 1)
        self.assertEqual(extract(limit=-2), nolim[:2])
        assertEqualExcept(extract(limit=-100), nolim[:100], len(nolim) - 5 - 1)
        self.assertEqual(extract(limit=0), [])
        del sys.tracebacklimit
        assertEqualExcept(extract(), nolim, -5 - 1)
        sys.tracebacklimit = 2
        self.assertEqual(extract(), nolim[-2:])
        self.assertEqual(extract(limit=3), nolim[-3:])
        self.assertEqual(extract(limit=-3), nolim[:3])
        sys.tracebacklimit = 0
        self.assertEqual(extract(), [])
        sys.tracebacklimit = -1
        self.assertEqual(extract(), [])
