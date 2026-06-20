# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_filecmp.py
# case: DirCompareTestCase_test_report_partial_closure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (left_dir, right_dir) = (self.dir, self.dir_same)
    d = filecmp.dircmp(left_dir, right_dir)
    left_subdir = os.path.join(left_dir, 'subdir')
    right_subdir = os.path.join(right_dir, 'subdir')
    expected_report = ['diff {} {}'.format(self.dir, self.dir_same), "Identical files : ['file']", "Common subdirectories : ['subdir']", '', 'diff {} {}'.format(left_subdir, right_subdir)]
    self._assert_report(d.report_partial_closure, expected_report)
