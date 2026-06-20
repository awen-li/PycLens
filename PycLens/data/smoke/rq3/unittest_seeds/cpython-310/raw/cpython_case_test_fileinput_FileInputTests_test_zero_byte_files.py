# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_zero_byte_files

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t1 = self.writeTmp('')
    t2 = self.writeTmp('')
    t3 = self.writeTmp('The only line there is.\n')
    t4 = self.writeTmp('')
    fi = FileInput(files=(t1, t2, t3, t4), encoding='utf-8')
    line = fi.readline()
    self.assertEqual(line, 'The only line there is.\n')
    self.assertEqual(fi.lineno(), 1)
    self.assertEqual(fi.filelineno(), 1)
    self.assertEqual(fi.filename(), t3)
    line = fi.readline()
    self.assertFalse(line)
    self.assertEqual(fi.lineno(), 1)
    self.assertEqual(fi.filelineno(), 0)
    self.assertEqual(fi.filename(), t4)
    fi.close()
