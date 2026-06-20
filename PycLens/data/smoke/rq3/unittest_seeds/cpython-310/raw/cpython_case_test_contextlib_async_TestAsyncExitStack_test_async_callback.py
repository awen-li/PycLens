# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: TestAsyncExitStack_test_async_callback

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = [((), {}), ((1,), {}), ((1, 2), {}), ((), dict(example=1)), ((1,), dict(example=1)), ((1, 2), dict(example=1))]
    result = []

    async def _exit(*args, **kwds):
        """Test metadata propagation"""
        result.append((args, kwds))
    async with AsyncExitStack() as stack:
        for (args, kwds) in reversed(expected):
            if args and kwds:
                f = stack.push_async_callback(_exit, *args, **kwds)
            elif args:
                f = stack.push_async_callback(_exit, *args)
            elif kwds:
                f = stack.push_async_callback(_exit, **kwds)
            else:
                f = stack.push_async_callback(_exit)
            self.assertIs(f, _exit)
        for wrapper in stack._exit_callbacks:
            self.assertIs(wrapper[1].__wrapped__, _exit)
            self.assertNotEqual(wrapper[1].__name__, _exit.__name__)
            self.assertIsNone(wrapper[1].__doc__, _exit.__doc__)
    self.assertEqual(result, expected)
    result = []
    async with AsyncExitStack() as stack:
        with self.assertRaises(TypeError):
            stack.push_async_callback(arg=1)
        with self.assertRaises(TypeError):
            self.exit_stack.push_async_callback(arg=2)
        with self.assertRaises(TypeError):
            stack.push_async_callback(callback=_exit, arg=3)
    self.assertEqual(result, [])
