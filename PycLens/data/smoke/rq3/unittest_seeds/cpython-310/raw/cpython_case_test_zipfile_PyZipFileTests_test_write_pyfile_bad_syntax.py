# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: PyZipFileTests_test_write_pyfile_bad_syntax

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.mkdir(TESTFN2)
    try:
        with open(os.path.join(TESTFN2, 'mod1.py'), 'w', encoding='utf-8') as fp:
            fp.write('Bad syntax in python file\n')
        with TemporaryFile() as t, zipfile.PyZipFile(t, 'w') as zipfp:
            with captured_stdout() as s:
                zipfp.writepy(os.path.join(TESTFN2, 'mod1.py'))
            self.assertIn('SyntaxError', s.getvalue())
            names = zipfp.namelist()
            self.assertIn('mod1.py', names)
            self.assertNotIn('mod1.pyc', names)
    finally:
        rmtree(TESTFN2)
