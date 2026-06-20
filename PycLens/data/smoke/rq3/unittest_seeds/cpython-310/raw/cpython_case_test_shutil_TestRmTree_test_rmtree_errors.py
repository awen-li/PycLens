# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestRmTree_test_rmtree_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = tempfile.mktemp(dir=self.mkdtemp())
    self.assertRaises(FileNotFoundError, shutil.rmtree, filename)
    shutil.rmtree(filename, ignore_errors=True)
    tmpdir = self.mkdtemp()
    write_file((tmpdir, 'tstfile'), '')
    filename = os.path.join(tmpdir, 'tstfile')
    with self.assertRaises(NotADirectoryError) as cm:
        shutil.rmtree(filename)
    self.assertEqual(cm.exception.filename, filename)
    self.assertTrue(os.path.exists(filename))
    shutil.rmtree(filename, ignore_errors=True)
    self.assertTrue(os.path.exists(filename))
    errors = []

    def onerror(*args):
        errors.append(args)
    shutil.rmtree(filename, onerror=onerror)
    self.assertEqual(len(errors), 2)
    self.assertIs(errors[0][0], os.scandir)
    self.assertEqual(errors[0][1], filename)
    self.assertIsInstance(errors[0][2][1], NotADirectoryError)
    self.assertEqual(errors[0][2][1].filename, filename)
    self.assertIs(errors[1][0], os.rmdir)
    self.assertEqual(errors[1][1], filename)
    self.assertIsInstance(errors[1][2][1], NotADirectoryError)
    self.assertEqual(errors[1][2][1].filename, filename)
