# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: ReprTestCase_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(os.path.join(os.path.split(__file__)[0], 'floating_points.txt'), encoding='utf-8') as floats_file:
        for line in floats_file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            v = eval(line)
            self.assertEqual(v, eval(repr(v)))
