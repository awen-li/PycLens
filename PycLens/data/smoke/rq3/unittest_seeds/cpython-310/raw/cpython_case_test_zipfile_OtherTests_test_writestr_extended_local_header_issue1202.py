# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_writestr_extended_local_header_issue1202

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, 'w') as orig_zip:
        for data in 'abcdefghijklmnop':
            zinfo = zipfile.ZipInfo(data)
            zinfo.flag_bits |= 8
            orig_zip.writestr(zinfo, data)
