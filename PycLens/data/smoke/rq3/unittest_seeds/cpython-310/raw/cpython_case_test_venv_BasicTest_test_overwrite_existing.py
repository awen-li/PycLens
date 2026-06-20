# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: BasicTest_test_overwrite_existing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.create_contents(self.ENV_SUBDIRS, 'foo')
    venv.create(self.env_dir)
    for subdirs in self.ENV_SUBDIRS:
        fn = os.path.join(self.env_dir, *subdirs + ('foo',))
        self.assertTrue(os.path.exists(fn))
        with open(fn, 'rb') as f:
            self.assertEqual(f.read(), b'Still here?')
    builder = venv.EnvBuilder(clear=True)
    builder.create(self.env_dir)
    for subdirs in self.ENV_SUBDIRS:
        fn = os.path.join(self.env_dir, *subdirs + ('foo',))
        self.assertFalse(os.path.exists(fn))
