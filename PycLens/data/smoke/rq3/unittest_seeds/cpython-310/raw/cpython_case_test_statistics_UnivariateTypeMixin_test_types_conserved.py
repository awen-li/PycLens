# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: UnivariateTypeMixin_test_types_conserved

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = self.prepare_data()
    for kind in self.prepare_types_for_conservation_test():
        d = [kind(x) for x in data]
        result = self.func(d)
        self.assertIs(type(result), kind)
