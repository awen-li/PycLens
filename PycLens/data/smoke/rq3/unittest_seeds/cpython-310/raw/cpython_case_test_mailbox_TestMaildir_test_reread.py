# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_reread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._box._refresh()
    for subdir in ('cur', 'new'):
        os.utime(os.path.join(self._box._path, subdir), (time.time() - 5,) * 2)
    self._box._skewfactor = -3
    orig_toc = self._box._toc

    def refreshed():
        return self._box._toc is not orig_toc
    self._box._refresh()
    self.assertFalse(refreshed())
    filename = os.path.join(self._path, 'cur', 'stray-file')
    os_helper.create_empty_file(filename)
    os.unlink(filename)
    self._box._refresh()
    self.assertTrue(refreshed())
