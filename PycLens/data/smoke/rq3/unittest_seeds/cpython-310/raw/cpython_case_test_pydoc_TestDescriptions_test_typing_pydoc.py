# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_typing_pydoc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(data: typing.List[typing.Any], x: int) -> typing.Iterator[typing.Tuple[int, typing.Any]]:
        ...
    T = typing.TypeVar('T')

    class C(typing.Generic[T], typing.Mapping[int, str]):
        ...
    self.assertEqual(pydoc.render_doc(foo).splitlines()[-1], 'f\x08fo\x08oo\x08o(data: List[Any], x: int) -> Iterator[Tuple[int, Any]]')
    self.assertEqual(pydoc.render_doc(C).splitlines()[2], 'class C\x08C(collections.abc.Mapping, typing.Generic)')
