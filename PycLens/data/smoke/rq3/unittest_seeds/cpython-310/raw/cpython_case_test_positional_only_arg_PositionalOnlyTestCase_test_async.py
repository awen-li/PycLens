# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_async

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def f(a=1, /, b=2):
        return (a, b)
    with self.assertRaisesRegex(TypeError, "f\\(\\) got some positional-only arguments passed as keyword arguments: 'a'"):
        f(a=1, b=2)

    def _check_call(*args, **kwargs):
        try:
            coro = f(*args, **kwargs)
            coro.send(None)
        except StopIteration as e:
            result = e.value
        self.assertEqual(result, (1, 2))
    _check_call(1, 2)
    _check_call(1, b=2)
    _check_call(1)
    _check_call()
