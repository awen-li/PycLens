# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_close_erroneous_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'w', encoding='utf-8') as fp:
        fp.write('this is not a legal zip file\n')
    try:
        zf = zipfile.ZipFile(TESTFN)
    except zipfile.BadZipFile:
        pass
