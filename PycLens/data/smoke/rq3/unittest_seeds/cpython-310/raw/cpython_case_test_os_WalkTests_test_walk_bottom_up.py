# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: WalkTests_test_walk_bottom_up

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    all = list(self.walk(self.walk_path, topdown=False))
    self.assertEqual(len(all), 4, all)
    flipped = all[3][1][0] != 'SUB1'
    all[3][1].sort()
    all[2 - 2 * flipped][-1].sort()
    all[2 - 2 * flipped][1].sort()
    self.assertEqual(all[3], (self.walk_path, ['SUB1', 'SUB2'], ['tmp1']))
    self.assertEqual(all[flipped], (self.sub11_path, [], []))
    self.assertEqual(all[flipped + 1], (self.sub1_path, ['SUB11'], ['tmp2']))
    self.assertEqual(all[2 - 2 * flipped], self.sub2_tree)
