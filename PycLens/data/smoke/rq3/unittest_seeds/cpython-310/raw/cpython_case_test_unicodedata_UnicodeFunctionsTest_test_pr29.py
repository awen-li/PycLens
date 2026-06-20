# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_pr29

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    composed = ('େ̀ା', 'ᄀ̀ᅡ', 'Li̍t-sṳ́', 'मार्क ज़' + 'ुकेरबर्ग', 'किर्गिज़' + 'स्तान')
    for text in composed:
        self.assertEqual(self.db.normalize('NFC', text), text)
