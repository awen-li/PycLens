# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_glob.py
# case: SymlinkLoopGlobTests_test_selflink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tempdir = TESTFN + '_dir'
    os.makedirs(tempdir)
    self.addCleanup(shutil.rmtree, tempdir)
    with change_cwd(tempdir):
        os.makedirs('dir')
        create_empty_file(os.path.join('dir', 'file'))
        os.symlink(os.curdir, os.path.join('dir', 'link'))
        results = glob.glob('**', recursive=True)
        self.assertEqual(len(results), len(set(results)))
        results = set(results)
        depth = 0
        while results:
            path = os.path.join(*['dir'] + ['link'] * depth)
            self.assertIn(path, results)
            results.remove(path)
            if not results:
                break
            path = os.path.join(path, 'file')
            self.assertIn(path, results)
            results.remove(path)
            depth += 1
        results = glob.glob(os.path.join('**', 'file'), recursive=True)
        self.assertEqual(len(results), len(set(results)))
        results = set(results)
        depth = 0
        while results:
            path = os.path.join(*['dir'] + ['link'] * depth + ['file'])
            self.assertIn(path, results)
            results.remove(path)
            depth += 1
        results = glob.glob(os.path.join('**', ''), recursive=True)
        self.assertEqual(len(results), len(set(results)))
        results = set(results)
        depth = 0
        while results:
            path = os.path.join(*['dir'] + ['link'] * depth + [''])
            self.assertIn(path, results)
            results.remove(path)
            depth += 1
