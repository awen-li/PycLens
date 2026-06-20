# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copy_return_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for fn in (shutil.copy, shutil.copy2):
        src_dir = self.mkdtemp()
        dst_dir = self.mkdtemp()
        src = os.path.join(src_dir, 'foo')
        write_file(src, 'foo')
        rv = fn(src, dst_dir)
        self.assertEqual(rv, os.path.join(dst_dir, 'foo'))
        rv = fn(src, os.path.join(dst_dir, 'bar'))
        self.assertEqual(rv, os.path.join(dst_dir, 'bar'))
