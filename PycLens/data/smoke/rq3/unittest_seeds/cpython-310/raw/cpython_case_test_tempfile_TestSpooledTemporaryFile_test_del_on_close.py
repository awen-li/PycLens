# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestSpooledTemporaryFile_test_del_on_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir = tempfile.mkdtemp()
    try:
        f = tempfile.SpooledTemporaryFile(max_size=10, dir=dir)
        self.assertFalse(f._rolled)
        f.write(b'blat ' * 5)
        self.assertTrue(f._rolled)
        filename = f.name
        f.close()
        self.assertEqual(os.listdir(dir), [])
        if not isinstance(filename, int):
            self.assertFalse(os.path.exists(filename), 'SpooledTemporaryFile %s exists after close' % filename)
    finally:
        os.rmdir(dir)
