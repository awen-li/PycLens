# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_methods_in_c

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    set_add = set.add
    expected_errmsg = 'unbound method set.add() needs an argument'
    with self.assertRaises(TypeError) as cm:
        set_add()
    self.assertEqual(cm.exception.args[0], expected_errmsg)
    expected_errmsg = "descriptor 'add' for 'set' objects doesn't apply to a 'int' object"
    with self.assertRaises(TypeError) as cm:
        set_add(0)
    self.assertEqual(cm.exception.args[0], expected_errmsg)
    with self.assertRaises(TypeError) as cm:
        set_add.__get__(0)
    self.assertEqual(cm.exception.args[0], expected_errmsg)
