# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: CoroutineTests_test_duck_gen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class GenLike:

        def send(self):
            pass

        def throw(self):
            pass

        def close(self):
            pass

        def __iter__(self):
            pass

        def __next__(self):
            pass
    gen = unittest.mock.MagicMock(GenLike)
    gen.__iter__ = lambda gen: gen
    gen.__name__ = 'gen'
    gen.__qualname__ = 'test.gen'
    self.assertIsInstance(gen, collections.abc.Generator)
    self.assertIs(gen, iter(gen))

    @types.coroutine
    def foo():
        return gen
    wrapper = foo()
    self.assertIsInstance(wrapper, types._GeneratorWrapper)
    self.assertIs(wrapper.__await__(), wrapper)
    self.assertIs(iter(wrapper), wrapper)
    self.assertIsInstance(wrapper, collections.abc.Coroutine)
    self.assertIsInstance(wrapper, collections.abc.Awaitable)
    self.assertIs(wrapper.__qualname__, gen.__qualname__)
    self.assertIs(wrapper.__name__, gen.__name__)
    for name in {'gi_running', 'gi_frame', 'gi_code', 'gi_yieldfrom', 'cr_running', 'cr_frame', 'cr_code', 'cr_await'}:
        with self.assertRaises(AttributeError):
            getattr(wrapper, name)
    gen.gi_running = object()
    gen.gi_frame = object()
    gen.gi_code = object()
    gen.gi_yieldfrom = object()
    self.assertIs(wrapper.gi_running, gen.gi_running)
    self.assertIs(wrapper.gi_frame, gen.gi_frame)
    self.assertIs(wrapper.gi_code, gen.gi_code)
    self.assertIs(wrapper.gi_yieldfrom, gen.gi_yieldfrom)
    self.assertIs(wrapper.cr_running, gen.gi_running)
    self.assertIs(wrapper.cr_frame, gen.gi_frame)
    self.assertIs(wrapper.cr_code, gen.gi_code)
    self.assertIs(wrapper.cr_await, gen.gi_yieldfrom)
    wrapper.close()
    gen.close.assert_called_once_with()
    wrapper.send(1)
    gen.send.assert_called_once_with(1)
    gen.reset_mock()
    next(wrapper)
    gen.__next__.assert_called_once_with()
    gen.reset_mock()
    wrapper.throw(1, 2, 3)
    gen.throw.assert_called_once_with(1, 2, 3)
    gen.reset_mock()
    wrapper.throw(1, 2)
    gen.throw.assert_called_once_with(1, 2)
    gen.reset_mock()
    wrapper.throw(1)
    gen.throw.assert_called_once_with(1)
    gen.reset_mock()
    error = Exception()
    gen.throw.side_effect = error
    try:
        wrapper.throw(1)
    except Exception as ex:
        self.assertIs(ex, error)
    else:
        self.fail('wrapper did not propagate an exception')
    gen.reset_mock()
    with self.assertRaises(TypeError):
        wrapper.throw()
    self.assertFalse(gen.throw.called)
    with self.assertRaises(TypeError):
        wrapper.close(1)
    self.assertFalse(gen.close.called)
    with self.assertRaises(TypeError):
        wrapper.send()
    self.assertFalse(gen.send.called)

    @types.coroutine
    def bar():
        return wrapper
    self.assertIs(wrapper, bar())
    ref = weakref.ref(wrapper)
    self.assertIs(ref(), wrapper)
