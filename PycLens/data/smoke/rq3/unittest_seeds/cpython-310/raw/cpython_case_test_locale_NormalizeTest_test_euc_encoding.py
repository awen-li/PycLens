# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: NormalizeTest_test_euc_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check('ja_jp.euc', 'ja_JP.eucJP')
    self.check('ja_jp.eucjp', 'ja_JP.eucJP')
    self.check('ko_kr.euc', 'ko_KR.eucKR')
    self.check('ko_kr.euckr', 'ko_KR.eucKR')
    self.check('zh_cn.euc', 'zh_CN.eucCN')
    self.check('zh_tw.euc', 'zh_TW.eucTW')
    self.check('zh_tw.euctw', 'zh_TW.eucTW')
