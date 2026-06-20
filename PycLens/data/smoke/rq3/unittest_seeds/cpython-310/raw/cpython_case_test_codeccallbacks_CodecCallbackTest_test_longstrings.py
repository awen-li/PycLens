# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_longstrings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    errors = ['strict', 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace', 'namereplace']
    for err in errors:
        codecs.register_error('test.' + err, codecs.lookup_error(err))
    l = 1000
    errors += ['test.' + err for err in errors]
    for uni in [s * l for s in ('x', 'あ', 'aä')]:
        for enc in ('ascii', 'latin-1', 'iso-8859-1', 'iso-8859-15', 'utf-8', 'utf-7', 'utf-16', 'utf-32'):
            for err in errors:
                try:
                    uni.encode(enc, err)
                except UnicodeError:
                    pass
