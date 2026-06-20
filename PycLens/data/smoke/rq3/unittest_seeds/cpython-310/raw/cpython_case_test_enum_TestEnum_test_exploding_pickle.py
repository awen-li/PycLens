# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_exploding_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    BadPickle = Enum('BadPickle', 'dill sweet bread-n-butter', module=__name__)
    globals()['BadPickle'] = BadPickle
    enum._make_class_unpicklable(BadPickle)
    test_pickle_exception(self.assertRaises, TypeError, BadPickle.dill)
    test_pickle_exception(self.assertRaises, PicklingError, BadPickle)
