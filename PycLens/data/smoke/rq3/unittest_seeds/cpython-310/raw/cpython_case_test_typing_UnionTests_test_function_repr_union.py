# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: UnionTests_test_function_repr_union

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def fun() -> int:
        ...
    self.assertEqual(repr(Union[fun, int]), 'typing.Union[fun, int]')
