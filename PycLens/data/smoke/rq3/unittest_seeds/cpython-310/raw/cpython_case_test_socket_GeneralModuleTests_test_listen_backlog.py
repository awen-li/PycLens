# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_listen_backlog

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for backlog in (0, -1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
            srv.bind((HOST, 0))
            srv.listen(backlog)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.bind((HOST, 0))
        srv.listen()
