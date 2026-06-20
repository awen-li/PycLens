# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestIPv6Environment_test_makeport

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.client.makeport():
        self.assertEqual(self.server.handler_instance.last_received_cmd, 'eprt')
