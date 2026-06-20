# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllibnet.py
# case: urlretrieveNetworkTests_test_specified_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.urlretrieve(self.logo, os_helper.TESTFN) as (file_location, info):
        self.assertEqual(file_location, os_helper.TESTFN)
        self.assertTrue(os.path.exists(file_location))
        with open(file_location, 'rb') as f:
            self.assertTrue(f.read(), 'reading from temporary file failed')
