# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_dict_subscribe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    K = TypeVar('K')
    V = TypeVar('V')
    self.assertEqual(Dict[K, V][str, int], Dict[str, int])
    self.assertEqual(Dict[K, int][str], Dict[str, int])
    self.assertEqual(Dict[str, V][int], Dict[str, int])
    self.assertEqual(Dict[K, List[V]][str, int], Dict[str, List[int]])
    self.assertEqual(Dict[K, List[int]][str], Dict[str, List[int]])
    self.assertEqual(Dict[K, list[V]][str, int], Dict[str, list[int]])
    self.assertEqual(Dict[K, list[int]][str], Dict[str, list[int]])
