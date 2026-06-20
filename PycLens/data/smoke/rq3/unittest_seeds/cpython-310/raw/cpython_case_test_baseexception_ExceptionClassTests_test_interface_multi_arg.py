# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_baseexception.py
# case: ExceptionClassTests_test_interface_multi_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    arg_count = 3
    args = tuple(range(arg_count))
    exc = Exception(*args)
    results = ([len(exc.args), arg_count], [exc.args, args], [str(exc), str(args)], [repr(exc), exc.__class__.__name__ + repr(exc.args)])
    self.interface_test_driver(results)
