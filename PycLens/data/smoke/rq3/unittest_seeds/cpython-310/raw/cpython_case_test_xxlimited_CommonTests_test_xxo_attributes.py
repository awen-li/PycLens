# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xxlimited.py
# case: CommonTests_test_xxo_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    xxo = self.module.Xxo()
    with self.assertRaises(AttributeError):
        xxo.foo
    with self.assertRaises(AttributeError):
        del xxo.foo
    xxo.foo = 1234
    self.assertEqual(xxo.foo, 1234)
    del xxo.foo
    with self.assertRaises(AttributeError):
        xxo.foo
