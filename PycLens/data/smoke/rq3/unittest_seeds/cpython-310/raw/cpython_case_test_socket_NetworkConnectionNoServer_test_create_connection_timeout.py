# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: NetworkConnectionNoServer_test_create_connection_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.mocked_socket_module():
        try:
            socket.create_connection((HOST, 1234))
        except TimeoutError:
            pass
        except OSError as exc:
            if socket_helper.IPV6_ENABLED or exc.errno != errno.EAFNOSUPPORT:
                raise
        else:
            self.fail('TimeoutError not raised')
