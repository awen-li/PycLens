# Source Generated with Decompyle++
# File: cpython-310-d531cfd01b69.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __p
bcsec_self__ = object()
    __p
bcsec_self__ = self
    
    class CM:
        
        def __aexit__(self):
            pass


    body_executed = None
    
    async def foo():
        body_executed = False
        await CM()
        if <NODE:28>:
            body_executed = True
    # WARNING: Decompyle incomplete

    with self.assertRaisesRegex(AttributeError, '__aenter__'):
        run_async(foo())
        None(None, None, None)
    with None:
        if not None:
            pass
    self.assertIs(body_executed, False)

if __name__ == '__main__':
    pass
with None:
    return None & __pybcsec_seed__()
