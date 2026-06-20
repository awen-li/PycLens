# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: WalkTests_test_walk_prune

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if walk_path is None:
        walk_path = self.walk_path
    all = []
    for (root, dirs, files) in self.walk(walk_path):
        all.append((root, dirs, files))
        if 'SUB1' in dirs:
            dirs.remove('SUB1')
    self.assertEqual(len(all), 2)
    self.assertEqual(all[0], (self.walk_path, ['SUB2'], ['tmp1']))
    all[1][-1].sort()
    all[1][1].sort()
    self.assertEqual(all[1], self.sub2_tree)
