# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ExecTests_test_execve_invalid_env

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = [sys.executable, '-c', 'pass']
    newenv = os.environ.copy()
    newenv['FRUIT\x00VEGETABLE'] = 'cabbage'
    with self.assertRaises(ValueError):
        os.execve(args[0], args, newenv)
    newenv = os.environ.copy()
    newenv['FRUIT'] = 'orange\x00VEGETABLE=cabbage'
    with self.assertRaises(ValueError):
        os.execve(args[0], args, newenv)
    newenv = os.environ.copy()
    newenv['FRUIT=ORANGE'] = 'lemon'
    with self.assertRaises(ValueError):
        os.execve(args[0], args, newenv)
