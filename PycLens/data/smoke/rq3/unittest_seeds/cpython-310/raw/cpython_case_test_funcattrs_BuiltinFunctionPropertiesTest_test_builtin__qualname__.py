# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: BuiltinFunctionPropertiesTest_test_builtin__qualname__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import time
    self.assertEqual(len.__qualname__, 'len')
    self.assertEqual(time.time.__qualname__, 'time')
    self.assertEqual(dict.fromkeys.__qualname__, 'dict.fromkeys')
    self.assertEqual(float.__getformat__.__qualname__, 'float.__getformat__')
    self.assertEqual(str.maketrans.__qualname__, 'str.maketrans')
    self.assertEqual(bytes.maketrans.__qualname__, 'bytes.maketrans')
    self.assertEqual([1, 2, 3].append.__qualname__, 'list.append')
    self.assertEqual({'foo': 'bar'}.pop.__qualname__, 'dict.pop')
