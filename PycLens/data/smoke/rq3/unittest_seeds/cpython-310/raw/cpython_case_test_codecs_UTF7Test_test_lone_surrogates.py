# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF7Test_test_lone_surrogates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [(b'a+2AE-b', 'a\ud801b'), (b'a+2AE\xffb', 'a�b'), (b'a+2AE', 'a�'), (b'a+2AEA-b', 'a�b'), (b'a+2AH-b', 'a�b'), (b'a+IKzYAQ-b', 'a€\ud801b'), (b'a+IKzYAQ\xffb', 'a€�b'), (b'a+IKzYAQA-b', 'a€�b'), (b'a+IKzYAd-b', 'a€�b'), (b'a+IKwgrNgB-b', 'a€€\ud801b'), (b'a+IKwgrNgB\xffb', 'a€€�b'), (b'a+IKwgrNgB', 'a€€�'), (b'a+IKwgrNgBA-b', 'a€€�b')]
    for (raw, expected) in tests:
        with self.subTest(raw=raw):
            self.assertEqual(raw.decode('utf-7', 'replace'), expected)
