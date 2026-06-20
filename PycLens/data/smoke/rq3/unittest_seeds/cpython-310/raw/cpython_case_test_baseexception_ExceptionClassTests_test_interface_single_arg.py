# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_baseexception.py
# case: ExceptionClassTests_test_interface_single_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    arg = 'spam'
    exc = Exception(arg)
    results = ([len(exc.args), 1], [exc.args[0], arg], [str(exc), str(arg)], [repr(exc), '%s(%r)' % (exc.__class__.__name__, arg)])
    self.interface_test_driver(results)
