# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigFileTest_test_defaults_do_no_interpolation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ini = textwrap.dedent('\n            [formatters]\n            keys=default\n\n            [formatter_default]\n\n            [handlers]\n            keys=console\n\n            [handler_console]\n            class=logging.StreamHandler\n            args=tuple()\n\n            [loggers]\n            keys=root\n\n            [logger_root]\n            formatter=default\n            handlers=console\n            ').strip()
    (fd, fn) = tempfile.mkstemp(prefix='test_logging_', suffix='.ini')
    try:
        os.write(fd, ini.encode('ascii'))
        os.close(fd)
        logging.config.fileConfig(fn, encoding='utf-8', defaults=dict(version=1, disable_existing_loggers=False, formatters={'generic': {'format': '%(asctime)s [%(process)d] [%(levelname)s] %(message)s', 'datefmt': '[%Y-%m-%d %H:%M:%S %z]', 'class': 'logging.Formatter'}}))
    finally:
        os.unlink(fn)
