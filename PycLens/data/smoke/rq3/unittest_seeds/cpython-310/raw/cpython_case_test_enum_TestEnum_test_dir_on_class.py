# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_dir_on_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Season = self.Season
    self.assertEqual(set(dir(Season)), set(['__class__', '__doc__', '__members__', '__module__', 'SPRING', 'SUMMER', 'AUTUMN', 'WINTER']))
