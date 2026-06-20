# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestNamedTemporaryFile_test_dis_del_on_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir = tempfile.mkdtemp()
    tmp = None
    try:
        f = tempfile.NamedTemporaryFile(dir=dir, delete=False)
        tmp = f.name
        f.write(b'blat')
        f.close()
        self.assertTrue(os.path.exists(f.name), 'NamedTemporaryFile %s missing after close' % f.name)
    finally:
        if tmp is not None:
            os.unlink(tmp)
        os.rmdir(dir)
