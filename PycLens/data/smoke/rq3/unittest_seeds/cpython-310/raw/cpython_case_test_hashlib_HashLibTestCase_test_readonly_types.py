# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_readonly_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (algorithm, constructors) in self.constructors_to_test.items():
        for constructor in constructors:
            try:
                hash_type = type(constructor())
            except ValueError:
                continue
            with self.subTest(hash_type=hash_type):
                with self.assertRaisesRegex(TypeError, 'immutable type'):
                    hash_type.value = False
