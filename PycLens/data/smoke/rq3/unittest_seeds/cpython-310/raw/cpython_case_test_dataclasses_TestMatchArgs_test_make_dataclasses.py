# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMatchArgs_test_make_dataclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = make_dataclass('C', [('x', int), ('y', int)])
    self.assertEqual(C.__match_args__, ('x', 'y'))
    C = make_dataclass('C', [('x', int), ('y', int)], match_args=True)
    self.assertEqual(C.__match_args__, ('x', 'y'))
    C = make_dataclass('C', [('x', int), ('y', int)], match_args=False)
    self.assertNotIn('__match__args__', C.__dict__)
    C = make_dataclass('C', [('x', int), ('y', int)], namespace={'__match_args__': ('z',)})
    self.assertEqual(C.__match_args__, ('z',))
