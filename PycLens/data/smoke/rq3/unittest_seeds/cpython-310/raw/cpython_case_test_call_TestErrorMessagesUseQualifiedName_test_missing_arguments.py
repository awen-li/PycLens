# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: TestErrorMessagesUseQualifiedName_test_missing_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = "A.method_two_args() missing 1 required positional argument: 'y'"
    with self.check_raises_type_error(msg):
        A().method_two_args('x')
