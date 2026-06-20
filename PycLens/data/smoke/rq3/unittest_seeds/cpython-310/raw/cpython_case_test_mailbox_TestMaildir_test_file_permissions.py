# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_file_permissions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.MaildirMessage(self._template % 0)
    orig_umask = os.umask(0)
    try:
        key = self._box.add(msg)
    finally:
        os.umask(orig_umask)
    path = os.path.join(self._path, self._box._lookup(key))
    mode = os.stat(path).st_mode
    self.assertFalse(mode & 73)
