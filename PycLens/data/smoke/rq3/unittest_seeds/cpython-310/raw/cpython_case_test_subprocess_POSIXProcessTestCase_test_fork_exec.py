# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_fork_exec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _posixsubprocess
    gc_enabled = gc.isenabled()
    try:
        func = lambda : None
        gc.enable()
        for (args, exe_list, cwd, env_list) in ((123, [b'exe'], None, [b'env']), ([b'arg'], 123, None, [b'env']), ([b'arg'], [b'exe'], 123, [b'env']), ([b'arg'], [b'exe'], None, 123)):
            with self.assertRaises(TypeError) as err:
                _posixsubprocess.fork_exec(args, exe_list, True, (), cwd, env_list, -1, -1, -1, -1, 1, 2, 3, 4, True, True, False, [], 0, -1, func)
            self.assertNotIn('takes exactly', str(err.exception))
    finally:
        if not gc_enabled:
            gc.disable()
