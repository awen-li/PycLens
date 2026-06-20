# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: TestErrorMessagesUseQualifiedName_test_too_many_positional

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'A.static_no_args() takes 0 positional arguments but 1 was given'
    with self.check_raises_type_error(msg):
        A.static_no_args("oops it's an arg")
