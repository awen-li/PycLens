# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickle.py
# case: CompatPickleTests_test_multiprocessing_exceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    module = import_helper.import_module('multiprocessing.context')
    for (name, exc) in get_exceptions(module):
        with self.subTest(name):
            self.assertEqual(reverse_mapping('multiprocessing.context', name), ('multiprocessing', name))
            self.assertEqual(mapping('multiprocessing', name), ('multiprocessing.context', name))
