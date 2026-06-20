# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestBaseExitStack_test_exit_exception_chaining

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def raise_exc(exc):
        raise exc
    saved_details = None

    def suppress_exc(*exc_details):
        nonlocal saved_details
        saved_details = exc_details
        return True
    try:
        with self.exit_stack() as stack:
            stack.callback(raise_exc, IndexError)
            stack.callback(raise_exc, KeyError)
            stack.callback(raise_exc, AttributeError)
            stack.push(suppress_exc)
            stack.callback(raise_exc, ValueError)
            1 / 0
    except IndexError as exc:
        self.assertIsInstance(exc.__context__, KeyError)
        self.assertIsInstance(exc.__context__.__context__, AttributeError)
        self.assertIsNone(exc.__context__.__context__.__context__)
    else:
        self.fail('Expected IndexError, but no exception was raised')
    inner_exc = saved_details[1]
    self.assertIsInstance(inner_exc, ValueError)
    self.assertIsInstance(inner_exc.__context__, ZeroDivisionError)
