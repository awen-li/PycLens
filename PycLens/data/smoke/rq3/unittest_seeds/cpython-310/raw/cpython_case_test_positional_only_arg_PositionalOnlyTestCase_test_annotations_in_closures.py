# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_annotations_in_closures

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def inner_has_pos_only():

        def f(x: int, /):
            ...
        return f
    assert inner_has_pos_only().__annotations__ == {'x': int}

    class Something:

        def method(self):

            def f(x: int, /):
                ...
            return f
    assert Something().method().__annotations__ == {'x': int}

    def multiple_levels():

        def inner_has_pos_only():

            def f(x: int, /):
                ...
            return f
        return inner_has_pos_only()
    assert multiple_levels().__annotations__ == {'x': int}
