# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_super.py
# case: TestSuper_test_super_with_closure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class E(A):

        def f(self):

            def nested():
                self
            return super().f() + 'E'
    self.assertEqual(E().f(), 'AE')
