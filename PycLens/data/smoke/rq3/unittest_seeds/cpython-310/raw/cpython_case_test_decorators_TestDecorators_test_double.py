# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestDecorators_test_double

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        @funcattrs(abc=1, xyz='haha')
        @funcattrs(booh=42)
        def foo(self):
            return 42
    self.assertEqual(C().foo(), 42)
    self.assertEqual(C.foo.abc, 1)
    self.assertEqual(C.foo.xyz, 'haha')
    self.assertEqual(C.foo.booh, 42)
