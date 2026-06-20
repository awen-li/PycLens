# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_reverse_iterator_for_empty_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(reversed({})), [])
    self.assertEqual(list(reversed({}.items())), [])
    self.assertEqual(list(reversed({}.values())), [])
    self.assertEqual(list(reversed({}.keys())), [])
    self.assertEqual(list(reversed(dict())), [])
    self.assertEqual(list(reversed(dict().items())), [])
    self.assertEqual(list(reversed(dict().values())), [])
    self.assertEqual(list(reversed(dict().keys())), [])
