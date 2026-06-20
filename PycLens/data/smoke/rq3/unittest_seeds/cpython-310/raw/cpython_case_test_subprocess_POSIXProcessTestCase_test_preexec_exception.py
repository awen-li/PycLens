# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_preexec_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def raise_it():
        raise ValueError('What if two swallows carried a coconut?')
    try:
        p = subprocess.Popen([sys.executable, '-c', ''], preexec_fn=raise_it)
    except subprocess.SubprocessError as e:
        self.assertTrue(subprocess._posixsubprocess, 'Expected a ValueError from the preexec_fn')
    except ValueError as e:
        self.assertIn('coconut', e.args[0])
    else:
        self.fail('Exception raised by preexec_fn did not make it to the parent process.')
