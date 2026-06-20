# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: TestErrorMessagesUseQualifiedName_test_positional_only_passed_as_keyword

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = "A.positional_only() got some positional-only arguments passed as keyword arguments: 'arg'"
    with self.check_raises_type_error(msg):
        A.positional_only(arg='x')
