# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: PyZipFileTests_test_write_python_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.mkdir(TESTFN2)
    try:
        with open(os.path.join(TESTFN2, 'mod1.py'), 'w', encoding='utf-8') as fp:
            fp.write('print(42)\n')
        with open(os.path.join(TESTFN2, 'mod2.py'), 'w', encoding='utf-8') as fp:
            fp.write('print(42 * 42)\n')
        with open(os.path.join(TESTFN2, 'mod2.txt'), 'w', encoding='utf-8') as fp:
            fp.write('bla bla bla\n')
        with TemporaryFile() as t, zipfile.PyZipFile(t, 'w') as zipfp:
            zipfp.writepy(TESTFN2)
            names = zipfp.namelist()
            self.assertCompiledIn('mod1.py', names)
            self.assertCompiledIn('mod2.py', names)
            self.assertNotIn('mod2.txt', names)
    finally:
        rmtree(TESTFN2)
