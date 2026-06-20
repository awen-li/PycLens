# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_retrbinary_rest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def callback(data):
        received.append(data.decode(self.client.encoding))
    for rest in (0, 10, 20):
        received = []
        self.client.retrbinary('retr', callback, rest=rest)
        self.check_data(''.join(received), RETR_DATA[rest:])
