# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree_c.py
# case: MiscTests_test_parser_ref_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def parser_ref_cycle():
        parser = cET.XMLParser()
        try:
            raise ValueError
        except ValueError as exc:
            err = exc
    parser_ref_cycle()
    support.gc_collect()
