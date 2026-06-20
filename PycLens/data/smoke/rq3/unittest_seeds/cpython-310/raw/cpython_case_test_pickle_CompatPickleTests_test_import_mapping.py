# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickle.py
# case: CompatPickleTests_test_import_mapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (module3, module2) in REVERSE_IMPORT_MAPPING.items():
        with self.subTest((module3, module2)):
            try:
                getmodule(module3)
            except ImportError:
                pass
            if module3[:1] != '_':
                self.assertIn(module2, IMPORT_MAPPING)
                self.assertEqual(IMPORT_MAPPING[module2], module3)
