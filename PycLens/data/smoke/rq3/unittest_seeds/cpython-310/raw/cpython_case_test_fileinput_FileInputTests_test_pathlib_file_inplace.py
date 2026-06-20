# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_pathlib_file_inplace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t1 = Path(self.writeTmp('Pathlib file.'))
    with FileInput(t1, inplace=True, encoding='utf-8') as fi:
        line = fi.readline()
        self.assertEqual(line, 'Pathlib file.')
        print('Modified %s' % line)
    with open(t1, encoding='utf-8') as f:
        self.assertEqual(f.read(), 'Modified Pathlib file.\n')
