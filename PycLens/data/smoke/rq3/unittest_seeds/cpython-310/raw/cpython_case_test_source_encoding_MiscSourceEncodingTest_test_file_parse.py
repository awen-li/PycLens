# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_source_encoding.py
# case: MiscSourceEncodingTest_test_file_parse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    unload(TESTFN)
    filename = TESTFN + '.py'
    f = open(filename, 'w', encoding='cp1252')
    sys.path.insert(0, os.curdir)
    try:
        with f:
            f.write('# -*- coding: cp1252 -*-\n')
            f.write("'''A short string\n")
            f.write("'''\n")
            f.write("'A very long string %s'\n" % ('X' * 1000))
        importlib.invalidate_caches()
        __import__(TESTFN)
    finally:
        del sys.path[0]
        unlink(filename)
        unlink(filename + 'c')
        unlink(filename + 'o')
        unload(TESTFN)
        rmtree('__pycache__')
