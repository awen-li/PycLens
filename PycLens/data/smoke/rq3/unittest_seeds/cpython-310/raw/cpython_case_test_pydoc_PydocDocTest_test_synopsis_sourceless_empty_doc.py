# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_synopsis_sourceless_empty_doc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_cwd() as test_dir:
        init_path = os.path.join(test_dir, 'foomod42.py')
        cached_path = importlib.util.cache_from_source(init_path)
        with open(init_path, 'w') as fobj:
            fobj.write('foo = 1')
        py_compile.compile(init_path)
        synopsis = pydoc.synopsis(init_path, {})
        self.assertIsNone(synopsis)
        synopsis_cached = pydoc.synopsis(cached_path, {})
        self.assertIsNone(synopsis_cached)
