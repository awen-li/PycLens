# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestBaseExitStack_test_push

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exc_raised = ZeroDivisionError

    def _expect_exc(exc_type, exc, exc_tb):
        self.assertIs(exc_type, exc_raised)

    def _suppress_exc(*exc_details):
        return True

    def _expect_ok(exc_type, exc, exc_tb):
        self.assertIsNone(exc_type)
        self.assertIsNone(exc)
        self.assertIsNone(exc_tb)

    class ExitCM(object):

        def __init__(self, check_exc):
            self.check_exc = check_exc

        def __enter__(self):
            self.fail('Should not be called!')

        def __exit__(self, *exc_details):
            self.check_exc(*exc_details)
    with self.exit_stack() as stack:
        stack.push(_expect_ok)
        self.assertIs(stack._exit_callbacks[-1][1], _expect_ok)
        cm = ExitCM(_expect_ok)
        stack.push(cm)
        self.assertIs(stack._exit_callbacks[-1][1].__self__, cm)
        stack.push(_suppress_exc)
        self.assertIs(stack._exit_callbacks[-1][1], _suppress_exc)
        cm = ExitCM(_expect_exc)
        stack.push(cm)
        self.assertIs(stack._exit_callbacks[-1][1].__self__, cm)
        stack.push(_expect_exc)
        self.assertIs(stack._exit_callbacks[-1][1], _expect_exc)
        stack.push(_expect_exc)
        self.assertIs(stack._exit_callbacks[-1][1], _expect_exc)
        1 / 0
