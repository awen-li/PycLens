# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ImportErrorTests_test_copy_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for kwargs in (dict(), dict(name='somename'), dict(path='somepath'), dict(name='somename', path='somepath')):
        orig = ImportError('test', **kwargs)
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            exc = pickle.loads(pickle.dumps(orig, proto))
            self.assertEqual(exc.args, ('test',))
            self.assertEqual(exc.msg, 'test')
            self.assertEqual(exc.name, orig.name)
            self.assertEqual(exc.path, orig.path)
        for c in (copy.copy, copy.deepcopy):
            exc = c(orig)
            self.assertEqual(exc.args, ('test',))
            self.assertEqual(exc.msg, 'test')
            self.assertEqual(exc.name, orig.name)
            self.assertEqual(exc.path, orig.path)
