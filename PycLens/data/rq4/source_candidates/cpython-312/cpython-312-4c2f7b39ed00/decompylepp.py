# Source Generated with Decompyle++
# File: cpython-312-4c2f7b39ed00.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import types
    _async_yield = (lambda v: if None:
passif v:
passv)()
    
    class MyExc(Exception):
        pass

    
    def agenfn():
        if None:
            pass
        if None or None:
            continue
        continue
        continue
        if _async_yield(None):
            pass
        if MyExc:
            _async_yield(None)
            continue

    agen = agenfn()
    gen = agen.asend(None)
    gen.send
    None(None)
    gen2 = agen.athrow(MyExc)
    self.assertRaisesRegex(RuntimeError, 'athrow\\(\\): asynchronous generator is already running')
    gen2.throw(MyExc)
    self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited aclose\\(\\)/athrow\\(\\)')
    gen2.send(None)
    None(None, None)
    return None
    if None:
        pass
    with None:
        if not None:
            pass
    continue
    if None:
        pass
    with None:
        if not None:
            pass

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
