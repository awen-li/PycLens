# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_read_does_not_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    alpharep = self.zipfile_ondisk(alpharep)
    with zipfile.ZipFile(alpharep) as file:
        for rep in range(2):
            zipfile.Path(file, 'a.txt').read_text(encoding='utf-8')
