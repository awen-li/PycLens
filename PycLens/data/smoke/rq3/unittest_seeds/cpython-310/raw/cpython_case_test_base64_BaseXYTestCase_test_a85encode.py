# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_a85encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    tests = {b'': b'', b'www.python.org': b'GB\\6`E-ZP=Df.1GEb>', bytes(range(255)): b'!!*-\'"9eu7#RLhG$k3[W&.oNg\'GVB"(`=52*$$(B+<_pR,UFcb-n-Vr/1iJ-0JP==1c70M3&s#]4?Ykm5X@_(6q\'R884cEH9MJ8X:f1+h<)lt#=BSg3>[:ZC?t!MSA7]@cBPD3sCi+\'.E,fo>FEMbNG^4U^I!pHnJ:W<)KS>/9Ll%"IN/`jYOHG]iPa.Q$R$jD4S=Q7DTV8*TUnsrdW2ZetXKAY/Yd(L?[\'d?O\\@K2_]Y2%o^qmn*`5Ta:aN;TJbg"GZd*^:jeCE.%f\\,!5gtgiEi8N\\UjQ5OekiqBum-X60nF?)@o_%qPq"ad`r;HT', b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#0^&*();:<>,. []{}': b'@:E_WAS,RgBkhF"D/O92EH6,BF`qtRH$VbC6UX@47n?3D92&&T:Jand;cHat=\'/U/0JP==1c70M3&r-I,;<FN.OZ`-3]oSW/g+A(H[P', b'no padding..': b'DJpY:@:Wn_DJ(RS', b'zero compression\x00\x00\x00\x00': b'H=_,8+Cf>,E,oN2F(oQ1z', b'zero compression\x00\x00\x00': b'H=_,8+Cf>,E,oN2F(oQ1!!!!', b'Boundary:\x00\x00\x00\x00': b'6>q!aA79M(3WK-[!!', b'Space compr:    ': b';fH/TAKYK$D/aMV+<VdL', b'\xff': b'rr', b'\xff' * 2: b's8N', b'\xff' * 3: b's8W*', b'\xff' * 4: b's8W-!'}
    for (data, res) in tests.items():
        eq(base64.a85encode(data), res, data)
        eq(base64.a85encode(data, adobe=False), res, data)
        eq(base64.a85encode(data, adobe=True), b'<~' + res + b'~>', data)
    self.check_other_types(base64.a85encode, b'www.python.org', b'GB\\6`E-ZP=Df.1GEb>')
    self.assertRaises(TypeError, base64.a85encode, '')
    eq(base64.a85encode(b'www.python.org', wrapcol=7, adobe=False), b'GB\\6`E-\nZP=Df.1\nGEb>')
    eq(base64.a85encode(b'\x00\x00\x00\x00www.python.org', wrapcol=7, adobe=False), b'zGB\\6`E\n-ZP=Df.\n1GEb>')
    eq(base64.a85encode(b'www.python.org', wrapcol=7, adobe=True), b'<~GB\\6`\nE-ZP=Df\n.1GEb>\n~>')
    eq(base64.a85encode(b' ' * 8, foldspaces=True, adobe=False), b'yy')
    eq(base64.a85encode(b' ' * 7, foldspaces=True, adobe=False), b'y+<Vd')
    eq(base64.a85encode(b' ' * 6, foldspaces=True, adobe=False), b'y+<U')
    eq(base64.a85encode(b' ' * 5, foldspaces=True, adobe=False), b'y+9')
