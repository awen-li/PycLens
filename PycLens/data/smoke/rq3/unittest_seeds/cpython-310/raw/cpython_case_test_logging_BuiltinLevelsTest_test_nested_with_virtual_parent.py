# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BuiltinLevelsTest_test_nested_with_virtual_parent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = self.next_message
    INF = logging.getLogger('INF')
    GRANDCHILD = logging.getLogger('INF.BADPARENT.UNDEF')
    CHILD = logging.getLogger('INF.BADPARENT')
    INF.setLevel(logging.INFO)
    GRANDCHILD.log(logging.FATAL, m())
    GRANDCHILD.info(m())
    CHILD.log(logging.FATAL, m())
    CHILD.info(m())
    GRANDCHILD.debug(m())
    CHILD.debug(m())
    self.assert_log_lines([('INF.BADPARENT.UNDEF', 'CRITICAL', '1'), ('INF.BADPARENT.UNDEF', 'INFO', '2'), ('INF.BADPARENT', 'CRITICAL', '3'), ('INF.BADPARENT', 'INFO', '4')])
