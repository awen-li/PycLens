# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_bound_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo(object):

        def m(self):
            pass
    f = Foo()
    f.b = f.m
    g = copy.deepcopy(f)
    self.assertEqual(g.m, g.b)
    self.assertIs(g.b.__self__, g)
    g.b()
