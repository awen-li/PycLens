# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: UnionTests_test_union_generalization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(Union[str, typing.Iterable[int]] == str)
    self.assertFalse(Union[str, typing.Iterable[int]] == typing.Iterable[int])
    self.assertIn(str, Union[str, typing.Iterable[int]].__args__)
    self.assertIn(typing.Iterable[int], Union[str, typing.Iterable[int]].__args__)
