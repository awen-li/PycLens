# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_meth_class_get

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    arg = [1, 2, 3]
    res = {1: None, 2: None, 3: None}
    self.assertEqual(dict.fromkeys(arg), res)
    self.assertEqual({}.fromkeys(arg), res)
    descr = dict.__dict__['fromkeys']
    self.assertEqual(descr.__get__(None, dict)(arg), res)
    self.assertEqual(descr.__get__({})(arg), res)
    try:
        descr.__get__(None, None)
    except TypeError:
        pass
    else:
        self.fail("shouldn't have allowed descr.__get__(None, None)")
    try:
        descr.__get__(42)
    except TypeError:
        pass
    else:
        self.fail("shouldn't have allowed descr.__get__(42)")
    try:
        descr.__get__(None, 42)
    except TypeError:
        pass
    else:
        self.fail("shouldn't have allowed descr.__get__(None, 42)")
    try:
        descr.__get__(None, int)
    except TypeError:
        pass
    else:
        self.fail("shouldn't have allowed descr.__get__(None, int)")
