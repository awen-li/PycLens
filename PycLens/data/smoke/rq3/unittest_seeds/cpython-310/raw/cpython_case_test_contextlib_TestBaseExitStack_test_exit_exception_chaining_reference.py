# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestBaseExitStack_test_exit_exception_chaining_reference

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class RaiseExc:

        def __init__(self, exc):
            self.exc = exc

        def __enter__(self):
            return self

        def __exit__(self, *exc_details):
            raise self.exc

    class RaiseExcWithContext:

        def __init__(self, outer, inner):
            self.outer = outer
            self.inner = inner

        def __enter__(self):
            return self

        def __exit__(self, *exc_details):
            try:
                raise self.inner
            except:
                raise self.outer

    class SuppressExc:

        def __enter__(self):
            return self

        def __exit__(self, *exc_details):
            type(self).saved_details = exc_details
            return True
    try:
        with RaiseExc(IndexError):
            with RaiseExcWithContext(KeyError, AttributeError):
                with SuppressExc():
                    with RaiseExc(ValueError):
                        1 / 0
    except IndexError as exc:
        self.assertIsInstance(exc.__context__, KeyError)
        self.assertIsInstance(exc.__context__.__context__, AttributeError)
        self.assertIsNone(exc.__context__.__context__.__context__)
    else:
        self.fail('Expected IndexError, but no exception was raised')
    inner_exc = SuppressExc.saved_details[1]
    self.assertIsInstance(inner_exc, ValueError)
    self.assertIsInstance(inner_exc.__context__, ZeroDivisionError)
