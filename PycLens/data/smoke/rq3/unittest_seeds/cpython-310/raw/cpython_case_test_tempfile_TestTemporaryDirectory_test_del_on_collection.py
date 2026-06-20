# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryDirectory_test_del_on_collection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir = tempfile.mkdtemp()
    try:
        d = self.do_create(dir=dir)
        name = d.name
        del d
        self.assertFalse(os.path.exists(name), 'TemporaryDirectory %s exists after __del__' % name)
    finally:
        os.rmdir(dir)
