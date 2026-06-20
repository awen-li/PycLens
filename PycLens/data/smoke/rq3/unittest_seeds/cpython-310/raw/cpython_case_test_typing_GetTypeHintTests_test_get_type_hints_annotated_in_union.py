# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetTypeHintTests_test_get_type_hints_annotated_in_union

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def with_union(x: int | list[Annotated[str, 'meta']]):
        ...
    self.assertEqual(get_type_hints(with_union), {'x': int | list[str]})
    self.assertEqual(get_type_hints(with_union, include_extras=True), {'x': int | list[Annotated[str, 'meta']]})
