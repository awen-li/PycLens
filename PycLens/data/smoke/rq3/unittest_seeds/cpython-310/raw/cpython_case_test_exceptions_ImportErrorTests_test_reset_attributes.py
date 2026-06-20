# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ImportErrorTests_test_reset_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exc = ImportError('test', name='name', path='path')
    self.assertEqual(exc.args, ('test',))
    self.assertEqual(exc.msg, 'test')
    self.assertEqual(exc.name, 'name')
    self.assertEqual(exc.path, 'path')
    exc.__init__()
    self.assertEqual(exc.args, ())
    self.assertEqual(exc.msg, None)
    self.assertEqual(exc.name, None)
    self.assertEqual(exc.path, None)
