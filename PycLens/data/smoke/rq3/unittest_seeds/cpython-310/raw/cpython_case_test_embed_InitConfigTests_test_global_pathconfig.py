# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_global_pathconfig

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctypes = import_helper.import_module('ctypes')
    _testinternalcapi = import_helper.import_module('_testinternalcapi')

    def get_func(name):
        func = getattr(ctypes.pythonapi, name)
        func.argtypes = ()
        func.restype = ctypes.c_wchar_p
        return func
    Py_GetPath = get_func('Py_GetPath')
    Py_GetPrefix = get_func('Py_GetPrefix')
    Py_GetExecPrefix = get_func('Py_GetExecPrefix')
    Py_GetProgramName = get_func('Py_GetProgramName')
    Py_GetProgramFullPath = get_func('Py_GetProgramFullPath')
    Py_GetPythonHome = get_func('Py_GetPythonHome')
    config = _testinternalcapi.get_configs()['config']
    self.assertEqual(Py_GetPath().split(os.path.pathsep), config['module_search_paths'])
    self.assertEqual(Py_GetPrefix(), config['prefix'])
    self.assertEqual(Py_GetExecPrefix(), config['exec_prefix'])
    self.assertEqual(Py_GetProgramName(), config['program_name'])
    self.assertEqual(Py_GetProgramFullPath(), config['executable'])
    self.assertEqual(Py_GetPythonHome(), config['home'])
