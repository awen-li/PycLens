# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, dir, 42, 42)
    local_var = 1
    self.assertIn('local_var', dir())
    self.assertIn('exit', dir(sys))

    class Foo(types.ModuleType):
        __dict__ = 8
    f = Foo('foo')
    self.assertRaises(TypeError, dir, f)
    self.assertIn('strip', dir(str))
    self.assertNotIn('__mro__', dir(str))

    class Foo(object):

        def __init__(self):
            self.x = 7
            self.y = 8
            self.z = 9
    f = Foo()
    self.assertIn('y', dir(f))

    class Foo(object):
        __slots__ = []
    f = Foo()
    self.assertIn('__repr__', dir(f))

    class Foo(object):
        __slots__ = ['__class__', '__dict__']

        def __init__(self):
            self.bar = 'wow'
    f = Foo()
    self.assertNotIn('__repr__', dir(f))
    self.assertIn('bar', dir(f))

    class Foo(object):

        def __dir__(self):
            return ['kan', 'ga', 'roo']
    f = Foo()
    self.assertTrue(dir(f) == ['ga', 'kan', 'roo'])

    class Foo(object):

        def __dir__(self):
            return ('b', 'c', 'a')
    res = dir(Foo())
    self.assertIsInstance(res, list)
    self.assertTrue(res == ['a', 'b', 'c'])

    class Foo(object):

        def __dir__(self):
            return 7
    f = Foo()
    self.assertRaises(TypeError, dir, f)
    try:
        raise IndexError
    except IndexError as e:
        self.assertEqual(len(dir(e.__traceback__)), 4)
    self.assertEqual(sorted([].__dir__()), dir([]))
