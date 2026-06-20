# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestBaseExitStack_test_exit_exception_non_suppressing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def raise_exc(exc):
        raise exc

    def suppress_exc(*exc_details):
        return True
    try:
        with self.exit_stack() as stack:
            stack.callback(lambda : None)
            stack.callback(raise_exc, IndexError)
    except Exception as exc:
        self.assertIsInstance(exc, IndexError)
    else:
        self.fail('Expected IndexError, but no exception was raised')
    try:
        with self.exit_stack() as stack:
            stack.callback(raise_exc, KeyError)
            stack.push(suppress_exc)
            stack.callback(raise_exc, IndexError)
    except Exception as exc:
        self.assertIsInstance(exc, KeyError)
    else:
        self.fail('Expected KeyError, but no exception was raised')
