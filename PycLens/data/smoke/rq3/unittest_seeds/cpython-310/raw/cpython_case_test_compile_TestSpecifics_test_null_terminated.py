# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_null_terminated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(ValueError, 'cannot contain null'):
        compile('123\x00', '<dummy>', 'eval')
    with self.assertRaisesRegex(ValueError, 'cannot contain null'):
        compile(memoryview(b'123\x00'), '<dummy>', 'eval')
    code = compile(memoryview(b'123\x00')[1:-1], '<dummy>', 'eval')
    self.assertEqual(eval(code), 23)
    code = compile(memoryview(b'1234')[1:-1], '<dummy>', 'eval')
    self.assertEqual(eval(code), 23)
    code = compile(memoryview(b'$23$')[1:-1], '<dummy>', 'eval')
    self.assertEqual(eval(code), 23)
    self.assertEqual(eval(memoryview(b'1234')[1:-1]), 23)
    namespace = dict()
    exec(memoryview(b'ax = 123')[1:-1], namespace)
    self.assertEqual(namespace['x'], 12)
