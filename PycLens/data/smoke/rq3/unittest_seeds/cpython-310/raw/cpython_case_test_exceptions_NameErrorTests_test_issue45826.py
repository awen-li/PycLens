# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: NameErrorTests_test_issue45826

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        with self.assertRaisesRegex(NameError, 'aaa'):
            aab
    try:
        f()
    except self.failureException:
        with support.captured_stderr() as err:
            sys.__excepthook__(*sys.exc_info())
    self.assertIn('aab', err.getvalue())
