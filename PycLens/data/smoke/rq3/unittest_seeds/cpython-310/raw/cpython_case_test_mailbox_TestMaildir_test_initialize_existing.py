# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_initialize_existing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tearDown()
    for subdir in ('', 'tmp', 'new', 'cur'):
        os.mkdir(os.path.normpath(os.path.join(self._path, subdir)))
    self._box = mailbox.Maildir(self._path)
    self._check_basics()
