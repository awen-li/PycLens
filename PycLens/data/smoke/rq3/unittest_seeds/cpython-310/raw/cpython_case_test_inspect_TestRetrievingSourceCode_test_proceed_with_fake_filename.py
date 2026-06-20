# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_proceed_with_fake_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (fn, source) = ('<test>', 'def x(): pass\n')
    getlines = linecache.getlines

    def monkey(filename, module_globals=None):
        if filename == fn:
            return source.splitlines(keepends=True)
        else:
            return getlines(filename, module_globals)
    linecache.getlines = monkey
    try:
        ns = {}
        exec(compile(source, fn, 'single'), ns)
        inspect.getsource(ns['x'])
    finally:
        linecache.getlines = getlines
