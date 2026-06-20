# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_async_for_backwards_jump_has_no_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def arange(n):
        for i in range(n):
            yield i

    async def f():
        async for i in arange(3):
            if i > 100:
                break
    tracer = self.make_tracer()
    coro = f()
    try:
        sys.settrace(tracer.trace)
        coro.send(None)
    except Exception:
        pass
    finally:
        sys.settrace(None)
    events = [(0, 'call'), (1, 'line'), (-3, 'call'), (-2, 'line'), (-1, 'line'), (-1, 'return'), (1, 'exception'), (2, 'line'), (1, 'line'), (-1, 'call'), (-2, 'line'), (-1, 'line'), (-1, 'return'), (1, 'exception'), (2, 'line'), (1, 'line'), (-1, 'call'), (-2, 'line'), (-1, 'line'), (-1, 'return'), (1, 'exception'), (2, 'line'), (1, 'line'), (-1, 'call'), (-2, 'line'), (-2, 'return'), (1, 'exception'), (1, 'return')]
    self.compare_events(f.__code__.co_firstlineno, tracer.events, events)
