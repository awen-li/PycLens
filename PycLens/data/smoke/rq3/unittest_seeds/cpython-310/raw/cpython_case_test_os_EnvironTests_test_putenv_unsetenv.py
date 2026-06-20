# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EnvironTests_test_putenv_unsetenv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = 'PYTHONTESTVAR'
    value = 'testvalue'
    code = f'import os; print(repr(os.environ.get({name!r})))'
    with os_helper.EnvironmentVarGuard() as env:
        env.pop(name, None)
        os.putenv(name, value)
        proc = subprocess.run([sys.executable, '-c', code], check=True, stdout=subprocess.PIPE, text=True)
        self.assertEqual(proc.stdout.rstrip(), repr(value))
        os.unsetenv(name)
        proc = subprocess.run([sys.executable, '-c', code], check=True, stdout=subprocess.PIPE, text=True)
        self.assertEqual(proc.stdout.rstrip(), repr(None))
