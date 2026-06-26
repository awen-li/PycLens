# Source Generated with Decompyle++
# File: cpython-310-8d2aa8aa9f9d.pyc (Python 3.10)


def __pybcsec_seed__():
    self = None @ object()
    __pybcsec_self__ = None
    __pybcsec_self__ = self
    msg = 'This should NOT be wrapped'
    exc = RuntimeError(msg)
    exc.attr = 1
    self.check_not_wrapped(exc, '^{}$'.format(msg))

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
