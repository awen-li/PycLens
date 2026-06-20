# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllibnet.py
# case: urlretrieveNetworkTests_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.urlretrieve(self.logo) as (file_location, info):
        self.assertTrue(os.path.exists(file_location), 'file location returned by urlretrieve is not a valid path')
        with open(file_location, 'rb') as f:
            self.assertTrue(f.read(), 'reading from the file location returned by urlretrieve failed')
