# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_reentrant_insertion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def mutate(d):
        d['b'] = 5
    self.check_reentrant_insertion(mutate)

    def mutate(d):
        d.update(self.__dict__)
        d.clear()
    self.check_reentrant_insertion(mutate)

    def mutate(d):
        while d:
            d.popitem()
    self.check_reentrant_insertion(mutate)
