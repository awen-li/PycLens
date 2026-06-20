# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_anext_iter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @types.coroutine
    def _async_yield(v):
        return (yield v)

    class MyError(Exception):
        pass

    async def agenfn():
        try:
            await _async_yield(1)
        except MyError:
            await _async_yield(2)
        return
        yield

    def test1(anext):
        agen = agenfn()
        with contextlib.closing(anext(agen, 'default').__await__()) as g:
            self.assertEqual(g.send(None), 1)
            self.assertEqual(g.throw(MyError, MyError(), None), 2)
            try:
                g.send(None)
            except StopIteration as e:
                err = e
            else:
                self.fail('StopIteration was not raised')
            self.assertEqual(err.value, 'default')

    def test2(anext):
        agen = agenfn()
        with contextlib.closing(anext(agen, 'default').__await__()) as g:
            self.assertEqual(g.send(None), 1)
            self.assertEqual(g.throw(MyError, MyError(), None), 2)
            with self.assertRaises(MyError):
                g.throw(MyError, MyError(), None)

    def test3(anext):
        agen = agenfn()
        with contextlib.closing(anext(agen, 'default').__await__()) as g:
            self.assertEqual(g.send(None), 1)
            g.close()
            with self.assertRaisesRegex(RuntimeError, 'cannot reuse'):
                self.assertEqual(g.send(None), 1)

    def test4(anext):

        @types.coroutine
        def _async_yield(v):
            yield (v * 10)
            return (yield (v * 10 + 1))

        async def agenfn():
            try:
                await _async_yield(1)
            except MyError:
                await _async_yield(2)
            return
            yield
        agen = agenfn()
        with contextlib.closing(anext(agen, 'default').__await__()) as g:
            self.assertEqual(g.send(None), 10)
            self.assertEqual(g.throw(MyError, MyError(), None), 20)
            with self.assertRaisesRegex(MyError, 'val'):
                g.throw(MyError, MyError('val'), None)

    def test5(anext):

        @types.coroutine
        def _async_yield(v):
            yield (v * 10)
            return (yield (v * 10 + 1))

        async def agenfn():
            try:
                await _async_yield(1)
            except MyError:
                return
            yield 'aaa'
        agen = agenfn()
        with contextlib.closing(anext(agen, 'default').__await__()) as g:
            self.assertEqual(g.send(None), 10)
            with self.assertRaisesRegex(StopIteration, 'default'):
                g.throw(MyError, MyError(), None)

    def test6(anext):

        @types.coroutine
        def _async_yield(v):
            yield (v * 10)
            return (yield (v * 10 + 1))

        async def agenfn():
            await _async_yield(1)
            yield 'aaa'
        agen = agenfn()
        with contextlib.closing(anext(agen, 'default').__await__()) as g:
            with self.assertRaises(MyError):
                g.throw(MyError, MyError(), None)

    def run_test(test):
        with self.subTest('pure-Python anext()'):
            test(py_anext)
        with self.subTest('builtin anext()'):
            test(anext)
    run_test(test1)
    run_test(test2)
    run_test(test3)
    run_test(test4)
    run_test(test5)
    run_test(test6)
