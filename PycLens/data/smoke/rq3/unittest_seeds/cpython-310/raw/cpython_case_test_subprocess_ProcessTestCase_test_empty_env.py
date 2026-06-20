# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_empty_env

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def is_env_var_to_ignore(n):
        """Determine if an environment variable is under our control."""
        return 'VERSIONER' in n or '__CF' in n or n == 'LD_PRELOAD' or n.startswith('SANDBOX') or (n == 'LC_CTYPE')
    with subprocess.Popen([sys.executable, '-c', 'import os; print(list(os.environ.keys()))'], stdout=subprocess.PIPE, env={}) as p:
        (stdout, stderr) = p.communicate()
        child_env_names = eval(stdout.strip())
        self.assertIsInstance(child_env_names, list)
        child_env_names = [k for k in child_env_names if not is_env_var_to_ignore(k)]
        self.assertEqual(child_env_names, [])
