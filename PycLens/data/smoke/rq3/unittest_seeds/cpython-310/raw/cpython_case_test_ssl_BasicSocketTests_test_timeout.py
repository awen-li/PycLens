# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for timeout in (None, 0.0, 5.0):
        s = socket.socket(socket.AF_INET)
        s.settimeout(timeout)
        with test_wrap_socket(s) as ss:
            self.assertEqual(timeout, ss.gettimeout())
