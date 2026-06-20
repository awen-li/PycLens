# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: NormalizeTest_test_japanese

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check('ja', 'ja_JP.eucJP')
    self.check('ja.jis', 'ja_JP.JIS7')
    self.check('ja.sjis', 'ja_JP.SJIS')
    self.check('ja_jp', 'ja_JP.eucJP')
    self.check('ja_jp.ajec', 'ja_JP.eucJP')
    self.check('ja_jp.euc', 'ja_JP.eucJP')
    self.check('ja_jp.eucjp', 'ja_JP.eucJP')
    self.check('ja_jp.iso-2022-jp', 'ja_JP.JIS7')
    self.check('ja_jp.iso2022jp', 'ja_JP.JIS7')
    self.check('ja_jp.jis', 'ja_JP.JIS7')
    self.check('ja_jp.jis7', 'ja_JP.JIS7')
    self.check('ja_jp.mscode', 'ja_JP.SJIS')
    self.check('ja_jp.pck', 'ja_JP.SJIS')
    self.check('ja_jp.sjis', 'ja_JP.SJIS')
    self.check('ja_jp.ujis', 'ja_JP.eucJP')
    self.check('ja_jp.utf8', 'ja_JP.UTF-8')
    self.check('japan', 'ja_JP.eucJP')
    self.check('japanese', 'ja_JP.eucJP')
    self.check('japanese-euc', 'ja_JP.eucJP')
    self.check('japanese.euc', 'ja_JP.eucJP')
    self.check('japanese.sjis', 'ja_JP.SJIS')
    self.check('jp_jp', 'ja_JP.eucJP')
