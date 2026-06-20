# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree_c.py
# case: test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    from test import test_xml_etree
    support.run_unittest(MiscTests, TestAliasWorking, TestAcceleratorImported, SizeofTest)
    test_xml_etree.test_main(module=cET)
