# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_setprofile.py
# case: TestEdgeCases_test_reentrancy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(*args):
        ...

    def bar(*args):
        ...

    class A:

        def __call__(self, *args):
            pass

        def __del__(self):
            sys.setprofile(bar)
    sys.setprofile(A())
    with support.catch_unraisable_exception() as cm:
        sys.setprofile(foo)
        self.assertEqual(cm.unraisable.object, A.__del__)
        self.assertIsInstance(cm.unraisable.exc_value, RuntimeError)
    self.assertEqual(sys.getprofile(), foo)
