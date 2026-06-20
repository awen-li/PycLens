# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: SpecialAttrsTests_test_genericalias_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo(Generic[T]):

        def bar(self):
            pass
        baz = 3
    self.assertIn('bar', dir(Foo[int]))
    self.assertIn('baz', dir(Foo[int]))
