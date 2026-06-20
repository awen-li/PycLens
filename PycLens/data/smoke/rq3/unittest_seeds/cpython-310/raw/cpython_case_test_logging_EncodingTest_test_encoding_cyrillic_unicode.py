# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: EncodingTest_test_encoding_cyrillic_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    log = logging.getLogger('test')
    message = 'до свидания'
    writer_class = codecs.getwriter('cp1251')
    writer_class.encoding = 'cp1251'
    stream = io.BytesIO()
    writer = writer_class(stream, 'strict')
    handler = logging.StreamHandler(writer)
    log.addHandler(handler)
    try:
        log.warning(message)
    finally:
        log.removeHandler(handler)
        handler.close()
    s = stream.getvalue()
    self.assertEqual(s, b'\xe4\xee \xf1\xe2\xe8\xe4\xe0\xed\xe8\xff\n')
