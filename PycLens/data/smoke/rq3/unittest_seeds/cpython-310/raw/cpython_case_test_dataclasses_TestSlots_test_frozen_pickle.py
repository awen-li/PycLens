# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestSlots_test_frozen_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.FrozenSlotsClass.__slots__, ('foo', 'bar'))
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.subTest(proto=proto):
            obj = self.FrozenSlotsClass('a', 1)
            p = pickle.loads(pickle.dumps(obj, protocol=proto))
            self.assertIsNot(obj, p)
            self.assertEqual(obj, p)
            obj = self.FrozenWithoutSlotsClass('a', 1)
            p = pickle.loads(pickle.dumps(obj, protocol=proto))
            self.assertIsNot(obj, p)
            self.assertEqual(obj, p)
