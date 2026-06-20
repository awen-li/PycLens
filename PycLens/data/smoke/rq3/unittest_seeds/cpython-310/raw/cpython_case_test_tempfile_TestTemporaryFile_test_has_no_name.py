# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryFile_test_has_no_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir = tempfile.mkdtemp()
    f = tempfile.TemporaryFile(dir=dir)
    f.write(b'blat')
    try:
        os.rmdir(dir)
    except:
        f.close()
        os.rmdir(dir)
        raise
