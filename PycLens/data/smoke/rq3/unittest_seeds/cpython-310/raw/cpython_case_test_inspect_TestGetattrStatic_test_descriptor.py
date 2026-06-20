# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class descriptor(object):

        def __get__(self, instance, owner):
            return 3

    class Foo(object):
        d = descriptor()
    foo = Foo()
    foo.__dict__['d'] = 1
    self.assertEqual(inspect.getattr_static(foo, 'd'), 1)
    descriptor.__set__ = lambda s, i, v: None
    self.assertEqual(inspect.getattr_static(foo, 'd'), Foo.__dict__['d'])
