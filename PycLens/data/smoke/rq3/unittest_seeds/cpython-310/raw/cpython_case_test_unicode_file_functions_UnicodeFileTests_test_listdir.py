# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode_file_functions.py
# case: UnicodeFileTests_test_listdir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sf0 = set(self.files)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)
        f1 = os.listdir(os_helper.TESTFN.encode(sys.getfilesystemencoding()))
    f2 = os.listdir(os_helper.TESTFN)
    sf2 = set((os.path.join(os_helper.TESTFN, f) for f in f2))
    self.assertEqual(sf0, sf2, '%a != %a' % (sf0, sf2))
    self.assertEqual(len(f1), len(f2))
