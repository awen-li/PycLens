# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: AttributeErrorTests_test_getattr_suggestions_no_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        blech = None

        def __getattr__(self, attr):
            raise AttributeError()
    try:
        A().bluch
    except AttributeError as exc:
        with support.captured_stderr() as err:
            sys.__excepthook__(*sys.exc_info())
    self.assertIn('blech', err.getvalue())

    class A:
        blech = None

        def __getattr__(self, attr):
            raise AttributeError
    try:
        A().bluch
    except AttributeError as exc:
        with support.captured_stderr() as err:
            sys.__excepthook__(*sys.exc_info())
    self.assertIn('blech', err.getvalue())
