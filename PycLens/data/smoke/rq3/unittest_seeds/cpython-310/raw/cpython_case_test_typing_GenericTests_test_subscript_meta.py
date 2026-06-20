# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_subscript_meta

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class Meta(type):
        ...
    self.assertEqual(Type[Meta], Type[Meta])
    self.assertEqual(Union[T, int][Meta], Union[Meta, int])
    self.assertEqual(Callable[..., Meta].__args__, (Ellipsis, Meta))
