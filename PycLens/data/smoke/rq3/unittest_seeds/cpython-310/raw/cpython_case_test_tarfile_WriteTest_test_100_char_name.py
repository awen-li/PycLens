# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_100_char_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = '0123456789' * 10
    tar = tarfile.open(tmpname, self.mode)
    try:
        t = tarfile.TarInfo(name)
        tar.addfile(t)
    finally:
        tar.close()
    tar = tarfile.open(tmpname)
    try:
        self.assertEqual(tar.getnames()[0], name, 'failed to store 100 char filename')
    finally:
        tar.close()
