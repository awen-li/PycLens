# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestIPv6Environment_test_transfer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def retr():

        def callback(data):
            received.append(data.decode(self.client.encoding))
        received = []
        self.client.retrbinary('retr', callback)
        self.assertEqual(len(''.join(received)), len(RETR_DATA))
        self.assertEqual(''.join(received), RETR_DATA)
    self.client.set_pasv(True)
    retr()
    self.client.set_pasv(False)
    retr()
