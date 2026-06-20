# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_bound_builtin_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = StringIO()
    p = _pickle.Pickler(s)
    self.assertEqual(self._get_summary_line(p.dump), 'dump(obj, /) method of _pickle.Pickler instance')
