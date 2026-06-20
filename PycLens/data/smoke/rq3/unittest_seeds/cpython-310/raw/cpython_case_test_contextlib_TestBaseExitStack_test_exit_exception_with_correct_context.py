# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestBaseExitStack_test_exit_exception_with_correct_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @contextmanager
    def gets_the_context_right(exc):
        try:
            yield
        finally:
            raise exc
    exc1 = Exception(1)
    exc2 = Exception(2)
    exc3 = Exception(3)
    exc4 = Exception(4)
    try:
        with self.exit_stack() as stack:
            stack.enter_context(gets_the_context_right(exc4))
            stack.enter_context(gets_the_context_right(exc3))
            stack.enter_context(gets_the_context_right(exc2))
            raise exc1
    except Exception as exc:
        self.assertIs(exc, exc4)
        self.assertIs(exc.__context__, exc3)
        self.assertIs(exc.__context__.__context__, exc2)
        self.assertIs(exc.__context__.__context__.__context__, exc1)
        self.assertIsNone(exc.__context__.__context__.__context__.__context__)
