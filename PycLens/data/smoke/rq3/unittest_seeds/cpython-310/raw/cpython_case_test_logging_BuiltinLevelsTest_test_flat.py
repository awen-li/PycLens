# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BuiltinLevelsTest_test_flat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = self.next_message
    ERR = logging.getLogger('ERR')
    ERR.setLevel(logging.ERROR)
    INF = logging.LoggerAdapter(logging.getLogger('INF'), {})
    INF.setLevel(logging.INFO)
    DEB = logging.getLogger('DEB')
    DEB.setLevel(logging.DEBUG)
    ERR.log(logging.CRITICAL, m())
    ERR.error(m())
    INF.log(logging.CRITICAL, m())
    INF.error(m())
    INF.warning(m())
    INF.info(m())
    DEB.log(logging.CRITICAL, m())
    DEB.error(m())
    DEB.warning(m())
    DEB.info(m())
    DEB.debug(m())
    ERR.warning(m())
    ERR.info(m())
    ERR.debug(m())
    INF.debug(m())
    self.assert_log_lines([('ERR', 'CRITICAL', '1'), ('ERR', 'ERROR', '2'), ('INF', 'CRITICAL', '3'), ('INF', 'ERROR', '4'), ('INF', 'WARNING', '5'), ('INF', 'INFO', '6'), ('DEB', 'CRITICAL', '7'), ('DEB', 'ERROR', '8'), ('DEB', 'WARNING', '9'), ('DEB', 'INFO', '10'), ('DEB', 'DEBUG', '11')])
