# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_namedtuple_subclass_issue_24931

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Point(namedtuple('_Point', ['x', 'y'])):
        pass
    a = Point(3, 4)
    self.assertEqual(a._asdict(), OrderedDict([('x', 3), ('y', 4)]))
    a.w = 5
    self.assertEqual(a.__dict__, {'w': 5})
