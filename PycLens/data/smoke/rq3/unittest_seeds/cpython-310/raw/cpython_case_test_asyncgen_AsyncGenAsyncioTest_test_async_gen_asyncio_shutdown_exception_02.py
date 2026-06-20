# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_shutdown_exception_02

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    messages = []

    def exception_handler(loop, context):
        messages.append(context)

    async def async_iterate():
        try:
            yield 1
            yield 2
        finally:
            1 / 0

    async def main():
        loop = asyncio.get_running_loop()
        loop.set_exception_handler(exception_handler)
        async for i in async_iterate():
            break
        gc_collect()
    asyncio.run(main())
    (message,) = messages
    self.assertIsInstance(message['exception'], ZeroDivisionError)
    self.assertIn('unhandled exception during asyncio.run() shutdown', message['message'])
