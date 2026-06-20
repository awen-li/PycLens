# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_pythonmalloc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pymalloc = support.with_pymalloc()
    if pymalloc:
        default_name = 'pymalloc_debug' if Py_DEBUG else 'pymalloc'
        default_name_debug = 'pymalloc_debug'
    else:
        default_name = 'malloc_debug' if Py_DEBUG else 'malloc'
        default_name_debug = 'malloc_debug'
    tests = [(None, default_name), ('debug', default_name_debug), ('malloc', 'malloc'), ('malloc_debug', 'malloc_debug')]
    if pymalloc:
        tests.extend((('pymalloc', 'pymalloc'), ('pymalloc_debug', 'pymalloc_debug')))
    for (env_var, name) in tests:
        with self.subTest(env_var=env_var, name=name):
            self.check_pythonmalloc(env_var, name)
