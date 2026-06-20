# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: LiteralTests_test_illegal_parameters_do_not_raise_runtime_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Literal[int]
    Literal[3j + 2, ..., ()]
    Literal[{'foo': 3, 'bar': 4}]
    Literal[T]
