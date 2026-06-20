# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_env_var

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import faulthandler; print(faulthandler.is_enabled())'
    args = (sys.executable, '-c', code)
    env = dict(os.environ)
    env['PYTHONFAULTHANDLER'] = ''
    env['PYTHONDEVMODE'] = ''
    output = subprocess.check_output(args, env=env)
    self.assertEqual(output.rstrip(), b'False')
    env = dict(os.environ)
    env['PYTHONFAULTHANDLER'] = '1'
    env['PYTHONDEVMODE'] = ''
    output = subprocess.check_output(args, env=env)
    self.assertEqual(output.rstrip(), b'True')
