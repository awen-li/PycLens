# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_with_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Manager:

        def __init__(self, name):
            self.name = name

        async def __aenter__(self):
            await AsyncYieldFrom(['enter-1-' + self.name, 'enter-2-' + self.name])
            return self

        async def __aexit__(self, *args):
            await AsyncYieldFrom(['exit-1-' + self.name, 'exit-2-' + self.name])
            if self.name == 'B':
                return True

    async def foo():
        async with Manager('A') as a, Manager('B') as b:
            await AsyncYieldFrom([('managers', a.name, b.name)])
            1 / 0
    f = foo()
    (result, _) = run_async(f)
    self.assertEqual(result, ['enter-1-A', 'enter-2-A', 'enter-1-B', 'enter-2-B', ('managers', 'A', 'B'), 'exit-1-B', 'exit-2-B', 'exit-1-A', 'exit-2-A'])

    async def foo():
        async with Manager('A') as a, Manager('C') as c:
            await AsyncYieldFrom([('managers', a.name, c.name)])
            1 / 0
    with self.assertRaises(ZeroDivisionError):
        run_async(foo())
