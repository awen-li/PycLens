# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = []
    self.client.dir(lambda x: l.append(x))
    self.assertEqual(''.join(l), LIST_DATA.replace('\r\n', ''))
