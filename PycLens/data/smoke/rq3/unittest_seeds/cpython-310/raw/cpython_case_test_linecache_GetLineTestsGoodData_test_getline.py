# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_linecache.py
# case: GetLineTestsGoodData_test_getline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tokenize.open(self.file_name) as fp:
        for (index, line) in enumerate(fp):
            if not line.endswith('\n'):
                line += '\n'
            cached_line = linecache.getline(self.file_name, index + 1)
            self.assertEqual(line, cached_line)
