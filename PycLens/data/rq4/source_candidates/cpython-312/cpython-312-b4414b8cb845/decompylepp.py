# Source Generated with Decompyle++
# File: cpython-312-b4414b8cb845.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r = repr(sock)
    cm = self.assertWarns(ResourceWarning)
    sock = None
    support.gc_collect()
    None(None, None)
    self.assertIn(r, None(str.warning.args[0]))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    f = sock.makefile('rb')
    r = repr(sock)
    sock = None
    support.gc_collect()
    self.assertWarns(ResourceWarning)
    f = None
    support.gc_collect()
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
