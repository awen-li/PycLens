# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_classify_newstyle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):

        def s():
            pass
        s = staticmethod(s)

        def c(cls):
            pass
        c = classmethod(c)

        def getp(self):
            pass
        p = property(getp)

        def m(self):
            pass

        def m1(self):
            pass
        datablob = '1'
        dd = _BrokenDataDescriptor()
        md = _BrokenMethodDescriptor()
    attrs = attrs_wo_objs(A)
    self.assertIn(('__new__', 'static method', object), attrs, 'missing __new__')
    self.assertIn(('__init__', 'method', object), attrs, 'missing __init__')
    self.assertIn(('s', 'static method', A), attrs, 'missing static method')
    self.assertIn(('c', 'class method', A), attrs, 'missing class method')
    self.assertIn(('p', 'property', A), attrs, 'missing property')
    self.assertIn(('m', 'method', A), attrs, 'missing plain method: %r' % attrs)
    self.assertIn(('m1', 'method', A), attrs, 'missing plain method')
    self.assertIn(('datablob', 'data', A), attrs, 'missing data')
    self.assertIn(('md', 'method', A), attrs, 'missing method descriptor')
    self.assertIn(('dd', 'data', A), attrs, 'missing data descriptor')

    class B(A):

        def m(self):
            pass
    attrs = attrs_wo_objs(B)
    self.assertIn(('s', 'static method', A), attrs, 'missing static method')
    self.assertIn(('c', 'class method', A), attrs, 'missing class method')
    self.assertIn(('p', 'property', A), attrs, 'missing property')
    self.assertIn(('m', 'method', B), attrs, 'missing plain method')
    self.assertIn(('m1', 'method', A), attrs, 'missing plain method')
    self.assertIn(('datablob', 'data', A), attrs, 'missing data')
    self.assertIn(('md', 'method', A), attrs, 'missing method descriptor')
    self.assertIn(('dd', 'data', A), attrs, 'missing data descriptor')

    class C(A):

        def m(self):
            pass

        def c(self):
            pass
    attrs = attrs_wo_objs(C)
    self.assertIn(('s', 'static method', A), attrs, 'missing static method')
    self.assertIn(('c', 'method', C), attrs, 'missing plain method')
    self.assertIn(('p', 'property', A), attrs, 'missing property')
    self.assertIn(('m', 'method', C), attrs, 'missing plain method')
    self.assertIn(('m1', 'method', A), attrs, 'missing plain method')
    self.assertIn(('datablob', 'data', A), attrs, 'missing data')
    self.assertIn(('md', 'method', A), attrs, 'missing method descriptor')
    self.assertIn(('dd', 'data', A), attrs, 'missing data descriptor')

    class D(B, C):

        def m1(self):
            pass
    attrs = attrs_wo_objs(D)
    self.assertIn(('s', 'static method', A), attrs, 'missing static method')
    self.assertIn(('c', 'method', C), attrs, 'missing plain method')
    self.assertIn(('p', 'property', A), attrs, 'missing property')
    self.assertIn(('m', 'method', B), attrs, 'missing plain method')
    self.assertIn(('m1', 'method', D), attrs, 'missing plain method')
    self.assertIn(('datablob', 'data', A), attrs, 'missing data')
    self.assertIn(('md', 'method', A), attrs, 'missing method descriptor')
    self.assertIn(('dd', 'data', A), attrs, 'missing data descriptor')
