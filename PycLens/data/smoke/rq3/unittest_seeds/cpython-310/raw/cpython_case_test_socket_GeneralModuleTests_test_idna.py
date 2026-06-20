# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_idna

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket_helper.transient_internet('python.org'):
        socket.gethostbyname('python.org')
    domain = 'испытание.pythontest.net'
    socket.gethostbyname(domain)
    socket.gethostbyname_ex(domain)
    socket.getaddrinfo(domain, 0, socket.AF_UNSPEC, socket.SOCK_STREAM)
