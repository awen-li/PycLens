# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMbox_test_file_perms

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        old_umask = os.umask(63)
        self._box.close()
        os.unlink(self._path)
        self._box = mailbox.mbox(self._path, create=True)
        self._box.add('')
        self._box.close()
    finally:
        os.umask(old_umask)
    st = os.stat(self._path)
    perms = st.st_mode
    self.assertFalse(perms & 73)
