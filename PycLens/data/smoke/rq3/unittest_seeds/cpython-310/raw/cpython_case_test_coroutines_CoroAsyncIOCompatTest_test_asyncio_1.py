# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroAsyncIOCompatTest_test_asyncio_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    asyncio = import_helper.import_module('asyncio')

    class MyException(Exception):
        pass
    buffer = []

    class CM:

        async def __aenter__(self):
            buffer.append(1)
            await asyncio.sleep(0.01)
            buffer.append(2)
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            await asyncio.sleep(0.01)
            buffer.append(exc_type.__name__)

    async def f():
        async with CM() as c:
            await asyncio.sleep(0.01)
            raise MyException
        buffer.append('unreachable')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(f())
    except MyException:
        pass
    finally:
        loop.close()
        asyncio.set_event_loop_policy(None)
    self.assertEqual(buffer, [1, 2, 'MyException'])
