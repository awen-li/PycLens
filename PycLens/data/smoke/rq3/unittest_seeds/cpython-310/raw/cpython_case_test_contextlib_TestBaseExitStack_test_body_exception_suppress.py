# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestBaseExitStack_test_body_exception_suppress

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def suppress_exc(*exc_details):
        return True
    try:
        with self.exit_stack() as stack:
            stack.push(suppress_exc)
            1 / 0
    except IndexError as exc:
        self.fail('Expected no exception, got IndexError')
