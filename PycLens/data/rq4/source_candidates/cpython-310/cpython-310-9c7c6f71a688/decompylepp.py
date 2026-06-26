# Source Generated with Decompyle++
# File: cpython-310-9c7c6f71a688.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    async def coroutine():
        return 'spam'

    coro = coroutine()
    await_iter = coro.__await__()
    it = iter(await_iter)
    with self.assertRaisesRegex(StopIteration, 'spam'):
        it.send(None)
        None(None, None, None)
    with None:
        if not None:
            pass
    with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        it.send(None)
        None(None, None, None)
    with None:
        if not None:
            pass
    with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        next(it)
        None(None, None, None)
    with None:
        if not None:
            pass
    with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        it.throw(Exception('wat'))
        None(None, None, None)
    with None:
        if not None:
            pass
    with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        it.throw(Exception('wat'))
        None(None, None, None)
    with None:
        if not None:
            pass
    it.close()
    it.close()

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
