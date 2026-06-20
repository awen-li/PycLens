# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestRoundtrip_test_random_files

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import glob, random
    fn = support.findfile('tokenize_tests.txt')
    tempdir = os.path.dirname(fn) or os.curdir
    testfiles = glob.glob(os.path.join(glob.escape(tempdir), 'test*.py'))
    testfiles.remove(os.path.join(tempdir, 'test_unicode_identifiers.py'))
    for f in ('buffer', 'builtin', 'fileio', 'inspect', 'os', 'platform', 'sys'):
        testfiles.remove(os.path.join(tempdir, 'test_%s.py') % f)
    if not support.is_resource_enabled('cpu'):
        testfiles = random.sample(testfiles, 10)
    for testfile in testfiles:
        if support.verbose >= 2:
            print('tokenize', testfile)
        with open(testfile, 'rb') as f:
            with self.subTest(file=testfile):
                self.check_roundtrip(f)
