# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode_file_functions.py
# case: UnicodeFileTests_test_normalize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    files = set(self.files)
    others = set()
    for nf in set(['NFC', 'NFD', 'NFKC', 'NFKD']):
        others |= set((normalize(nf, file) for file in files))
    others -= files
    for name in others:
        self._apply_failure(open, name)
        self._apply_failure(os.stat, name)
        self._apply_failure(os.chdir, name)
        self._apply_failure(os.rmdir, name)
        self._apply_failure(os.remove, name)
        self._apply_failure(os.listdir, name)
