# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_no_type_check_no_bases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def meth(self, x: int):
            ...

    @no_type_check
    class D(C):
        c = C
    self.assertEqual(get_type_hints(C.meth), {'x': int})
