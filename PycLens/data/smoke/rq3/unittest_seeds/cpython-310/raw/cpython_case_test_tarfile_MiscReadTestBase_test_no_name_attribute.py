# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_no_name_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(self.tarname, 'rb') as fobj:
        data = fobj.read()
    fobj = io.BytesIO(data)
    self.assertRaises(AttributeError, getattr, fobj, 'name')
    tar = tarfile.open(fileobj=fobj, mode=self.mode)
    self.assertIsNone(tar.name)
