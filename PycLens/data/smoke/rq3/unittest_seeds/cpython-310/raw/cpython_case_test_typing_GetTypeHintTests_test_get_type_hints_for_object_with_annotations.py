# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetTypeHintTests_test_get_type_hints_for_object_with_annotations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        ...

    class B:
        ...
    b = B()
    b.__annotations__ = {'x': 'A'}
    self.assertEqual(gth(b, locals()), {'x': A})
