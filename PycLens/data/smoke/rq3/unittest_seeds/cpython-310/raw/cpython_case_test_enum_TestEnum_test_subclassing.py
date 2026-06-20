# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_subclassing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if isinstance(Name, Exception):
        raise Name
    self.assertEqual(Name.BDFL, 'Guido van Rossum')
    self.assertTrue(Name.BDFL, Name('Guido van Rossum'))
    self.assertIs(Name.BDFL, getattr(Name, 'BDFL'))
    test_pickle_dump_load(self.assertIs, Name.BDFL)
