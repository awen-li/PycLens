# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_chain_setstate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, chain().__setstate__, ())
    self.assertRaises(TypeError, chain().__setstate__, [])
    self.assertRaises(TypeError, chain().__setstate__, 0)
    self.assertRaises(TypeError, chain().__setstate__, ([],))
    self.assertRaises(TypeError, chain().__setstate__, (iter([]), []))
    it = chain()
    it.__setstate__((iter(['abc', 'def']),))
    self.assertEqual(list(it), ['a', 'b', 'c', 'd', 'e', 'f'])
    it = chain()
    it.__setstate__((iter(['abc', 'def']), iter(['ghi'])))
    self.assertEqual(list(it), ['ghi', 'a', 'b', 'c', 'd', 'e', 'f'])
