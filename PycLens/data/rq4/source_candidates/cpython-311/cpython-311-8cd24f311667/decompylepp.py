# Source Generated with Decompyle++
# File: cpython-311-8cd24f311667.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'e:é, euro:€, non-bmp:􏿿'.encode('utf-8')
    code = 'import sys; print(ascii(sys.argv[1]))'
    decoded = text.decode('utf-8', 'surrogateescape')
    ascii(decoded).encode('ascii')
# WARNING: Decompyle incomplete

__name__ == '__main__'
if None:
    __pybcsec_seed__()
    return None
