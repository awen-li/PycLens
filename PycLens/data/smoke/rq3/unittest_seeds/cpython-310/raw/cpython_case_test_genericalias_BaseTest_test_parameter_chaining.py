# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_parameter_chaining

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from typing import List, Dict, Union, Callable
    self.assertEqual(list[T][int], list[int])
    self.assertEqual(dict[str, T][int], dict[str, int])
    self.assertEqual(dict[T, int][str], dict[str, int])
    self.assertEqual(dict[K, V][str, int], dict[str, int])
    self.assertEqual(dict[T, T][int], dict[int, int])
    self.assertEqual(list[list[T]][int], list[list[int]])
    self.assertEqual(list[dict[T, int]][str], list[dict[str, int]])
    self.assertEqual(list[dict[str, T]][int], list[dict[str, int]])
    self.assertEqual(list[dict[K, V]][str, int], list[dict[str, int]])
    self.assertEqual(dict[T, list[int]][str], dict[str, list[int]])
    self.assertEqual(list[List[T]][int], list[List[int]])
    self.assertEqual(list[Dict[K, V]][str, int], list[Dict[str, int]])
    self.assertEqual(list[Union[K, V]][str, int], list[Union[str, int]])
    self.assertEqual(list[Callable[[K, V], K]][str, int], list[Callable[[str, int], str]])
    self.assertEqual(dict[T, List[int]][str], dict[str, List[int]])
    with self.assertRaises(TypeError):
        list[int][int]
        dict[T, int][str, int]
        dict[str, T][str, int]
        dict[T, T][str, int]
