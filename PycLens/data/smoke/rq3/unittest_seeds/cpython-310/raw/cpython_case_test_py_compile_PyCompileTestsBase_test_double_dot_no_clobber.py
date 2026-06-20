# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileTestsBase_test_double_dot_no_clobber

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    weird_path = os.path.join(self.directory, 'foo.bar.py')
    cache_path = importlib.util.cache_from_source(weird_path)
    pyc_path = weird_path + 'c'
    (head, tail) = os.path.split(cache_path)
    penultimate_tail = os.path.basename(head)
    self.assertEqual(os.path.join(penultimate_tail, tail), os.path.join('__pycache__', 'foo.bar.{}.pyc'.format(sys.implementation.cache_tag)))
    with open(weird_path, 'w') as file:
        file.write('x = 123\n')
    py_compile.compile(weird_path)
    self.assertTrue(os.path.exists(cache_path))
    self.assertFalse(os.path.exists(pyc_path))
