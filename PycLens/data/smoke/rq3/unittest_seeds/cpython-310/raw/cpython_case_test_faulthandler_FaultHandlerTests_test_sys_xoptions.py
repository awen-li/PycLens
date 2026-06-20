# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_sys_xoptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import faulthandler; print(faulthandler.is_enabled())'
    args = filter(None, (sys.executable, '-E' if sys.flags.ignore_environment else '', '-X', 'faulthandler', '-c', code))
    env = os.environ.copy()
    env.pop('PYTHONFAULTHANDLER', None)
    output = subprocess.check_output(args, env=env)
    self.assertEqual(output.rstrip(), b'True')
