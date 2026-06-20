# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllibnet.py
# case: urlretrieveNetworkTests_test_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.urlretrieve(self.logo) as (file_location, info):
        self.assertIsInstance(info, email.message.Message, 'info is not an instance of email.message.Message')
