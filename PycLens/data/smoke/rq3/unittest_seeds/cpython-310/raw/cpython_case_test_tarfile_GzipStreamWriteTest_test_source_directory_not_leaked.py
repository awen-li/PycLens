# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: GzipStreamWriteTest_test_source_directory_not_leaked

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tarfile.open(tmpname, self.mode).close()
    payload = pathlib.Path(tmpname).read_text(encoding='latin-1')
    assert os.path.dirname(tmpname) not in payload
