# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: WalkTests_test_walk_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not os_helper.can_symlink():
        self.skipTest('need symlink support')
    walk_it = self.walk(self.walk_path, follow_symlinks=True)
    for (root, dirs, files) in walk_it:
        if root == self.link_path:
            self.assertEqual(dirs, [])
            self.assertEqual(files, ['tmp4'])
            break
    else:
        self.fail("Didn't follow symlink with followlinks=True")
