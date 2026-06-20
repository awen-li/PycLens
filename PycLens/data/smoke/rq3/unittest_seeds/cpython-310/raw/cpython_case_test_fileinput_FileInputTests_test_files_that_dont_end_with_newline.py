# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_files_that_dont_end_with_newline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t1 = self.writeTmp('A\nB\nC')
    t2 = self.writeTmp('D\nE\nF')
    fi = FileInput(files=(t1, t2), encoding='utf-8')
    lines = list(fi)
    self.assertEqual(lines, ['A\n', 'B\n', 'C', 'D\n', 'E\n', 'F'])
    self.assertEqual(fi.filelineno(), 3)
    self.assertEqual(fi.lineno(), 6)
