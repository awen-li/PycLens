# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_issue31315

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    create_dynamic = support.get_attribute(imp, 'create_dynamic')

    class BadSpec:
        name = None
        origin = 'foo'
    with self.assertRaises(TypeError):
        create_dynamic(BadSpec())
