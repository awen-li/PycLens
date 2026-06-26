# Source Generated with Decompyle++
# File: cpython-39-05c7afdebcba.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'from __future__ import generator_stop\nfrom contextlib import contextmanager\n@contextmanager\ndef woohoo():\n    yield\n'
    locals = { }
    exec(code, locals, locals)
    woohoo = locals['woohoo']
    a

_exc = StopIteration('spam')
    
    try:
        with woohoo():
            raise a

_exc
            None(None, None, None)
        with None:
            if not None:
                pass
    finally:
        pass
    if Exception:
        ex = None
        
        try:
            self.assertIs(ex, a

_exc)
        finally:
            ex = None
            del ex
        ex = None
        del ex
        return None



if __name__ == '__main__':
    __pybcsec_seed__()
