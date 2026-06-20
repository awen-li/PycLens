# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: WalkTests_test_walk_bad_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    errors = []
    walk_it = self.walk(self.walk_path, onerror=errors.append)
    (root, dirs, files) = next(walk_it)
    self.assertEqual(errors, [])
    dir1 = 'SUB1'
    path1 = os.path.join(root, dir1)
    path1new = os.path.join(root, dir1 + '.new')
    os.rename(path1, path1new)
    try:
        roots = [r for (r, d, f) in walk_it]
        self.assertTrue(errors)
        self.assertNotIn(path1, roots)
        self.assertNotIn(path1new, roots)
        for dir2 in dirs:
            if dir2 != dir1:
                self.assertIn(os.path.join(root, dir2), roots)
    finally:
        os.rename(path1new, path1)
