# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_set_operations_with_iterator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    origin = {1: 2, 3: 4}
    self.assertEqual(origin.keys() & iter([1, 2]), {1})
    self.assertEqual(origin.keys() | iter([1, 2]), {1, 2, 3})
    self.assertEqual(origin.keys() ^ iter([1, 2]), {2, 3})
    self.assertEqual(origin.keys() - iter([1, 2]), {3})
    items = origin.items()
    self.assertEqual(items & iter([(1, 2)]), {(1, 2)})
    self.assertEqual(items ^ iter([(1, 2)]), {(3, 4)})
    self.assertEqual(items | iter([(1, 2)]), {(1, 2), (3, 4)})
    self.assertEqual(items - iter([(1, 2)]), {(3, 4)})
