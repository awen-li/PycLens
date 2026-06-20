# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_mangling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def f():
            __mangled = 1
            __not_mangled__ = 2
            import __mangled_mod
            import __package__.module
    self.assertIn('_A__mangled', A.f.__code__.co_varnames)
    self.assertIn('__not_mangled__', A.f.__code__.co_varnames)
    self.assertIn('_A__mangled_mod', A.f.__code__.co_varnames)
    self.assertIn('__package__', A.f.__code__.co_varnames)
