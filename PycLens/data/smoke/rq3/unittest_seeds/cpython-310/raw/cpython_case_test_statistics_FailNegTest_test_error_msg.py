# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: FailNegTest_test_error_msg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'badness #%d' % random.randint(10000, 99999)
    try:
        next(statistics._fail_neg([-1], msg))
    except statistics.StatisticsError as e:
        errmsg = e.args[0]
    else:
        self.fail("expected exception, but it didn't happen")
    self.assertEqual(errmsg, msg)
