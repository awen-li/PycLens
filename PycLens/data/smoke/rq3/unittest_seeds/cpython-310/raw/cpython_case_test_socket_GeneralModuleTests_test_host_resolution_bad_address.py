# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_host_resolution_bad_address

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    explanation = 'resolving an invalid IP address did not raise OSError; can be caused by a broken DNS server'
    for addr in ['0.1.1.~1', '1+.1.1.1', '::1q', '::1::2', '1:1:1:1:1:1:1:1:1']:
        with self.assertRaises(OSError, msg=addr):
            socket.gethostbyname(addr)
        with self.assertRaises(OSError, msg=explanation):
            socket.gethostbyaddr(addr)
