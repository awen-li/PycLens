# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_getfullargspec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFullArgSpecEquals(mod2.keyworded, [], varargs_e='arg1', kwonlyargs_e=['arg2'], kwonlydefaults_e={'arg2': 1}, formatted='(*arg1, arg2=1)')
    self.assertFullArgSpecEquals(mod2.annotated, ['arg1'], ann_e={'arg1': list}, formatted='(arg1: list)')
    self.assertFullArgSpecEquals(mod2.keyword_only_arg, [], kwonlyargs_e=['arg'], formatted='(*, arg)')
    self.assertFullArgSpecEquals(mod2.all_markers, ['a', 'b', 'c', 'd'], kwonlyargs_e=['e', 'f'], formatted='(a, b, c, d, *, e, f)')
    self.assertFullArgSpecEquals(mod2.all_markers_with_args_and_kwargs, ['a', 'b', 'c', 'd'], varargs_e='args', varkw_e='kwargs', kwonlyargs_e=['e', 'f'], formatted='(a, b, c, d, *args, e, f, **kwargs)')
    self.assertFullArgSpecEquals(mod2.all_markers_with_defaults, ['a', 'b', 'c', 'd'], defaults_e=(1, 2, 3), kwonlyargs_e=['e', 'f'], kwonlydefaults_e={'e': 4, 'f': 5}, formatted='(a, b=1, c=2, d=3, *, e=4, f=5)')
