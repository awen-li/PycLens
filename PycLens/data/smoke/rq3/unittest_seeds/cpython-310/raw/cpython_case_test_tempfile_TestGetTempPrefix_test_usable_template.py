# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestGetTempPrefix_test_usable_template

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = tempfile.gettempprefix() + 'xxxxxx.xxx'
    d = tempfile.mkdtemp(prefix='')
    try:
        p = os.path.join(d, p)
        fd = os.open(p, os.O_RDWR | os.O_CREAT)
        os.close(fd)
        os.unlink(p)
    finally:
        os.rmdir(d)
