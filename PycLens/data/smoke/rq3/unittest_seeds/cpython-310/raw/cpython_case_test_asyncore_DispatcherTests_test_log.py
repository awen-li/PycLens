# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: DispatcherTests_test_log

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = asyncore.dispatcher()
    l1 = 'Lovely spam! Wonderful spam!'
    l2 = "I don't like spam!"
    with support.captured_stderr() as stderr:
        d.log(l1)
        d.log(l2)
    lines = stderr.getvalue().splitlines()
    self.assertEqual(lines, ['log: %s' % l1, 'log: %s' % l2])
