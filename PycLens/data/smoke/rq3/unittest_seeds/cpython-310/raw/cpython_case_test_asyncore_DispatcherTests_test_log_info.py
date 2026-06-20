# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: DispatcherTests_test_log_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = asyncore.dispatcher()
    l1 = 'Have you got anything without spam?'
    l2 = "Why can't she have egg bacon spam and sausage?"
    l3 = "THAT'S got spam in it!"
    with support.captured_stdout() as stdout:
        d.log_info(l1, 'EGGS')
        d.log_info(l2)
        d.log_info(l3, 'SPAM')
    lines = stdout.getvalue().splitlines()
    expected = ['EGGS: %s' % l1, 'info: %s' % l2, 'SPAM: %s' % l3]
    self.assertEqual(lines, expected)
