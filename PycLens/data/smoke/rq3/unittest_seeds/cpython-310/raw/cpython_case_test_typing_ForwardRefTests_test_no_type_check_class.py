# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_no_type_check_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @no_type_check
    class C:

        def foo(a: 'whatevers') -> {}:
            pass
    cth = get_type_hints(C.foo)
    self.assertEqual(cth, {})
    ith = get_type_hints(C().foo)
    self.assertEqual(ith, {})
