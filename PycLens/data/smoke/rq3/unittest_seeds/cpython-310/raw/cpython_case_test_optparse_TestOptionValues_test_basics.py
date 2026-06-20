# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionValues_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    values = Values()
    self.assertEqual(vars(values), {})
    self.assertEqual(values, {})
    self.assertNotEqual(values, {'foo': 'bar'})
    self.assertNotEqual(values, '')
    dict = {'foo': 'bar', 'baz': 42}
    values = Values(defaults=dict)
    self.assertEqual(vars(values), dict)
    self.assertEqual(values, dict)
    self.assertNotEqual(values, {'foo': 'bar'})
    self.assertNotEqual(values, {})
    self.assertNotEqual(values, '')
    self.assertNotEqual(values, [])
