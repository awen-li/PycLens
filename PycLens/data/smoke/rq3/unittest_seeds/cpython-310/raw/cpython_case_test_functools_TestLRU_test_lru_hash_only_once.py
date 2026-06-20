# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_hash_only_once

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @self.module.lru_cache(maxsize=1)
    def f(x, y):
        return x * 3 + y
    mock_int = unittest.mock.Mock()
    mock_int.__mul__ = unittest.mock.Mock(return_value=15)
    mock_int.__hash__ = unittest.mock.Mock(return_value=999)
    self.assertEqual(f(mock_int, 1), 16)
    self.assertEqual(mock_int.__hash__.call_count, 1)
    self.assertEqual(f.cache_info(), (0, 1, 1, 1))
    self.assertEqual(f(mock_int, 1), 16)
    self.assertEqual(mock_int.__hash__.call_count, 2)
    self.assertEqual(f.cache_info(), (1, 1, 1, 1))
    self.assertEqual(f(6, 2), 20)
    self.assertEqual(mock_int.__hash__.call_count, 2)
    self.assertEqual(f.cache_info(), (1, 2, 1, 1))
    self.assertEqual(f(mock_int, 1), 16)
    self.assertEqual(mock_int.__hash__.call_count, 3)
    self.assertEqual(f.cache_info(), (1, 3, 1, 1))
