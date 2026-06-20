# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: LiteralTests_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Literal[1]
    Literal[1, 2, 3]
    Literal['x', 'y', 'z']
    Literal[None]
    Literal[True]
    Literal[1, '2', False]
    Literal[Literal[1, 2], Literal[4, 5]]
    Literal[b'foo', u'bar']
