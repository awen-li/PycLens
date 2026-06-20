# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicConfigTest_test_strformatstyle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stdout() as output:
        logging.basicConfig(stream=sys.stdout, style='{')
        logging.error('Log an error')
        sys.stdout.seek(0)
        self.assertEqual(output.getvalue().strip(), 'ERROR:root:Log an error')
