# Source Generated with Decompyle++
# File: cpython-312-81a633db3a65.pyc (Python 3.12)


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
    gen.send(None)
    gen2 = agen.asend(None)
    self.assertRaisesRegex(RuntimeError, 'anext\\(\\): asynchronous generator is already running')
    gen2.throw(MyExc)
    None(None, None)
    self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited __anext__\\(\\)/asend\\(\\)')
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
