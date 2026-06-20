# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: CoroutineTests_test_gen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gen_func():
        yield 1
        return (yield 2)
    gen = gen_func()

    @types.coroutine
    def foo():
        return gen
    wrapper = foo()
    self.assertIsInstance(wrapper, types._GeneratorWrapper)
    self.assertIs(wrapper.__await__(), gen)
    for name in ('__name__', '__qualname__', 'gi_code', 'gi_running', 'gi_frame'):
        self.assertIs(getattr(foo(), name), getattr(gen, name))
    self.assertIs(foo().cr_code, gen.gi_code)
    self.assertEqual(next(wrapper), 1)
    self.assertEqual(wrapper.send(None), 2)
    with self.assertRaisesRegex(StopIteration, 'spam'):
        wrapper.send('spam')
    gen = gen_func()
    wrapper = foo()
    wrapper.send(None)
    with self.assertRaisesRegex(Exception, 'ham'):
        wrapper.throw(Exception, Exception('ham'))
    foo = types.coroutine(foo)
    self.assertIs(foo().__await__(), gen)
