# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_method_aliases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def tkraise(self, aboveThis=None):
            """Raise this widget in the stacking order."""
        lift = tkraise

        def a_size(self):
            """Return size"""

    class B(A):

        def itemconfigure(self, tagOrId, cnf=None, **kw):
            """Configure resources of an item TAGORID."""
        itemconfig = itemconfigure
        b_size = A.a_size
    doc = pydoc.render_doc(B)
    doc = re.sub('\x08.', '', doc)
    self.assertEqual(doc, 'Python Library Documentation: class B in module %s\n\nclass B(A)\n |  Method resolution order:\n |      B\n |      A\n |      builtins.object\n |  \n |  Methods defined here:\n |  \n |  b_size = a_size(self)\n |  \n |  itemconfig = itemconfigure(self, tagOrId, cnf=None, **kw)\n |  \n |  itemconfigure(self, tagOrId, cnf=None, **kw)\n |      Configure resources of an item TAGORID.\n |  \n |  ----------------------------------------------------------------------\n |  Methods inherited from A:\n |  \n |  a_size(self)\n |      Return size\n |  \n |  lift = tkraise(self, aboveThis=None)\n |  \n |  tkraise(self, aboveThis=None)\n |      Raise this widget in the stacking order.\n |  \n |  ----------------------------------------------------------------------\n |  Data descriptors inherited from A:\n |  \n |  __dict__\n |      dictionary for instance variables (if defined)\n |  \n |  __weakref__\n |      list of weak references to the object (if defined)\n' % __name__)
    doc = pydoc.render_doc(B, renderer=pydoc.HTMLDoc())
    self.assertEqual(doc, 'Python Library Documentation: class B in module %s\n\n<p>\n<table width="100%%" cellspacing=0 cellpadding=2 border=0 summary="section">\n<tr bgcolor="#ffc8d8">\n<td colspan=3 valign=bottom>&nbsp;<br>\n<font color="#000000" face="helvetica, arial"><a name="B">class <strong>B</strong></a>(A)</font></td></tr>\n    \n<tr><td bgcolor="#ffc8d8"><tt>&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>\n<td width="100%%"><dl><dt>Method resolution order:</dt>\n<dd>B</dd>\n<dd>A</dd>\n<dd><a href="builtins.html#object">builtins.object</a></dd>\n</dl>\n<hr>\nMethods defined here:<br>\n<dl><dt><a name="B-b_size"><strong>b_size</strong></a> = <a href="#B-a_size">a_size</a>(self)</dt></dl>\n\n<dl><dt><a name="B-itemconfig"><strong>itemconfig</strong></a> = <a href="#B-itemconfigure">itemconfigure</a>(self, tagOrId, cnf=None, **kw)</dt></dl>\n\n<dl><dt><a name="B-itemconfigure"><strong>itemconfigure</strong></a>(self, tagOrId, cnf=None, **kw)</dt><dd><tt>Configure&nbsp;resources&nbsp;of&nbsp;an&nbsp;item&nbsp;TAGORID.</tt></dd></dl>\n\n<hr>\nMethods inherited from A:<br>\n<dl><dt><a name="B-a_size"><strong>a_size</strong></a>(self)</dt><dd><tt>Return&nbsp;size</tt></dd></dl>\n\n<dl><dt><a name="B-lift"><strong>lift</strong></a> = <a href="#B-tkraise">tkraise</a>(self, aboveThis=None)</dt></dl>\n\n<dl><dt><a name="B-tkraise"><strong>tkraise</strong></a>(self, aboveThis=None)</dt><dd><tt>Raise&nbsp;this&nbsp;widget&nbsp;in&nbsp;the&nbsp;stacking&nbsp;order.</tt></dd></dl>\n\n<hr>\nData descriptors inherited from A:<br>\n<dl><dt><strong>__dict__</strong></dt>\n<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>\n</dl>\n<dl><dt><strong>__weakref__</strong></dt>\n<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>\n</dl>\n</td></tr></table>' % __name__)
