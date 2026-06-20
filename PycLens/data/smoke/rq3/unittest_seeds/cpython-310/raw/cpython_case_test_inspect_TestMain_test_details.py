# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestMain_test_details

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    module = importlib.import_module('unittest')
    args = support.optim_args_from_interpreter_flags()
    (rc, out, err) = assert_python_ok(*args, '-m', 'inspect', 'unittest', '--details')
    output = out.decode()
    self.assertIn(module.__name__, output)
    self.assertIn(module.__file__, output)
    self.assertIn(module.__cached__, output)
    self.assertEqual(err, b'')
