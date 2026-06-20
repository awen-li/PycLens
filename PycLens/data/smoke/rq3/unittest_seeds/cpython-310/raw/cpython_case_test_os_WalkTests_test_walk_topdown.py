# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: WalkTests_test_walk_topdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    all = list(self.walk(self.walk_path))
    self.assertEqual(len(all), 4)
    flipped = all[0][1][0] != 'SUB1'
    all[0][1].sort()
    all[3 - 2 * flipped][-1].sort()
    all[3 - 2 * flipped][1].sort()
    self.assertEqual(all[0], (self.walk_path, ['SUB1', 'SUB2'], ['tmp1']))
    self.assertEqual(all[1 + flipped], (self.sub1_path, ['SUB11'], ['tmp2']))
    self.assertEqual(all[2 + flipped], (self.sub11_path, [], []))
    self.assertEqual(all[3 - 2 * flipped], self.sub2_tree)
