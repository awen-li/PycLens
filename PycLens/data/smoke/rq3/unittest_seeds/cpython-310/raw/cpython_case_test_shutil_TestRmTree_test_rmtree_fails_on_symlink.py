# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestRmTree_test_rmtree_fails_on_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp = self.mkdtemp()
    dir_ = os.path.join(tmp, 'dir')
    os.mkdir(dir_)
    link = os.path.join(tmp, 'link')
    os.symlink(dir_, link)
    self.assertRaises(OSError, shutil.rmtree, link)
    self.assertTrue(os.path.exists(dir_))
    self.assertTrue(os.path.lexists(link))
    errors = []

    def onerror(*args):
        errors.append(args)
    shutil.rmtree(link, onerror=onerror)
    self.assertEqual(len(errors), 1)
    self.assertIs(errors[0][0], os.path.islink)
    self.assertEqual(errors[0][1], link)
    self.assertIsInstance(errors[0][2][1], OSError)
