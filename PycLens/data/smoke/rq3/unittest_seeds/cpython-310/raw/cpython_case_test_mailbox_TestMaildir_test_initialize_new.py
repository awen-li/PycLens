# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_initialize_new

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tearDown()
    self._box = mailbox.Maildir(self._path)
    self._check_basics()
    self._delete_recursively(self._path)
    self._box = self._factory(self._path, factory=None)
    self._check_basics()
