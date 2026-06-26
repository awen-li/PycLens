# Source Generated with Decompyle++
# File: cpython-39-ccda63e4c86c.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class Wrapper:
        
        def __init__(self, coro):
            if not coro.__class__ is types.CoroutineType:
                raise None
            self.coro = coro

        
        def __await__(self):
            return self.coro.__await__()


    
    class FutureLike:
        
        def __await__(self):
            yield None


    
    class Marker(Exception):
        pass

    
    async def coro1():
        
        try:
            await FutureLike()
        finally:
            return None
            if ZeroDivisionError:
                raise Marker
        return None


    
    async def coro2():
        await Wrapper(coro1())
        return <NODE:28>

    c = coro2()
    c.send(None)
    with self.assertRaisesRegex(StopIteration, 'spam'):
        c.send('spam')
        None(None, None, None)
    with None:
        if not None:
            pass
    c = coro2()
    c.send(None)
    with self.assertRaises(Marker):
        c.throw(ZeroDivisionError)
        None(None, None, None)
    with None:
        if not None:
            pass

__pybcsec_seed__()
