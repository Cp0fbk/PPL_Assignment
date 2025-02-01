import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    
    def test_101(self):
        """test variable"""
        input = "a : integer;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 101))

    def test_102(self):
        """test variable"""
        input = """
        a, b, c : integer; 
            e : float;
            a : integer
        """
        expect = "Error on line 5 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 102))

    def test_103(self):
        """test variable"""
        input = """
           a, b, c : integer; 
            e : float;
            s : string;
            a : integer
        """
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 103))

    def test_104(self):
        """test variable"""
        input = """
           a, b, c : integer; 
            e : float;
            a, : integer;
            s : string;
            a : integer
        """
        expect = "Error on line 4 col 15: :"
        self.assertTrue(TestParser.test(input, expect, 104))

    def test_105(self):
        """test variable"""
        input = """
            a : float;
            b : boolean;
            c : string;
            d : auto;
            e, h : auto;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 105))
    
    def test_106(self):
        """test variable"""
        input = """
            f : array [1] of integer;
            g : array [1, 2] of float;
            h, h, h : array [1, 3] of boolean;
            j : array [1, 3] of integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 106))

    def test_107(self):
        """test variable"""
        input = """
            c : string;
            d : auto;
            e, h : auto;
            f : array [1] of integer;
            g : array [1, 2] of float;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 107))

    def test_108(self):
        """test variable"""
        input = """
            a : array [1] of auto;
        """
        expect = "Error on line 2 col 29: auto"
        self.assertTrue(TestParser.test(input, expect, 108))

    def test_109(self):
        """test variable"""
        input = """
            a : array [] of auto;
        """
        expect = "Error on line 2 col 23: ]"
        self.assertTrue(TestParser.test(input, expect, 109))

    def test_110(self):
        """test variable"""
        input = """
            a : array [,] of auto;
        """
        expect = "Error on line 2 col 23: ,"
        self.assertTrue(TestParser.test(input, expect, 110))
    def test_111(self):
        """test variable"""
        input = """
            a : array [1.2] of auto;
        """
        expect = "Error on line 2 col 23: 1.2"
        self.assertTrue(TestParser.test(input, expect, 111))

    def test_112(self):
        """test variable"""
        input = """
            a : array [0.5] of auto;
        """
        expect = "Error on line 2 col 23: 0.5"
        self.assertTrue(TestParser.test(input, expect, 112))
    
    def test_113(self):
        """test variable"""
        input = """
            a : array [true] of auto;
        """
        expect = "Error on line 2 col 23: true"
        self.assertTrue(TestParser.test(input, expect, 113))
    
    def test_114(self):
        """test variable"""
        input = """
            a : array [1+2] of auto;
        """
        expect = "Error on line 2 col 24: +"
        self.assertTrue(TestParser.test(input, expect, 114))

    def test_115(self):
        """test variable"""
        input = """
            a : array [1-2] of auto;
        """
        expect = "Error on line 2 col 24: -"
        self.assertTrue(TestParser.test(input, expect, 115))
    
    def test_116(self):
        """test variable"""
        input = """
            a : array [1/2] of auto;
        """
        expect = "Error on line 2 col 24: /"
        self.assertTrue(TestParser.test(input, expect, 116))

    def test_117(self):
        """test variable"""
        input = """
            a : array [1%2] of auto;
        """
        expect = "Error on line 2 col 24: %"
        self.assertTrue(TestParser.test(input, expect, 117))
    
    def test_118(self):
        """test variable"""
        input = """
            a : array [1=2] of auto;
        """
        expect = "Error on line 2 col 24: ="
        self.assertTrue(TestParser.test(input, expect, 118))

    def test_119(self):
        """test variable"""
        input = """
            a : array [1e2] of auto;
        """
        expect = "Error on line 2 col 23: 1e2"
        self.assertTrue(TestParser.test(input, expect, 119))

    def test_120(self):
        """test variable"""
        input = """
            f : integer = 1;
            x, y : integer = 1, 2;
            a, b, c, d : array [1] of float  = 1, 2, 3, 4;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 120))

    def test_121(self):
        """test variable"""
        input = """
            f : integer = 1, 2;
            x, y : integer = 1, 2;
            a, b, c, d : array [1] of float  = 1, 2, 3, 4;
        """
        expect = "Error on line 2 col 27: ,"
        self.assertTrue(TestParser.test(input, expect, 121))
    
    def test_122(self):
        """test variable"""
        input = """
            a, b : integer = 1;
        """
        expect = "Error on line 2 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 122))

    def test_123(self):
        """test variable"""
        input = """
            x, y : float = 1;
        """
        expect = "Error on line 2 col 28: ;"
        self.assertTrue(TestParser.test(input, expect, 123))

    def test_124(self):
        """test variable"""
        input = """
            for : auto = 1;
        """
        expect = "Error on line 2 col 12: for"
        self.assertTrue(TestParser.test(input, expect, 124))
    
    def test_125(self):
        """test variable"""
        input = """
            for : auto = 5;
        """
        expect = "Error on line 2 col 12: for"
        self.assertTrue(TestParser.test(input, expect, 125))
    
    def test_126(self):
        """test variable"""
        input = """
            x : auto = for;
        """
        expect = "Error on line 2 col 23: for"
        self.assertTrue(TestParser.test(input, expect, 126))
    
    def test_127(self):
        """test variable"""
        input = """
            x : string = ;
        """
        expect = "Error on line 2 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 127))

    def test_128(self):
        """test variable"""
        input = """
            x : float = ;
        """
        expect = "Error on line 2 col 24: ;"
        self.assertTrue(TestParser.test(input, expect, 128))
    
    def test_129(self):
        """test function"""
        input = """
            function : function auto (inherit out id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "Error on line 2 col 12: function"
        self.assertTrue(TestParser.test(input, expect, 129))
    
    def test_130(self):
        """test function"""
        input = """
            foo : function auto (inherit out id : auto, inherit out id : auto) inherit foo1 {}
            foo : function array [1] of integer () {}
            foo : function integer (inherit id : float, out id : boolean, id : array [1] of integer) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 130))
    
    def test_131(self):
        """test function"""
        input = """
            foo : function break (inherit out id : auto, inherit out id : auto) inherit foo1 {}
            foo : function array [1] of integer () {}
            foo : function integer (inherit id : float, out id : boolean, id : array [1] of integer) {}
        """
        expect = "Error on line 2 col 27: break"
        self.assertTrue(TestParser.test(input, expect, 131))
    
    def test_132(self):
        """test function"""
        input = """
            foo : function true (inherit out id : auto, inherit out id : auto) inherit foo1 {}
            foo : function array [1] of integer () {}
            foo : function integer (inherit id : float, out id : boolean, id : array [1] of integer) {}
        """
        expect = "Error on line 2 col 27: true"
        self.assertTrue(TestParser.test(input, expect, 132))

    def test_133(self):
        """test function"""
        input = """
            foo : function out (inherit out id : auto, inherit out id : auto) inherit foo1 {}
            foo : function array [1] of integer () {}
            foo : function integer (inherit id : float, out id : boolean, id : array [1] of integer) {}
        """
        expect = "Error on line 2 col 27: out"
        self.assertTrue(TestParser.test(input, expect, 133))
    
    def test_134(self):
        """test function"""
        input = """
            function : function auto (inherit out id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "Error on line 2 col 12: function"
        self.assertTrue(TestParser.test(input, expect, 134))
    
    def test_135(self):
        """test function"""
        input = """
            array : function auto (inherit out id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "Error on line 2 col 12: array"
        self.assertTrue(TestParser.test(input, expect, 135))

    def test_136(self):
        """test function"""
        input = """
            out : function auto (inherit out id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "Error on line 2 col 12: out"
        self.assertTrue(TestParser.test(input, expect, 136))

    def test_137(self):
        """test function"""
        input = """
            false : function auto (inherit out id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "Error on line 2 col 12: false"
        self.assertTrue(TestParser.test(input, expect, 137))

    def test_138(self):
        """test function"""
        input = """
            foo : function auto (out inherit id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "Error on line 2 col 37: inherit"
        self.assertTrue(TestParser.test(input, expect, 138))
    
    def test_139(self):
        """test function"""
        input = """
            foo : function, auto (out inherit id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "Error on line 2 col 26: ,"
        self.assertTrue(TestParser.test(input, expect, 139))
    
    def test_140(self):
        """test function"""
        input = """
            foo : function auto (inherit out id : auto, ) inherit foo1 {}
        """
        expect = "Error on line 2 col 56: )"
        self.assertTrue(TestParser.test(input, expect, 140))
    
    def test_141(self):
        """test function"""
        input = """
            foo : function auto (inherit out id : auto, float ) inherit foo1 {}
        """
        expect = "Error on line 2 col 56: float"
        self.assertTrue(TestParser.test(input, expect, 141))

    def test_142(self):
        """test function"""
        input = """
            foo5 : function auto (inherit out id : auto) inherit out foo1 {}
        """
        expect = "Error on line 2 col 65: out"
        self.assertTrue(TestParser.test(input, expect, 142))
    
    def test_143(self):
        """test function"""
        input = """
            foo5 : function auto (inherit out id : auto) inherit break foo1 {}
        """
        expect = "Error on line 2 col 65: break"
        self.assertTrue(TestParser.test(input, expect, 143))
    
    def test_144(self):
        """test function"""
        input = """
            fo4 : function (inherit out id : auto) {}
        """
        expect = "Error on line 2 col 27: ("
        self.assertTrue(TestParser.test(input, expect, 144))
    
    def test_145(self):
        """test function"""
        input = """
            fo4 : function auto (inherit out id : auto) foo5 {}
        """
        expect = "Error on line 2 col 56: foo5"
        self.assertTrue(TestParser.test(input, expect, 145))
    
    def test_146(self):
        """test function"""
        input = """
            id : auto = a :: 1;
            id : auto = a <= b;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 146))
    
    def test_147(self):
        """test function"""
        input = """
            id : auto = a[1,2,3];
            id : auto = id[2,3] + id[2];
            id : auto = 1 + 1.0 - "1" + true - false - {1} + {1,2,3};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 147))
    
    def test_148(self):
        """test function"""
        input = """
            id : auto = a >= b;
            id : auto = a < b;
            id : auto = a + b - c;
            id : auto = a * b / c % d;
            id : auto = - a;
            id : auto = ! a;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 148))

    def test_149(self):
        """test function"""
        input = """
            id : auto = a == b;
            id : auto = a != b;
            id : auto = a && b || c ;
            id : auto = a + b - c;
            id : auto = a * b / c % d;
            id : auto = - a;
            id : auto = ! a;
            id : auto = a[1,2,3];
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 149))
    
    def test_150(self):
        """test function"""
        input = """
            id : auto = a == b;
            id : auto = a != b;
            id : auto = a && b || c ;
            id : auto = a + b - c;
            id : auto = a * b / c % d;
            id : auto = - a;
            id : auto = ! a;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 150))

    def test_151(self):
        """test function"""
        input = """
            id : auto = a > b ;
            id : auto = a != b;
            id : auto = a && b || c ;
            id : auto = a + b - c;
            id : auto = a * b / c % d;
            id : auto = - a;
            id : auto = id[2,3] + id[2];
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 151))
    
    def test_152(self):
        """test function"""
        input = """
            fo4 : function false (inherit out id : auto) {}
        """
        expect = "Error on line 2 col 27: false"
        self.assertTrue(TestParser.test(input, expect, 152))

    def test_153(self):
        """test function"""
        input = """
            fo4 : function (inherit break id : auto) {}
        """
        expect = "Error on line 2 col 27: ("
        self.assertTrue(TestParser.test(input, expect, 153))
    
    def test_154(self):
        """test expression"""
        input = """
            id : auto = "a" :: 15 :: "b";
        """
        expect = "Error on line 2 col 34: ::"
        self.assertTrue(TestParser.test(input, expect, 154))
    
    def test_155(self):
        """test expression"""
        input = """
            id : float = "a" :: 15 :: "b";
        """
        expect = "Error on line 2 col 35: ::"
        self.assertTrue(TestParser.test(input, expect, 155))
    
    def test_156(self):
        """test expression"""
        input = """
            id : integer = "a" :: 15 :: "b";
        """
        expect = "Error on line 2 col 37: ::"
        self.assertTrue(TestParser.test(input, expect, 156))
    
    def test_157(self):
        """test expression"""
        input = """
            id : string = "a" :: 15 :: "b";
        """
        expect = "Error on line 2 col 36: ::"
        self.assertTrue(TestParser.test(input, expect, 157))
    
    def test_158(self):
        """test expression"""
        input = """
            id : bool = "a" :: 15 :: "b";
        """
        expect = "Error on line 2 col 17: bool"
        self.assertTrue(TestParser.test(input, expect, 158))
    
    def test_159(self):
        """test expression"""
        input = """
            a5 : auto = ("a" :: 1) :: "b";
            a9 : auto = "a" :: (a[2] :: "b");
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 159))
    
    def test_160(self):
        """test expression"""
        input = """
            a5 : auto = a >= b < c;
        """
        expect = "Error on line 2 col 31: <"
        self.assertTrue(TestParser.test(input, expect, 160))
    
    def test_161(self):
        """test expression"""
        input = """
            a5 : auto = a != b = c;
        """
        expect = "Error on line 2 col 31: ="
        self.assertTrue(TestParser.test(input, expect, 161))

    def test_162(self):
        """test expression"""
        input = """
            a5 : auto = a != b > c;
        """
        expect = "Error on line 2 col 31: >"
        self.assertTrue(TestParser.test(input, expect, 162))
    
    def test_163(self):
        """test expression"""
        input = """
            id : string = (a :: b) > c :: d;
            id : string = a :: b > c :: d;
        """
        expect = "Error on line 3 col 37: ::"
        self.assertTrue(TestParser.test(input, expect, 163))

    def test_164(self):
        """test expression"""
        input = """
            id : string = a && b && c;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 164))
    
    def test_165(self):
        """test expression"""
        input = """
            id : string = a && b || c;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 165))
    
    def test_166(self):
        """test expression"""
        input = """
            id : string = true || false && "true" || a[7];
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 166))
    
    def test_167(self):
        """test expression"""
        input = """
            a5 : array [1] of integer = (a > b) && (d < c);
            a9 : string = a > b && d < c;
        """
        expect = "Error on line 3 col 37: <"
        self.assertTrue(TestParser.test(input, expect, 167))
    
    def test_168(self):
        """test expression"""
        input = """
            str : string = a + b * 2 / b % c;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 168))
    
    def test_169(self):
        """test expression"""
        input = """
            str : string =  b * 2 / b % c;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 169))
    
    def test_170(self):
        """test expression"""
        input = """
            num : float = ---- b;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 170))
    
    def test_171(self):
        """test expression"""
        input = """
            num : float = ! ! ! b;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 171))
    
    def test_172(self):
        """test expression"""
        input = """
            a5 : float = !! -- b;
            a9 : float = -- !! b;
        """
        expect = "Error on line 3 col 28: !"
        self.assertTrue(TestParser.test(input, expect, 172))
    
    def test_173(self):
        """test expression"""
        input = """
            a5 : float = for[1+2, 7 :: c];
        """
        expect = "Error on line 2 col 25: for"
        self.assertTrue(TestParser.test(input, expect, 173))
    
    def test_174(self):
        """test expression"""
        input = """
            a5 : float = a[];
        """
        expect = "Error on line 2 col 27: ]"
        self.assertTrue(TestParser.test(input, expect, 174))
    
    def test_175(self):
        """test expression"""
        input = """
            ar : float = a[1][2];
        """
        expect = "Error on line 2 col 29: ["
        self.assertTrue(TestParser.test(input, expect, 175))
    
    def test_176(self):
        """test expression"""
        input = """
            a5 : float = fo4() + fo4(i[2, 1+ 2], 2 :: 3, "2");
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 176))
    
    def test_177(self):
        """test expression"""
        input = """
            a5 : float = {};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 177))
    
    def test_178(self):
        """test expression"""
        input = """
            a5 : float = foo()[2];
        """
        expect = "Error on line 2 col 30: ["
        self.assertTrue(TestParser.test(input, expect, 178))
    
    def test_179(self):
        """test statements"""
        input = """
            foo : function auto ()
            {
                a5 : float;
                a9 : float = 5;
                a, b : float = 1, 2;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 179))
    
    def test_180(self):
        """test statements"""
        input = """
            fo4 : function auto ()
            {
                a5 = 1 + 2;
                a9 = {2}
            }
        """
        expect = "Error on line 6 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 180))
    
    def test_181(self):
        """test statements"""
        input = """
            fo4 : function auto ()
            {
                if (1+2*3) a = 1;
                else a = 2;
                
                if (true)
                    if (true){}
                    else {}
                    
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 181))
    
    def test_182(self):
        """test statements"""
        input = """
            fo4 : function string ()
            {
                continue;
                break;
                continue;
                break;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 182))

    def test_183(self):
        """test statements"""
        input = """
            fo4 : function string ()
            {
                continue;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 183))
    
    def test_184(self):
        """test statements"""
        input = """
            fo4 : function string ()
            {
                continue
            }
        """
        expect = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 184))
    
    def test_185(self):
        """test statements"""
        input = """
            fo4 : function string ()
            {
                for(id = 1, i < 1, i + 1) break;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 185))
    
    def test_186(self):
        """test statements"""
        input = """
            fo4 : function string ()
            {
                for(id = 1 + 2 * 3, 1+2::3 , 1+2::3) {}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 186))
    
    def test_187(self):
        """test statements"""
        input = """
            fo4 : function string ()
            {
                for(id = 1, i < 1,) break;
            }
        """
        expect = "Error on line 4 col 34: )"
        self.assertTrue(TestParser.test(input, expect, 187))
    
    def test_188(self):
        """test statements"""
        input = """
            fo4 : function string ()
            {
                while() break;
            }
        """
        expect = "Error on line 4 col 22: )"
        self.assertTrue(TestParser.test(input, expect, 188))
    
    def test_189(self):
        """test statements"""
        input = """
            fo4 : function string ()
            {
                do 
                {
                   break; 
                }
                while(true);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 189))
    
    def test_190(self):
        """test statements"""
        input = """
            fo4 : function string ()
            {
                break;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 190))
    
    def test_191(self):
        """test statements"""
        input = """
            fo4 : function string ()
            {
                do 
                    if(true) break;
                while(1);
            }
        """
        expect = "Error on line 5 col 20: if"
        self.assertTrue(TestParser.test(input, expect, 191))
    
    def test_192(self):
        """test statements"""
        input = """
            fo4 : function string ()
            {
                do 
                    {};
                while(1);
            }
        """
        expect = "Error on line 5 col 22: ;"
        self.assertTrue(TestParser.test(input, expect, 192))
    
    def test_193(self):
        """test statements"""
        input = """
            foo : function auto ()
            {
                {  
                }
                {
                    return;
                }
                {}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 193))
    
    def test_194(self):
        """test statements"""
        input = """
            foo : function auto ()
            {
                {  
                }
                {
                    return;
                }
                {{{return;}}}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 194))
    
    def test_195(self):
        """test statements"""
        input = """
            foo : function auto ()
            {
                {   
                };
            }
        """
        expect = "Error on line 5 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 195))

    def test_196(self):
        """test function"""
        input = """
            fo4 : function void (a : void){}
        """
        expect = "Error on line 2 col 37: void"
        self.assertTrue(TestParser.test(input, expect, 196))
    
    def test_197(self):
        """test function"""
        input = """
            fo4 : function void (a : string){}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 197))
    
    def test_198(self):
        """test function"""
        input = """
            fo4 : function auto (a : string){}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 198))
    
    def test_199(self):
        """test statements"""
        input = """
            fo4 : function auto ()
            {
                return
            }
        """
        expect = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 199))
    
    def test_200(self):
        """test function"""
        input = """
            foo : function void (){
                return {1 :: 8, 1 * 5 + a[2, 8], {1,2,4}};
                return foo({1} + {0}, {9});
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))


