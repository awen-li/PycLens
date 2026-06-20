# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_argspec_api_ignores_wrapped

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.wraps(mod.spam)
    def ham(x, y):
        pass
    self.assertArgSpecEquals(ham, ['x', 'y'], formatted='(x, y)')
    self.assertFullArgSpecEquals(ham, ['x', 'y'], formatted='(x, y)')
    self.assertFullArgSpecEquals(functools.partial(ham), ['x', 'y'], formatted='(x, y)')

    def check_method(f):
        self.assertArgSpecEquals(f, ['self', 'x', 'y'], formatted='(self, x, y)')

    class C:

        @functools.wraps(mod.spam)
        def ham(self, x, y):
            pass
        pham = functools.partialmethod(ham)

        @functools.wraps(mod.spam)
        def __call__(self, x, y):
            pass
    check_method(C())
    check_method(C.ham)
    check_method(C().ham)
    check_method(C.pham)
    check_method(C().pham)

    class C_new:

        @functools.wraps(mod.spam)
        def __new__(self, x, y):
            pass
    check_method(C_new)

    class C_init:

        @functools.wraps(mod.spam)
        def __init__(self, x, y):
            pass
    check_method(C_init)
