# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EnvironTests_test_get_exec_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    defpath_list = os.defpath.split(os.pathsep)
    test_path = ['/monty', '/python', '', '/flying/circus']
    test_env = {'PATH': os.pathsep.join(test_path)}
    saved_environ = os.environ
    try:
        os.environ = dict(test_env)
        self.assertSequenceEqual(test_path, os.get_exec_path())
        self.assertSequenceEqual(test_path, os.get_exec_path(env=None))
    finally:
        os.environ = saved_environ
    self.assertSequenceEqual(defpath_list, os.get_exec_path({}))
    self.assertSequenceEqual(('',), os.get_exec_path({'PATH': ''}))
    self.assertSequenceEqual(test_path, os.get_exec_path(test_env))
    if os.supports_bytes_environ:
        try:
            with warnings.catch_warnings(record=True):
                mixed_env = {'PATH': '1', b'PATH': b'2'}
        except BytesWarning:
            pass
        else:
            self.assertRaises(ValueError, os.get_exec_path, mixed_env)
        self.assertSequenceEqual(os.get_exec_path({b'PATH': b'abc'}), ['abc'])
        self.assertSequenceEqual(os.get_exec_path({b'PATH': 'abc'}), ['abc'])
        self.assertSequenceEqual(os.get_exec_path({'PATH': b'abc'}), ['abc'])
