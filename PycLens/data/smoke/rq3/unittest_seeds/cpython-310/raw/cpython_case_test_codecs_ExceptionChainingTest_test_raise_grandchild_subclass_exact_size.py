# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ExceptionChainingTest_test_raise_grandchild_subclass_exact_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'This should be wrapped'

    class MyRuntimeError(RuntimeError):
        __slots__ = ()
    self.check_wrapped(MyRuntimeError(msg), msg, MyRuntimeError)
