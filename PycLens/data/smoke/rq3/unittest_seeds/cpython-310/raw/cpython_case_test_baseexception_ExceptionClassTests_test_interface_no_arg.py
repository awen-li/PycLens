# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_baseexception.py
# case: ExceptionClassTests_test_interface_no_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exc = Exception()
    results = ([len(exc.args), 0], [exc.args, tuple()], [str(exc), ''], [repr(exc), exc.__class__.__name__ + '()'])
    self.interface_test_driver(results)
