# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: UnraisableHookTest_test_original_unraisablehook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for err_msg in (None, 'original hook'):
        with self.subTest(err_msg=err_msg):
            obj = 'an object'
            with test.support.captured_output('stderr') as stderr:
                with test.support.swap_attr(sys, 'unraisablehook', sys.__unraisablehook__):
                    self.write_unraisable_exc(ValueError(42), err_msg, obj)
            err = stderr.getvalue()
            if err_msg is not None:
                self.assertIn(f'Exception ignored {err_msg}: {obj!r}\n', err)
            else:
                self.assertIn(f'Exception ignored in: {obj!r}\n', err)
            self.assertIn('Traceback (most recent call last):\n', err)
            self.assertIn('ValueError: 42\n', err)
