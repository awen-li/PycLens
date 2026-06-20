# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ExceptionChainingTest_test_instance_attribute_is_not_wrapped

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'This should NOT be wrapped'
    exc = RuntimeError(msg)
    exc.attr = 1
    self.check_not_wrapped(exc, '^{}$'.format(msg))
