# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BuiltinLevelsTest_test_nested_inherited

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = self.next_message
    INF = logging.getLogger('INF')
    INF.setLevel(logging.INFO)
    INF_ERR = logging.getLogger('INF.ERR')
    INF_ERR.setLevel(logging.ERROR)
    INF_UNDEF = logging.getLogger('INF.UNDEF')
    INF_ERR_UNDEF = logging.getLogger('INF.ERR.UNDEF')
    UNDEF = logging.getLogger('UNDEF')
    INF_UNDEF.log(logging.CRITICAL, m())
    INF_UNDEF.error(m())
    INF_UNDEF.warning(m())
    INF_UNDEF.info(m())
    INF_ERR_UNDEF.log(logging.CRITICAL, m())
    INF_ERR_UNDEF.error(m())
    INF_UNDEF.debug(m())
    INF_ERR_UNDEF.warning(m())
    INF_ERR_UNDEF.info(m())
    INF_ERR_UNDEF.debug(m())
    self.assert_log_lines([('INF.UNDEF', 'CRITICAL', '1'), ('INF.UNDEF', 'ERROR', '2'), ('INF.UNDEF', 'WARNING', '3'), ('INF.UNDEF', 'INFO', '4'), ('INF.ERR.UNDEF', 'CRITICAL', '5'), ('INF.ERR.UNDEF', 'ERROR', '6')])
