# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: DispatcherTests_test_unhandled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = asyncore.dispatcher()
    d.ignore_log_types = ()
    with support.captured_stdout() as stdout:
        d.handle_expt()
        d.handle_read()
        d.handle_write()
        d.handle_connect()
    lines = stdout.getvalue().splitlines()
    expected = ['warning: unhandled incoming priority event', 'warning: unhandled read event', 'warning: unhandled write event', 'warning: unhandled connect event']
    self.assertEqual(lines, expected)
