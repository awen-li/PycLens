# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestBaseExitStack_test_exit_exception_with_existing_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def raise_nested(inner_exc, outer_exc):
        try:
            raise inner_exc
        finally:
            raise outer_exc
    exc1 = Exception(1)
    exc2 = Exception(2)
    exc3 = Exception(3)
    exc4 = Exception(4)
    exc5 = Exception(5)
    try:
        with self.exit_stack() as stack:
            stack.callback(raise_nested, exc4, exc5)
            stack.callback(raise_nested, exc2, exc3)
            raise exc1
    except Exception as exc:
        self.assertIs(exc, exc5)
        self.assertIs(exc.__context__, exc4)
        self.assertIs(exc.__context__.__context__, exc3)
        self.assertIs(exc.__context__.__context__.__context__, exc2)
        self.assertIs(exc.__context__.__context__.__context__.__context__, exc1)
        self.assertIsNone(exc.__context__.__context__.__context__.__context__.__context__)
