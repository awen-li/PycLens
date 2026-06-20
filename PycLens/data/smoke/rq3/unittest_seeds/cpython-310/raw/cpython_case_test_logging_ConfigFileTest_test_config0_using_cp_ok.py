# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigFileTest_test_config0_using_cp_ok

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stdout() as output:
        file = io.StringIO(textwrap.dedent(self.config0))
        cp = configparser.ConfigParser()
        cp.read_file(file)
        logging.config.fileConfig(cp)
        logger = logging.getLogger()
        logger.info(self.next_message())
        logger.error(self.next_message())
        self.assert_log_lines([('ERROR', '2')], stream=output)
        self.assert_log_lines([])
