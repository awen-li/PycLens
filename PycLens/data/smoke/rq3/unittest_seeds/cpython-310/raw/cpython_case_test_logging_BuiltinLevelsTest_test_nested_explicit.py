# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BuiltinLevelsTest_test_nested_explicit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = self.next_message
    INF = logging.getLogger('INF')
    INF.setLevel(logging.INFO)
    INF_ERR = logging.getLogger('INF.ERR')
    INF_ERR.setLevel(logging.ERROR)
    INF_ERR.log(logging.CRITICAL, m())
    INF_ERR.error(m())
    INF_ERR.warning(m())
    INF_ERR.info(m())
    INF_ERR.debug(m())
    self.assert_log_lines([('INF.ERR', 'CRITICAL', '1'), ('INF.ERR', 'ERROR', '2')])
