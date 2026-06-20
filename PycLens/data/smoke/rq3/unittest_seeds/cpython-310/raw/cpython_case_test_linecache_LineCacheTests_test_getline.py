# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_linecache.py
# case: LineCacheTests_test_getline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    getline = linecache.getline
    self.assertEqual(getline(FILENAME, 2 ** 15), EMPTY)
    self.assertEqual(getline(FILENAME, -1), EMPTY)
    self.assertRaises(TypeError, getline, FILENAME, 1.1)
    self.assertEqual(getline(EMPTY, 1), EMPTY)
    self.assertEqual(getline(INVALID_NAME, 1), EMPTY)
    for entry in MODULES:
        filename = os.path.join(MODULE_PATH, entry) + '.py'
        with open(filename, encoding='utf-8') as file:
            for (index, line) in enumerate(file):
                self.assertEqual(line, getline(filename, index + 1))
    empty = linecache.getlines('a/b/c/__init__.py')
    self.assertEqual(empty, [])
