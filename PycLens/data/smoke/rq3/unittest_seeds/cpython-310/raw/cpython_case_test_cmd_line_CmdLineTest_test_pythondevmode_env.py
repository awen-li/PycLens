# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_pythondevmode_env

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import sys; print(sys.flags.dev_mode)'
    env = dict(os.environ)
    env.pop('PYTHONDEVMODE', None)
    args = (sys.executable, '-c', code)
    proc = subprocess.run(args, stdout=subprocess.PIPE, universal_newlines=True, env=env)
    self.assertEqual(proc.stdout.rstrip(), 'False')
    self.assertEqual(proc.returncode, 0, proc)
    env['PYTHONDEVMODE'] = '1'
    proc = subprocess.run(args, stdout=subprocess.PIPE, universal_newlines=True, env=env)
    self.assertEqual(proc.stdout.rstrip(), 'True')
    self.assertEqual(proc.returncode, 0, proc)
