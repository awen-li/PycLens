# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_linecache.py
# case: LineCacheTests_test_no_ending_newline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    with open(os_helper.TESTFN, 'w', encoding='utf-8') as fp:
        fp.write(SOURCE_3)
    lines = linecache.getlines(os_helper.TESTFN)
    self.assertEqual(lines, ['\n', 'def f():\n', '    return 3\n'])
