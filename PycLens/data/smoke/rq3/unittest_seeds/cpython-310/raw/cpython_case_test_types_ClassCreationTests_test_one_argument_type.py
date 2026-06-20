# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_one_argument_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_message = 'type.__new__() takes exactly 3 arguments (1 given)'
    self.assertIs(type(5), int)

    class M(type):
        pass
    with self.assertRaises(TypeError) as cm:
        M(5)
    self.assertEqual(str(cm.exception), expected_message)

    class N(type, metaclass=M):
        pass
    with self.assertRaises(TypeError) as cm:
        N(5)
    self.assertEqual(str(cm.exception), expected_message)
