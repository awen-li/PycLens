# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_choice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    choice = self.gen.choice
    with self.assertRaises(IndexError):
        choice([])
    self.assertEqual(choice([50]), 50)
    self.assertIn(choice([25, 75]), [25, 75])
