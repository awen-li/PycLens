# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_multiple_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __init__(self):
            self.__state = 0

        def getstate(self):
            return self.__state

        def setstate(self, state):
            self.__state = state
    a = C()
    self.assertEqual(a.getstate(), 0)
    a.setstate(10)
    self.assertEqual(a.getstate(), 10)

    class D(dict, C):

        def __init__(self):
            type({}).__init__(self)
            C.__init__(self)
    d = D()
    self.assertEqual(list(d.keys()), [])
    d['hello'] = 'world'
    self.assertEqual(list(d.items()), [('hello', 'world')])
    self.assertEqual(d['hello'], 'world')
    self.assertEqual(d.getstate(), 0)
    d.setstate(10)
    self.assertEqual(d.getstate(), 10)
    self.assertEqual(D.__mro__, (D, dict, C, object))

    class Node(object):

        def __int__(self):
            return int(self.foo())

        def foo(self):
            return '23'

    class Frag(Node, list):

        def foo(self):
            return '42'
    self.assertEqual(Node().__int__(), 23)
    self.assertEqual(int(Node()), 23)
    self.assertEqual(Frag().__int__(), 42)
    self.assertEqual(int(Frag()), 42)
