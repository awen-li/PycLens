# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_context_manager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t1 = self.writeTmp('A\nB\nC')
    t2 = self.writeTmp('D\nE\nF')
    with FileInput(files=(t1, t2), encoding='utf-8') as fi:
        lines = list(fi)
    self.assertEqual(lines, ['A\n', 'B\n', 'C', 'D\n', 'E\n', 'F'])
    self.assertEqual(fi.filelineno(), 3)
    self.assertEqual(fi.lineno(), 6)
    self.assertEqual(fi._files, ())
