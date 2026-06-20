# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: SortedTestCase_test_sorted

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.fromstring('[b]\no4=1\no3=2\no2=3\no1=4\n[a]\nk=v\n')
    output = io.StringIO()
    cf.write(output)
    self.assertEqual(output.getvalue(), '[a]\nk = v\n\n[b]\no1 = 4\no2 = 3\no3 = 2\no4 = 1\n\n')
