# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_folder_file_perms

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig_umask = os.umask(0)
    try:
        subfolder = self._box.add_folder('subfolder')
    finally:
        os.umask(orig_umask)
    path = os.path.join(subfolder._path, 'maildirfolder')
    st = os.stat(path)
    perms = st.st_mode
    self.assertFalse(perms & 73)
