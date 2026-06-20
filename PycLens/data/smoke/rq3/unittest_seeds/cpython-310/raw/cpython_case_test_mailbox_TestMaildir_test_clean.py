# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_clean

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    foo_path = os.path.join(self._path, 'tmp', 'foo')
    bar_path = os.path.join(self._path, 'tmp', 'bar')
    with open(foo_path, 'w', encoding='utf-8') as f:
        f.write('@')
    with open(bar_path, 'w', encoding='utf-8') as f:
        f.write('@')
    self._box.clean()
    self.assertTrue(os.path.exists(foo_path))
    self.assertTrue(os.path.exists(bar_path))
    foo_stat = os.stat(foo_path)
    os.utime(foo_path, (time.time() - 129600 - 2, foo_stat.st_mtime))
    self._box.clean()
    self.assertFalse(os.path.exists(foo_path))
    self.assertTrue(os.path.exists(bar_path))
