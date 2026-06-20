# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: NameErrorTests_test_name_error_suggestions_from_builtins

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        print(ZeroDivisionErrrrr)
    try:
        func()
    except NameError as exc:
        with support.captured_stderr() as err:
            sys.__excepthook__(*sys.exc_info())
    self.assertIn("'ZeroDivisionError'?", err.getvalue())
