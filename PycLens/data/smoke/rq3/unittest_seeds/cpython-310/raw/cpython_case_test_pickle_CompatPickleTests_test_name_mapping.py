# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickle.py
# case: CompatPickleTests_test_name_mapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for ((module3, name3), (module2, name2)) in REVERSE_NAME_MAPPING.items():
        with self.subTest(((module3, name3), (module2, name2))):
            if (module2, name2) == ('exceptions', 'OSError'):
                attr = getattribute(module3, name3)
                self.assertTrue(issubclass(attr, OSError))
            elif (module2, name2) == ('exceptions', 'ImportError'):
                attr = getattribute(module3, name3)
                self.assertTrue(issubclass(attr, ImportError))
            else:
                (module, name) = mapping(module2, name2)
                if module3[:1] != '_':
                    self.assertEqual((module, name), (module3, name3))
                try:
                    attr = getattribute(module3, name3)
                except ImportError:
                    pass
                else:
                    self.assertEqual(getattribute(module, name), attr)
