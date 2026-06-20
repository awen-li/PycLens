# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: HelperFunctionsTests_test_trace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    message = 'bla-bla-bla'
    for (verbose, out) in ((True, message + '\n'), (False, '')):
        with mock.patch('sys.flags', mock.Mock(verbose=verbose)), mock.patch('sys.stderr', io.StringIO()):
            site._trace(message)
            self.assertEqual(sys.stderr.getvalue(), out)
