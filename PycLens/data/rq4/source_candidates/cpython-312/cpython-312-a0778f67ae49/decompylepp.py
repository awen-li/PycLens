# Source Generated with Decompyle++
# File: cpython-312-a0778f67ae49.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    has_cycle = None
    
    def f():
        if None:
            pass

    
    def g(exb):
        if None:
            pass
        raise exb
        if None:
            pass
        if Exception:
            if None or None:
                continue
        elif f():
            pass
        if None:
            pass

    exb = KeyError('a')
    gen = g(exb)
    gen.send(None)
    gen.throw(exb)
    self.assertEqual(has_cycle, False)

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
