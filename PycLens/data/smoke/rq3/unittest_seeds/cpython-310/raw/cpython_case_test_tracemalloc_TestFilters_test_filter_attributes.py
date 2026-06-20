# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestFilters_test_filter_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = tracemalloc.Filter(True, 'abc')
    self.assertEqual(f.inclusive, True)
    self.assertEqual(f.filename_pattern, 'abc')
    self.assertIsNone(f.lineno)
    self.assertEqual(f.all_frames, False)
    f = tracemalloc.Filter(False, 'test.py', 123, True)
    self.assertEqual(f.inclusive, False)
    self.assertEqual(f.filename_pattern, 'test.py')
    self.assertEqual(f.lineno, 123)
    self.assertEqual(f.all_frames, True)
    f = tracemalloc.Filter(inclusive=False, filename_pattern='test.py', lineno=123, all_frames=True)
    self.assertEqual(f.inclusive, False)
    self.assertEqual(f.filename_pattern, 'test.py')
    self.assertEqual(f.lineno, 123)
    self.assertEqual(f.all_frames, True)
    self.assertRaises(AttributeError, setattr, f, 'filename_pattern', 'abc')
