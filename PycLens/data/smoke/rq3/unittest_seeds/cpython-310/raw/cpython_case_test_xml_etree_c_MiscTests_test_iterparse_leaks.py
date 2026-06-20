# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree_c.py
# case: MiscTests_test_iterparse_leaks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    XML = '<a></a></b>'
    parser = cET.iterparse(io.StringIO(XML))
    next(parser)
    del parser
    support.gc_collect()
