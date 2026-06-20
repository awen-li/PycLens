# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ExceptionChainingTest_test_new_override_is_not_wrapped

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CustomNew(RuntimeError):

        def __new__(cls):
            return super().__new__(cls)
    self.check_not_wrapped(CustomNew, '')
