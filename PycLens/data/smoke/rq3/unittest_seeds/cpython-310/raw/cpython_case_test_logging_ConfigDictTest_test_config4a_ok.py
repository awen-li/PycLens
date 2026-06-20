# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigDictTest_test_config4a_ok

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stdout() as output:
        self.apply_config(self.config4a)
        try:
            raise RuntimeError()
        except RuntimeError:
            logging.exception('just testing')
        sys.stdout.seek(0)
        self.assertEqual(output.getvalue(), 'ERROR:root:just testing\nGot a [RuntimeError]\n')
        self.assert_log_lines([])
