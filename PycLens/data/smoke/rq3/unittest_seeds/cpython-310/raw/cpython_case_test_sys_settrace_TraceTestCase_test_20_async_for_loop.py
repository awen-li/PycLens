# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_20_async_for_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class AsyncIteratorWrapper:

        def __init__(self, obj):
            self._it = iter(obj)

        def __aiter__(self):
            return self

        async def __anext__(self):
            try:
                return next(self._it)
            except StopIteration:
                raise StopAsyncIteration

    async def doit_async():
        async for letter in AsyncIteratorWrapper('abc'):
            x = letter
        y = 42

    def run(tracer):
        x = doit_async()
        try:
            sys.settrace(tracer)
            x.send(None)
        finally:
            sys.settrace(None)
    tracer = self.make_tracer()
    events = [(0, 'call'), (1, 'line'), (-12, 'call'), (-11, 'line'), (-11, 'return'), (-9, 'call'), (-8, 'line'), (-8, 'return'), (-6, 'call'), (-5, 'line'), (-4, 'line'), (-4, 'return'), (1, 'exception'), (2, 'line'), (1, 'line'), (-6, 'call'), (-5, 'line'), (-4, 'line'), (-4, 'return'), (1, 'exception'), (2, 'line'), (1, 'line'), (-6, 'call'), (-5, 'line'), (-4, 'line'), (-4, 'return'), (1, 'exception'), (2, 'line'), (1, 'line'), (-6, 'call'), (-5, 'line'), (-4, 'line'), (-4, 'exception'), (-3, 'line'), (-2, 'line'), (-2, 'exception'), (-2, 'return'), (1, 'exception'), (3, 'line'), (3, 'return')]
    try:
        run(tracer.trace)
    except Exception:
        pass
    self.compare_events(doit_async.__code__.co_firstlineno, tracer.events, events)
