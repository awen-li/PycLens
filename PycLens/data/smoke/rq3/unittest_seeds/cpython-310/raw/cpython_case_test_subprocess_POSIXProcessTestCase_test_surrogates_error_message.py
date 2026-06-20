# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_surrogates_error_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def prepare():
        raise ValueError('surrogate:\udcff')
    try:
        subprocess.call(ZERO_RETURN_CMD, preexec_fn=prepare)
    except ValueError as err:
        self.assertIsNone(subprocess._posixsubprocess)
        self.assertEqual(str(err), 'surrogate:\udcff')
    except subprocess.SubprocessError as err:
        self.assertIsNotNone(subprocess._posixsubprocess)
        self.assertEqual(str(err), 'Exception occurred in preexec_fn.')
    else:
        self.fail('Expected ValueError or subprocess.SubprocessError')
