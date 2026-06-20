# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypeVarTests_test_or

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    X = TypeVar('X')
    self.assertEqual(X | 'x', Union[X, 'x'])
    self.assertEqual('x' | X, Union['x', X])
    self.assertEqual(get_args(X | 'x'), (X, ForwardRef('x')))
    self.assertEqual(get_args('x' | X), (ForwardRef('x'), X))
