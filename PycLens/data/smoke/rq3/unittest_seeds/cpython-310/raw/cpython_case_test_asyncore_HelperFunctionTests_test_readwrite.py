# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: HelperFunctionTests_test_readwrite

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    attributes = ('read', 'expt', 'write', 'closed', 'error_handled')
    expected = ((select.POLLIN, 'read'), (select.POLLPRI, 'expt'), (select.POLLOUT, 'write'), (select.POLLERR, 'closed'), (select.POLLHUP, 'closed'), (select.POLLNVAL, 'closed'))

    class testobj:

        def __init__(self):
            self.read = False
            self.write = False
            self.closed = False
            self.expt = False
            self.error_handled = False

        def handle_read_event(self):
            self.read = True

        def handle_write_event(self):
            self.write = True

        def handle_close(self):
            self.closed = True

        def handle_expt_event(self):
            self.expt = True

        def handle_error(self):
            self.error_handled = True
    for (flag, expectedattr) in expected:
        tobj = testobj()
        self.assertEqual(getattr(tobj, expectedattr), False)
        asyncore.readwrite(tobj, flag)
        for attr in attributes:
            self.assertEqual(getattr(tobj, attr), attr == expectedattr)
        tr1 = exitingdummy()
        self.assertRaises(asyncore.ExitNow, asyncore.readwrite, tr1, flag)
        tr2 = crashingdummy()
        self.assertEqual(tr2.error_handled, False)
        asyncore.readwrite(tr2, flag)
        self.assertEqual(tr2.error_handled, True)
