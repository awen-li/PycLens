# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_filecmp.py
# case: DirCompareTestCase_test_dircmp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (left_dir, right_dir) = (self.dir, self.dir_same)
    d = filecmp.dircmp(left_dir, right_dir)
    self.assertEqual(d.left, left_dir)
    self.assertEqual(d.right, right_dir)
    if self.caseinsensitive:
        self._assert_lists(d.left_list, ['file', 'subdir'])
        self._assert_lists(d.right_list, ['FiLe', 'subdir'])
    else:
        self._assert_lists(d.left_list, ['file', 'subdir'])
        self._assert_lists(d.right_list, ['file', 'subdir'])
    self._assert_lists(d.common, ['file', 'subdir'])
    self._assert_lists(d.common_dirs, ['subdir'])
    self.assertEqual(d.left_only, [])
    self.assertEqual(d.right_only, [])
    self.assertEqual(d.same_files, ['file'])
    self.assertEqual(d.diff_files, [])
    expected_report = ['diff {} {}'.format(self.dir, self.dir_same), "Identical files : ['file']", "Common subdirectories : ['subdir']"]
    self._assert_report(d.report, expected_report)
    (left_dir, right_dir) = (self.dir, self.dir_diff)
    d = filecmp.dircmp(left_dir, right_dir)
    self.assertEqual(d.left, left_dir)
    self.assertEqual(d.right, right_dir)
    self._assert_lists(d.left_list, ['file', 'subdir'])
    self._assert_lists(d.right_list, ['file', 'file2', 'subdir'])
    self._assert_lists(d.common, ['file', 'subdir'])
    self._assert_lists(d.common_dirs, ['subdir'])
    self.assertEqual(d.left_only, [])
    self.assertEqual(d.right_only, ['file2'])
    self.assertEqual(d.same_files, ['file'])
    self.assertEqual(d.diff_files, [])
    expected_report = ['diff {} {}'.format(self.dir, self.dir_diff), "Only in {} : ['file2']".format(self.dir_diff), "Identical files : ['file']", "Common subdirectories : ['subdir']"]
    self._assert_report(d.report, expected_report)
    (left_dir, right_dir) = (self.dir, self.dir_diff)
    shutil.move(os.path.join(self.dir_diff, 'file2'), os.path.join(self.dir, 'file2'))
    d = filecmp.dircmp(left_dir, right_dir)
    self.assertEqual(d.left, left_dir)
    self.assertEqual(d.right, right_dir)
    self._assert_lists(d.left_list, ['file', 'file2', 'subdir'])
    self._assert_lists(d.right_list, ['file', 'subdir'])
    self._assert_lists(d.common, ['file', 'subdir'])
    self.assertEqual(d.left_only, ['file2'])
    self.assertEqual(d.right_only, [])
    self.assertEqual(d.same_files, ['file'])
    self.assertEqual(d.diff_files, [])
    expected_report = ['diff {} {}'.format(self.dir, self.dir_diff), "Only in {} : ['file2']".format(self.dir), "Identical files : ['file']", "Common subdirectories : ['subdir']"]
    self._assert_report(d.report, expected_report)
    with open(os.path.join(self.dir_diff, 'file2'), 'w', encoding='utf-8') as output:
        output.write('Different contents.\n')
    d = filecmp.dircmp(self.dir, self.dir_diff)
    self.assertEqual(d.same_files, ['file'])
    self.assertEqual(d.diff_files, ['file2'])
    expected_report = ['diff {} {}'.format(self.dir, self.dir_diff), "Identical files : ['file']", "Differing files : ['file2']", "Common subdirectories : ['subdir']"]
    self._assert_report(d.report, expected_report)
