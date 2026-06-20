# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: PEP626Tests_test_lineno_after_raise_in_with_exit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ExitFails:

        def __enter__(self):
            return self

        def __exit__(self, *args):
            raise ValueError

    def after_with():
        with ExitFails():
            1 / 0
    self.lineno_after_raise(after_with, 1, 1)
