# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_meta_no_type_check

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @no_type_check_decorator
    def magic_decorator(func):
        return func
    self.assertEqual(magic_decorator.__name__, 'magic_decorator')

    @magic_decorator
    def foo(a: 'whatevers') -> {}:
        pass

    @magic_decorator
    class C:

        def foo(a: 'whatevers') -> {}:
            pass
    self.assertEqual(foo.__name__, 'foo')
    th = get_type_hints(foo)
    self.assertEqual(th, {})
    cth = get_type_hints(C.foo)
    self.assertEqual(cth, {})
    ith = get_type_hints(C().foo)
    self.assertEqual(ith, {})
