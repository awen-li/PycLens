# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickle.py
# case: CompatPickleTests_test_reverse_name_mapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for ((module2, name2), (module3, name3)) in NAME_MAPPING.items():
        with self.subTest(((module2, name2), (module3, name3))):
            try:
                attr = getattribute(module3, name3)
            except ImportError:
                pass
            (module, name) = reverse_mapping(module3, name3)
            if (module2, name2, module3, name3) not in ALT_NAME_MAPPING:
                self.assertEqual((module, name), (module2, name2))
            (module, name) = mapping(module, name)
            self.assertEqual((module, name), (module3, name3))
