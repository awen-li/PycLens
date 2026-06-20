# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_linecache.py
# case: LineCacheTests_test_checkcache

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    getline = linecache.getline
    source_name = os_helper.TESTFN + '.py'
    self.addCleanup(os_helper.unlink, source_name)
    with open(source_name, 'w', encoding='utf-8') as source:
        source.write(SOURCE_1)
    getline(source_name, 1)
    source_list = []
    with open(source_name, encoding='utf-8') as source:
        for (index, line) in enumerate(source):
            self.assertEqual(line, getline(source_name, index + 1))
            source_list.append(line)
    with open(source_name, 'w', encoding='utf-8') as source:
        source.write(SOURCE_2)
    linecache.checkcache('dummy')
    for (index, line) in enumerate(source_list):
        self.assertEqual(line, getline(source_name, index + 1))
    linecache.checkcache(source_name)
    with open(source_name, encoding='utf-8') as source:
        for (index, line) in enumerate(source):
            self.assertEqual(line, getline(source_name, index + 1))
            source_list.append(line)
