# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_bug_1727780

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    files = [('randv2_32.pck', 780), ('randv2_64.pck', 866), ('randv3.pck', 343)]
    for (file, value) in files:
        with open(support.findfile(file), 'rb') as f:
            r = pickle.load(f)
        self.assertEqual(int(r.random() * 1000), value)
