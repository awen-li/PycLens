# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_read_unicode_filenames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fname = findfile('zip_cp437_header.zip')
    with zipfile.ZipFile(fname) as zipfp:
        for name in zipfp.namelist():
            zipfp.open(name).close()
