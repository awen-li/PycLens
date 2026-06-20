# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: CreateServerFunctionalTest_test_dual_stack_client_v4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    port = socket_helper.find_unused_port()
    with socket.create_server(('', port), family=socket.AF_INET6, dualstack_ipv6=True) as sock:
        self.echo_server(sock)
        self.echo_client(('127.0.0.1', port), socket.AF_INET)
