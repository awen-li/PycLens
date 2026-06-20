# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ExceptionChainingTest_test_multiple_args_is_not_wrapped

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg_re = "^\\('a', 'b', 'c'\\)$"
    self.check_not_wrapped(RuntimeError('a', 'b', 'c'), msg_re)
