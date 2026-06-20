# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestNamedTemporaryFile_test_del_on_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir = tempfile.mkdtemp()
    try:
        with tempfile.NamedTemporaryFile(dir=dir) as f:
            f.write(b'blat')
        self.assertEqual(os.listdir(dir), [])
        self.assertFalse(os.path.exists(f.name), 'NamedTemporaryFile %s exists after close' % f.name)
    finally:
        os.rmdir(dir)
