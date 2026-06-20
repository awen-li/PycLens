# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: OriginTrackingTest_test_origin_tracking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig_depth = sys.get_coroutine_origin_tracking_depth()
    try:

        async def corofn():
            pass
        sys.set_coroutine_origin_tracking_depth(0)
        self.assertEqual(sys.get_coroutine_origin_tracking_depth(), 0)
        with contextlib.closing(corofn()) as coro:
            self.assertIsNone(coro.cr_origin)
        sys.set_coroutine_origin_tracking_depth(1)
        self.assertEqual(sys.get_coroutine_origin_tracking_depth(), 1)
        (fname, lineno) = self.here()
        with contextlib.closing(corofn()) as coro:
            self.assertEqual(coro.cr_origin, ((fname, lineno + 1, 'test_origin_tracking'),))
        sys.set_coroutine_origin_tracking_depth(2)
        self.assertEqual(sys.get_coroutine_origin_tracking_depth(), 2)

        def nested():
            return (self.here(), corofn())
        (fname, lineno) = self.here()
        ((nested_fname, nested_lineno), coro) = nested()
        with contextlib.closing(coro):
            self.assertEqual(coro.cr_origin, ((nested_fname, nested_lineno, 'nested'), (fname, lineno + 1, 'test_origin_tracking')))
        sys.set_coroutine_origin_tracking_depth(1000)
        with contextlib.closing(corofn()) as coro:
            self.assertTrue(2 < len(coro.cr_origin) < 1000)
        with self.assertRaises(ValueError):
            sys.set_coroutine_origin_tracking_depth(-1)
        self.assertEqual(sys.get_coroutine_origin_tracking_depth(), 1000)
    finally:
        sys.set_coroutine_origin_tracking_depth(orig_depth)
