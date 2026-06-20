# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestContext_test_context_manager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ContextManager:

        def __enter__(self):
            pass

        def __exit__(self, t, v, tb):
            xyzzy
    try:
        with ContextManager():
            1 / 0
    except NameError as e:
        self.assertIsInstance(e.__context__, ZeroDivisionError)
    else:
        self.fail('No exception raised')
