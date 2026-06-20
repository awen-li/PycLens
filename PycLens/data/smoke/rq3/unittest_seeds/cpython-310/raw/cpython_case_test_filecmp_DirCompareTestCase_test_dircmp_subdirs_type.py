# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_filecmp.py
# case: DirCompareTestCase_test_dircmp_subdirs_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyDirCmp(filecmp.dircmp):
        pass
    d = MyDirCmp(self.dir, self.dir_diff)
    sub_dirs = d.subdirs
    self.assertEqual(list(sub_dirs.keys()), ['subdir'])
    sub_dcmp = sub_dirs['subdir']
    self.assertEqual(type(sub_dcmp), MyDirCmp)
