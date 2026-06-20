# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_parameters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from typing import List, Dict, Callable
    D0 = dict[str, int]
    self.assertEqual(D0.__args__, (str, int))
    self.assertEqual(D0.__parameters__, ())
    D1a = dict[str, V]
    self.assertEqual(D1a.__args__, (str, V))
    self.assertEqual(D1a.__parameters__, (V,))
    D1b = dict[K, int]
    self.assertEqual(D1b.__args__, (K, int))
    self.assertEqual(D1b.__parameters__, (K,))
    D2a = dict[K, V]
    self.assertEqual(D2a.__args__, (K, V))
    self.assertEqual(D2a.__parameters__, (K, V))
    D2b = dict[T, T]
    self.assertEqual(D2b.__args__, (T, T))
    self.assertEqual(D2b.__parameters__, (T,))
    L0 = list[str]
    self.assertEqual(L0.__args__, (str,))
    self.assertEqual(L0.__parameters__, ())
    L1 = list[T]
    self.assertEqual(L1.__args__, (T,))
    self.assertEqual(L1.__parameters__, (T,))
    L2 = list[list[T]]
    self.assertEqual(L2.__args__, (list[T],))
    self.assertEqual(L2.__parameters__, (T,))
    L3 = list[List[T]]
    self.assertEqual(L3.__args__, (List[T],))
    self.assertEqual(L3.__parameters__, (T,))
    L4a = list[Dict[K, V]]
    self.assertEqual(L4a.__args__, (Dict[K, V],))
    self.assertEqual(L4a.__parameters__, (K, V))
    L4b = list[Dict[T, int]]
    self.assertEqual(L4b.__args__, (Dict[T, int],))
    self.assertEqual(L4b.__parameters__, (T,))
    L5 = list[Callable[[K, V], K]]
    self.assertEqual(L5.__args__, (Callable[[K, V], K],))
    self.assertEqual(L5.__parameters__, (K, V))
