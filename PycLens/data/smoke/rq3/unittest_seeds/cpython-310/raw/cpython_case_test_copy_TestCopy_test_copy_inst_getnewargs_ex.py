# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_copy_inst_getnewargs_ex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(int):

        def __new__(cls, *, foo):
            self = int.__new__(cls)
            self.foo = foo
            return self

        def __getnewargs_ex__(self):
            return ((), {'foo': self.foo})

        def __eq__(self, other):
            return self.foo == other.foo
    x = C(foo=42)
    y = copy.copy(x)
    self.assertIsInstance(y, C)
    self.assertEqual(y, x)
    self.assertIsNot(y, x)
    self.assertEqual(y.foo, x.foo)
