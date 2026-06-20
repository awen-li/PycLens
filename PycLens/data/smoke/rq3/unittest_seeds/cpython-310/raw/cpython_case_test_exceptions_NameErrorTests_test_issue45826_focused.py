# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: NameErrorTests_test_issue45826_focused

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        try:
            nonsense
        except BaseException as E:
            E.with_traceback(None)
            raise ZeroDivisionError()
    try:
        f()
    except ZeroDivisionError:
        with support.captured_stderr() as err:
            sys.__excepthook__(*sys.exc_info())
    self.assertIn('nonsense', err.getvalue())
    self.assertIn('ZeroDivisionError', err.getvalue())
