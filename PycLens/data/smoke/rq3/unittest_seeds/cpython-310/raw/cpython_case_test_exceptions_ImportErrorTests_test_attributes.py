# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ImportErrorTests_test_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exc = ImportError('test')
    self.assertIsNone(exc.name)
    self.assertIsNone(exc.path)
    exc = ImportError('test', name='somemodule')
    self.assertEqual(exc.name, 'somemodule')
    self.assertIsNone(exc.path)
    exc = ImportError('test', path='somepath')
    self.assertEqual(exc.path, 'somepath')
    self.assertIsNone(exc.name)
    exc = ImportError('test', path='somepath', name='somename')
    self.assertEqual(exc.name, 'somename')
    self.assertEqual(exc.path, 'somepath')
    msg = "'invalid' is an invalid keyword argument for ImportError"
    with self.assertRaisesRegex(TypeError, msg):
        ImportError('test', invalid='keyword')
    with self.assertRaisesRegex(TypeError, msg):
        ImportError('test', name='name', invalid='keyword')
    with self.assertRaisesRegex(TypeError, msg):
        ImportError('test', path='path', invalid='keyword')
    with self.assertRaisesRegex(TypeError, msg):
        ImportError(invalid='keyword')
    with self.assertRaisesRegex(TypeError, msg):
        ImportError('test', invalid='keyword', another=True)
