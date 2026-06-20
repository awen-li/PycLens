# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_readonly_files

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as dir:
        fname = os.path.join(dir, 'db')
        with dumbdbm.open(fname, 'n') as f:
            self.assertEqual(list(f.keys()), [])
            for key in self._dict:
                f[key] = self._dict[key]
        os.chmod(fname + '.dir', stat.S_IRUSR)
        os.chmod(fname + '.dat', stat.S_IRUSR)
        os.chmod(dir, stat.S_IRUSR | stat.S_IXUSR)
        with dumbdbm.open(fname, 'r') as f:
            self.assertEqual(sorted(f.keys()), sorted(self._dict))
            f.close()
