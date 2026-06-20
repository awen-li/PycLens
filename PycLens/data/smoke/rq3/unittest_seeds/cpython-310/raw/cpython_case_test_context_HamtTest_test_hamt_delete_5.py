# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hamt_delete_5

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = hamt()
    keys = []
    for i in range(17):
        key = HashKey(i, str(i))
        keys.append(key)
        h = h.set(key, f'val-{i}')
    collision_key16 = HashKey(16, '18')
    h = h.set(collision_key16, 'collision')
    self.assertEqual(len(h), 18)
    h = h.delete(keys[2])
    self.assertEqual(len(h), 17)
    h = h.delete(collision_key16)
    self.assertEqual(len(h), 16)
    h = h.delete(keys[16])
    self.assertEqual(len(h), 15)
    h = h.delete(keys[1])
    self.assertEqual(len(h), 14)
    h = h.delete(keys[1])
    self.assertEqual(len(h), 14)
    for key in keys:
        h = h.delete(key)
    self.assertEqual(len(h), 0)
