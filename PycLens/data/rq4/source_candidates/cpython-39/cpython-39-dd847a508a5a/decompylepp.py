# Source Generated with Decompyle++
# File: cpython-39-dd847a508a5a.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sniffer = csv.Sniffer()
    self.assertIs(sniffer.has_header(self.sample8), False)
    self.assertIs(sniffer.has_header(self.header2 + self.sample8), True)

if __name__ == '__main__':
    __pybcsec_seed__()
