# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestBaseExitStack_test_callback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = [((), {}), ((1,), {}), ((1, 2), {}), ((), dict(example=1)), ((1,), dict(example=1)), ((1, 2), dict(example=1)), ((1, 2), dict(self=3, callback=4))]
    result = []

    def _exit(*args, **kwds):
        """Test metadata propagation"""
        result.append((args, kwds))
    with self.exit_stack() as stack:
        for (args, kwds) in reversed(expected):
            if args and kwds:
                f = stack.callback(_exit, *args, **kwds)
            elif args:
                f = stack.callback(_exit, *args)
            elif kwds:
                f = stack.callback(_exit, **kwds)
            else:
                f = stack.callback(_exit)
            self.assertIs(f, _exit)
        for wrapper in stack._exit_callbacks:
            self.assertIs(wrapper[1].__wrapped__, _exit)
            self.assertNotEqual(wrapper[1].__name__, _exit.__name__)
            self.assertIsNone(wrapper[1].__doc__, _exit.__doc__)
    self.assertEqual(result, expected)
    result = []
    with self.exit_stack() as stack:
        with self.assertRaises(TypeError):
            stack.callback(arg=1)
        with self.assertRaises(TypeError):
            self.exit_stack.callback(arg=2)
        with self.assertRaises(TypeError):
            stack.callback(callback=_exit, arg=3)
    self.assertEqual(result, [])
