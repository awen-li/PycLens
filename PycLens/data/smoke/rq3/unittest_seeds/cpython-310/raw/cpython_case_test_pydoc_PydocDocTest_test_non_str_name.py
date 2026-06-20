# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_non_str_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        __name__ = 42

    class B:
        pass
    adoc = pydoc.render_doc(A())
    bdoc = pydoc.render_doc(B())
    self.assertEqual(adoc.replace('A', 'B'), bdoc)
