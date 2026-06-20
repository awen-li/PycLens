# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_pathlib_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t1 = Path(self.writeTmp('Pathlib file.'))
    with FileInput(t1, encoding='utf-8') as fi:
        line = fi.readline()
        self.assertEqual(line, 'Pathlib file.')
        self.assertEqual(fi.lineno(), 1)
        self.assertEqual(fi.filelineno(), 1)
        self.assertEqual(fi.filename(), os.fspath(t1))
