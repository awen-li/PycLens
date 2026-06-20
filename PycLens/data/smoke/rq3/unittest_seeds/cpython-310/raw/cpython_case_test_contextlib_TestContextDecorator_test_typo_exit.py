# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestContextDecorator_test_typo_exit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class mycontext(ContextDecorator):

        def __enter__(self):
            pass

        def __uxit__(self, *exc):
            pass
    with self.assertRaises(AttributeError):
        with mycontext():
            pass
