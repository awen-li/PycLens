# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyFileObj_test_file_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.get_files() as (src, dst):
        shutil.copyfileobj(src, dst)
        self.assertEqual(src.tell(), self.FILESIZE)
        self.assertEqual(dst.tell(), self.FILESIZE)
