# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_getfullargspec_builtin_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFullArgSpecEquals(_pickle.Pickler.dump, ['self', 'obj'], formatted='(self, obj)')
    self.assertFullArgSpecEquals(_pickle.Pickler(io.BytesIO()).dump, ['self', 'obj'], formatted='(self, obj)')
    self.assertFullArgSpecEquals(os.stat, args_e=['path'], kwonlyargs_e=['dir_fd', 'follow_symlinks'], kwonlydefaults_e={'dir_fd': None, 'follow_symlinks': True}, formatted='(path, *, dir_fd=None, follow_symlinks=True)')
