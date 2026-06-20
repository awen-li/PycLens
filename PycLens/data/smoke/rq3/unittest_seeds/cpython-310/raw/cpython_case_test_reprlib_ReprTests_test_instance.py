# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: ReprTests_test_instance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    i1 = ClassWithRepr('a')
    eq(r(i1), repr(i1))
    i2 = ClassWithRepr('x' * 1000)
    expected = repr(i2)[:13] + '...' + repr(i2)[-14:]
    eq(r(i2), expected)
    i3 = ClassWithFailingRepr()
    eq(r(i3), '<ClassWithFailingRepr instance at %#x>' % id(i3))
    s = r(ClassWithFailingRepr)
    self.assertTrue(s.startswith('<class '))
    self.assertTrue(s.endswith('>'))
    self.assertIn(s.find('...'), [12, 13])
