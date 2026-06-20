# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: GeneratorTest_test_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        yield 1
    gen = func()
    self.assertEqual(gen.__name__, 'func')
    self.assertEqual(gen.__qualname__, 'GeneratorTest.test_name.<locals>.func')
    gen.__name__ = 'name'
    gen.__qualname__ = 'qualname'
    self.assertEqual(gen.__name__, 'name')
    self.assertEqual(gen.__qualname__, 'qualname')
    self.assertRaises(TypeError, setattr, gen, '__name__', 123)
    self.assertRaises(TypeError, setattr, gen, '__qualname__', 123)
    self.assertRaises(TypeError, delattr, gen, '__name__')
    self.assertRaises(TypeError, delattr, gen, '__qualname__')
    func.__qualname__ = 'func_qualname'
    func.__name__ = 'func_name'
    gen = func()
    self.assertEqual(gen.__name__, 'func_name')
    self.assertEqual(gen.__qualname__, 'func_qualname')
    gen = (x for x in range(10))
    self.assertEqual(gen.__name__, '<genexpr>')
    self.assertEqual(gen.__qualname__, 'GeneratorTest.test_name.<locals>.<genexpr>')
