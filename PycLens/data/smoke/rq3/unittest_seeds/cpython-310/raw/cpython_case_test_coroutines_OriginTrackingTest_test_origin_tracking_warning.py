# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: OriginTrackingTest_test_origin_tracking_warning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def corofn():
        pass
    (a1_filename, a1_lineno) = self.here()

    def a1():
        return corofn()
    a1_lineno += 2
    (a2_filename, a2_lineno) = self.here()

    def a2():
        return a1()
    a2_lineno += 2

    def check(depth, msg):
        sys.set_coroutine_origin_tracking_depth(depth)
        with self.assertWarns(RuntimeWarning) as cm:
            a2()
            support.gc_collect()
        self.assertEqual(msg, str(cm.warning))
    orig_depth = sys.get_coroutine_origin_tracking_depth()
    try:
        msg = check(0, f"coroutine '{corofn.__qualname__}' was never awaited")
        check(1, ''.join([f"coroutine '{corofn.__qualname__}' was never awaited\n", 'Coroutine created at (most recent call last)\n', f'  File "{a1_filename}", line {a1_lineno}, in a1\n', f'    return corofn()  # comment in a1']))
        check(2, ''.join([f"coroutine '{corofn.__qualname__}' was never awaited\n", 'Coroutine created at (most recent call last)\n', f'  File "{a2_filename}", line {a2_lineno}, in a2\n', f'    return a1()  # comment in a2\n', f'  File "{a1_filename}", line {a1_lineno}, in a1\n', f'    return corofn()  # comment in a1']))
    finally:
        sys.set_coroutine_origin_tracking_depth(orig_depth)
