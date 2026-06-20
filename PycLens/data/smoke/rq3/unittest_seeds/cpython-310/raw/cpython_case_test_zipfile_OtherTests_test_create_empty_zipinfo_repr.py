# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_create_empty_zipinfo_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zi = zipfile.ZipInfo(filename='empty')
    self.assertEqual(repr(zi), "<ZipInfo filename='empty' file_size=0>")
