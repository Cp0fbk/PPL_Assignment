import unittest
from TestUtils import TestAST
from AST import *

#id: 2212631
class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        """test variable declaration"""
        input = """
            a : integer;  
        """
        expect = Program([
                VarDecl("a", IntegerType())
            ])
        self.assertTrue(TestAST.test(input, str(expect), 201))

    def test_2(self):
        """test variable declaration"""
        input = """
            x, y : float;  
        """
        expect = Program([
                VarDecl("x", FloatType()),
                VarDecl("y", FloatType())
            ])
        self.assertTrue(TestAST.test(input, str(expect), 202))

    def test_3(self):
        """test variable declaration"""
        input = """
            x, y : float; 
            z : auto; 
        """
        expect = Program([
                VarDecl("x", FloatType()),
                VarDecl("y", FloatType()),
                VarDecl("z", AutoType())
            ])
        self.assertTrue(TestAST.test(input, str(expect), 203))

    def test_4(self):
        """test variable declaration"""
        input = """
            x, y : string; 
            z : auto; 
        """
        expect = Program([
                VarDecl("x", StringType()),
                VarDecl("y", StringType()),
                VarDecl("z", AutoType())
            ])
        self.assertTrue(TestAST.test(input, str(expect), 204))

    def test_5(self):
        """test variable declaration"""
        input = """
            x, y : string; 
            z : boolean; 
        """
        expect = Program([
                VarDecl("x", StringType()),
                VarDecl("y", StringType()),
                VarDecl("z", BooleanType())
            ])
        self.assertTrue(TestAST.test(input, str(expect), 205))
    
    def test_6(self):
        """test variable declaration"""
        input = """
            a, b : array [4,5] of integer;
        """
        expect = Program([
                VarDecl("a", ArrayType([4, 5], IntegerType())),
                VarDecl("b", ArrayType([4, 5], IntegerType()))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 206))

    def test_7(self):
        """test variable declaration"""
        input = """
            a, b : array [4,5] of float;
        """
        expect = Program([
                VarDecl("a", ArrayType([4, 5], FloatType())),
                VarDecl("b", ArrayType([4, 5], FloatType()))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 207))

    def test_8(self):
        """test variable declaration"""
        input = """
            a, b : array [4] of string;
        """
        expect = Program([
                VarDecl("a", ArrayType([4], StringType())),
                VarDecl("b", ArrayType([4], StringType()))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 208))

    def test_9(self):
        """test variable declaration"""
        input = """
            a, b : array [4] of boolean;
        """
        expect = Program([
                VarDecl("a", ArrayType([4], BooleanType())),
                VarDecl("b", ArrayType([4], BooleanType()))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 209))

    def test_10(self):
        """test variable declaration"""
        input = """
            x : integer = 15;
        """
        expect = Program([
                VarDecl("x", IntegerType(), IntegerLit(15))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 210))
    def test_11(self):
        """test variable declaration"""
        input = """
            x, y : integer = 15, 16;
        """
        expect = Program([
                VarDecl("x", IntegerType(), IntegerLit(15)),
                VarDecl("y", IntegerType(), IntegerLit(16))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 211))

    def test_12(self):
        """test variable declaration"""
        input = """
            x, y : string = 15, 16;
        """
        expect = Program([
                VarDecl("x", StringType(), IntegerLit(15)),
                VarDecl("y", StringType(), IntegerLit(16))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 212))
    
    def test_13(self):
        """test variable declaration"""
        input = """
            x, y : string = 15, 16;
            z : float = 20;
        """
        expect = Program([
                VarDecl("x", StringType(), IntegerLit(15)),
                VarDecl("y", StringType(), IntegerLit(16)),
                VarDecl("z", FloatType(), IntegerLit(20))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 213))
    
    def test_14(self):
        """test variable declaration"""
        input = """
            x, y : auto = 15, 16;
            z, t, e : float = 20, 21, 22;
        """
        expect = Program([
                VarDecl("x", AutoType(), IntegerLit(15)),
                VarDecl("y", AutoType(), IntegerLit(16)),
                VarDecl("z", FloatType(), IntegerLit(20)),
                VarDecl("t", FloatType(), IntegerLit(21)),
                VarDecl("e", FloatType(), IntegerLit(22))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 214))

    def test_15(self):
        """test variable declaration"""
        input = """
            z, t, e : float = 20, 21, 22;
        """
        expect = Program([
                VarDecl("z", FloatType(), IntegerLit(20)),
                VarDecl("t", FloatType(), IntegerLit(21)),
                VarDecl("e", FloatType(), IntegerLit(22))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 215))
    
    def test_16(self):
        """test variable declaration"""
        input = """
            z, t, e : auto = 20, 21, 22;
        """
        expect = Program([
                VarDecl("z", AutoType(), IntegerLit(20)),
                VarDecl("t", AutoType(), IntegerLit(21)),
                VarDecl("e", AutoType(), IntegerLit(22))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 216))

    def test_17(self):
        """test variable declaration"""
        input = """
            z, t, e : boolean;
        """
        expect = Program([
                VarDecl("z", BooleanType()),
                VarDecl("t", BooleanType()),
                VarDecl("e", BooleanType())
            ])
        self.assertTrue(TestAST.test(input, str(expect), 217))
    
    def test_18(self):
        """test variable declaration"""
        input = """
            a, b, c : auto;
        """
        expect = Program([
                VarDecl("a", AutoType()),
                VarDecl("b", AutoType()),
                VarDecl("c", AutoType())
            ])
        self.assertTrue(TestAST.test(input, str(expect), 218))

    def test_19(self):
        """test variable declaration"""
        input = """
            a, b, c : float;
        """
        expect = Program([
                VarDecl("a", FloatType()),
                VarDecl("b", FloatType()),
                VarDecl("c", FloatType())
            ])
        self.assertTrue(TestAST.test(input, str(expect), 219))

    def test_20(self):
        """test function declaration"""
        input = """
            foo : function void () inherit foo1 {}
        """
        expect = Program([
            FuncDecl("foo", VoidType(), [], "foo1", BlockStmt([]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 220))

    def test_21(self):
        """test function declaration"""
        input = """
            foo : function void () inherit foo1 {}
            foo : function auto (inherit out id : float, out id : auto, inherit id : integer) inherit foo1 {}
        """
        expect = Program([
            FuncDecl("foo", VoidType(), [], "foo1", BlockStmt([])),
            FuncDecl("foo", AutoType(), [ParamDecl("id", FloatType(), out=True, inherit=True), 
                                         ParamDecl("id", AutoType(), out=True, inherit=False), 
                                         ParamDecl("id", IntegerType(), out=False, inherit=True)],
                     "foo1", BlockStmt([]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 221))
    
    def test_22(self):
        """test function declaration"""
        input = """
            foo : function auto (inherit out id : float, out id : auto, inherit id : integer) inherit foo1 {}
            foo : function array [1] of integer (inherit out id : array [1] of integer) {}
        """
        expect = Program([
            FuncDecl("foo", AutoType(), [ParamDecl("id", FloatType(), out=True, inherit=True), 
                                         ParamDecl("id", AutoType(), out=True, inherit=False), 
                                         ParamDecl("id", IntegerType(), out=False, inherit=True)],
                     "foo1", BlockStmt([])),
            FuncDecl("foo", ArrayType([1], IntegerType()), [ParamDecl("id", ArrayType([1], IntegerType()), out=True, inherit=True)], "None", BlockStmt([]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 222))

    def test_23(self):
        """test expression"""
        input = """
            id : integer = 1 > 2;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr(">", IntegerLit(1), IntegerLit(2)))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 223))

    def test_24(self):
        """test expression"""
        input = """
            id : integer = 1 > 2;
            id : integer = 1 >= 2;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr(">", IntegerLit(1), IntegerLit(2))),
                VarDecl("id", IntegerType(), BinExpr(">=", IntegerLit(1), IntegerLit(2)))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 224))
    
    def test_25(self):
        """test expression"""
        input = """
            id : integer = 1 < true;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr("<", IntegerLit(1), BooleanLit(True)))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 225))
    
    def test_26(self):
        """test expression"""
        input = """
            id : integer = 1 < true;
            id : integer = 1 <= "2x";
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr("<", IntegerLit(1), BooleanLit(True))),
                VarDecl("id", IntegerType(), BinExpr("<=", IntegerLit(1), StringLit("2x")))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 226))
    
    def test_27(self):
        """test expression"""
        input = """
            id : integer = 1 == 2.0;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr("==", IntegerLit(1), FloatLit(2.0)))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 227))

    def test_28(self):
        """test expression"""
        input = """
            id : integer = 1 > 2;
            id : integer = 1 == 2.0;
            id : integer = 1.0 != 2;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr(">", IntegerLit(1), IntegerLit(2))),
                VarDecl("id", IntegerType(), BinExpr("==", IntegerLit(1), FloatLit(2.0))),
                VarDecl("id", IntegerType(), BinExpr("!=", FloatLit(1.0), IntegerLit(2)))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 228))
    
    def test_29(self):
        """test expression"""
        input = """
            id : integer = 1 < true;
            id : integer = 1.0 != 2;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr("<", IntegerLit(1), BooleanLit(True))),
                VarDecl("id", IntegerType(), BinExpr("!=", FloatLit(1.0), IntegerLit(2)))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 229))
    
    def test_30(self):
        """test expression"""
        input = """
            id : integer = 4 > 5 :: "2" == 15.001;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr("::", BinExpr(">", IntegerLit(4), IntegerLit(5)), BinExpr("==", StringLit("2"), FloatLit(15.001))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 230))
    
    def test_31(self):
        """test expression"""
        input = """
            id : integer = 4 < 5 :: "2" == 1.001;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr("::", BinExpr("<", IntegerLit(4), IntegerLit(5)), BinExpr("==", StringLit("2"), FloatLit(1.001))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 231))
    
    def test_32(self):
        """test expression"""
        input = """
            id : integer = 4 > 5 :: "5" == 1.001;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr("::", BinExpr(">", IntegerLit(4), IntegerLit(5)), BinExpr("==", StringLit("5"), FloatLit(1.001))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 232))

    def test_33(self):
        """test expression"""
        input = """
            x : integer = 4 && 5 || x;
        """
        expect = Program([
                VarDecl("x", IntegerType(), BinExpr("||", BinExpr("&&", IntegerLit(4), IntegerLit(5)), Id("x")))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 233))
    
    def test_34(self):
        """test expression"""
        input = """
            a2 : integer = 3 && 5 || a2;
        """
        expect = Program([
                VarDecl("a2", IntegerType(), BinExpr("||", BinExpr("&&", IntegerLit(3), IntegerLit(5)), Id("a2")))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 234))
    
    def test_35(self):
        """test expression"""
        input = """
            x : integer = 1 + 2 - 3;
        """
        expect = Program([
            VarDecl("x", IntegerType(), BinExpr("-", BinExpr("+", IntegerLit(1), IntegerLit(2)), IntegerLit(3)))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 235))

    def test_36(self):
        """test expression"""
        input = """
            x : integer = 5 - 2 - 3;
        """
        expect = Program([
            VarDecl("x", IntegerType(), BinExpr("-", BinExpr("-", IntegerLit(5), IntegerLit(2)), IntegerLit(3)))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 236))

    def test_37(self):
        """test expression"""
        input = """
            x : integer = 15 / 2 - 3;
        """
        expect = Program([
            VarDecl("x", IntegerType(), BinExpr("-", BinExpr("/", IntegerLit(15), IntegerLit(2)), IntegerLit(3)))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 237))

    def test_38(self):
        """test expression"""
        input = """
            x : integer = 1 + 2 / 3;
        """
        expect = Program([
            VarDecl("x", IntegerType(), BinExpr("+", IntegerLit(1), BinExpr("/", IntegerLit(2), IntegerLit(3))))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 238))
    
    def test_39(self):
        """test expression"""
        input = """
            x : integer = 1 + 2 % 3;
        """
        expect = Program([
            VarDecl("x", IntegerType(), BinExpr("+", IntegerLit(1), BinExpr("%", IntegerLit(2), IntegerLit(3))))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 239))
    
    def test_40(self):
        """test expression"""
        input = """
            x : integer = 1 * 2 / 3;
        """
        expect = Program([
            VarDecl("x", IntegerType(), BinExpr("/", BinExpr("*", IntegerLit(1), IntegerLit(2)), IntegerLit(3)))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 240))
    
    def test_41(self):
        """test expression"""
        input = """
            x : integer = 15 * 5 / 3 % 2.0;
        """
        expect = Program([
                VarDecl("x", IntegerType(), BinExpr("%", BinExpr("/", BinExpr("*", IntegerLit(15), IntegerLit(5)), IntegerLit(3)), FloatLit(2.0)))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 241))

    def test_42(self):
        """test expression"""
        input = """
            x : integer = 15.5 * 5 / 3 % 2.0;
        """
        expect = Program([
                VarDecl("x", IntegerType(), BinExpr("%", BinExpr("/", BinExpr("*", FloatLit(15.5), IntegerLit(5)), IntegerLit(3)), FloatLit(2.0)))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 242))
    
    def test_43(self):
        """test expression"""
        input = """
            x : float = 15.5 * 5 / 3 % 2.0;
        """
        expect = Program([
                VarDecl("x", FloatType(), BinExpr("%", BinExpr("/", BinExpr("*", FloatLit(15.5), IntegerLit(5)), IntegerLit(3)), FloatLit(2.0)))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 243))
    
    def test_44(self):
        """test expression"""
        input = """
            x : float = 15.5 / 5 * 3 % 2.0;
        """
        expect = Program([
                VarDecl("x", FloatType(), BinExpr("%", BinExpr("*", BinExpr("/", FloatLit(15.5), IntegerLit(5)), IntegerLit(3)), FloatLit(2.0)))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 244))
    
    def test_45(self):
        """test expression"""
        input = """
            x : integer = !1 + !!!1;
        """
        expect = Program([
                VarDecl("x", IntegerType(), BinExpr("+", UnExpr("!", IntegerLit(1)), UnExpr("!", UnExpr("!", UnExpr("!", IntegerLit(1))))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 245))
    
    def test_46(self):
        """test expression"""
        input = """
            id : integer = !1;
        """
        expect = Program([
                VarDecl("id", IntegerType(), UnExpr("!", IntegerLit(1)))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 246))
    
    def test_47(self):
        """test expression"""
        input = """
            id : integer = !!!1;
        """
        expect = Program([
                VarDecl("id", IntegerType(), UnExpr("!", UnExpr("!", UnExpr("!", IntegerLit(1)))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 247))
    
    def test_48(self):
        """test expression"""
        input = """
            x : integer = -1 + ---1;
        """
        expect = Program([
                VarDecl("x", IntegerType(), BinExpr("+", UnExpr("-", IntegerLit(1)), UnExpr("-", UnExpr("-", UnExpr("-", IntegerLit(1))))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 248))

    def test_49(self):
        """test expression"""
        input = """
            x : integer = -2 / ---1;
        """
        expect = Program([
                VarDecl("x", IntegerType(), BinExpr("/", UnExpr("-", IntegerLit(2)), UnExpr("-", UnExpr("-", UnExpr("-", IntegerLit(1))))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 249))
    
    def test_50(self):
        """test expression"""
        input = """
            x : integer = -2 * ---1;
        """
        expect = Program([
                VarDecl("x", IntegerType(), BinExpr("*", UnExpr("-", IntegerLit(2)), UnExpr("-", UnExpr("-", UnExpr("-", IntegerLit(1))))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 250))

    def test_51(self):
        """test expression"""
        input = """
            x : integer = a[1+2] - a[3, 4];
            y : integer = a[1+2, a[3, 4]];
        """
        expect = Program([
                VarDecl("x", IntegerType(), BinExpr("-", ArrayCell("a", [BinExpr("+", IntegerLit(1), IntegerLit(2))]), ArrayCell("a", [IntegerLit(3), IntegerLit(4)]))),
                VarDecl("y", IntegerType(), ArrayCell("a", [BinExpr("+", IntegerLit(1), IntegerLit(2)), ArrayCell("a", [IntegerLit(3), IntegerLit(4)])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 251))
    
    def test_52(self):
        """test expression"""
        input = """
            x : integer = a[1+2] - a[3, 4];
            y : float = a[1+2, a[3, 4]];
        """
        expect = Program([
                VarDecl("x", IntegerType(), BinExpr("-", ArrayCell("a", [BinExpr("+", IntegerLit(1), IntegerLit(2))]), ArrayCell("a", [IntegerLit(3), IntegerLit(4)]))),
                VarDecl("y", FloatType(), ArrayCell("a", [BinExpr("+", IntegerLit(1), IntegerLit(2)), ArrayCell("a", [IntegerLit(3), IntegerLit(4)])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 252))

    def test_53(self):
        """test expression"""
        input = """
            x : float = a[1+2] - a[3, 4];
            y : float = a[1+2, a[3, 4]];
        """
        expect = Program([
                VarDecl("x", FloatType(), BinExpr("-", ArrayCell("a", [BinExpr("+", IntegerLit(1), IntegerLit(2))]), ArrayCell("a", [IntegerLit(3), IntegerLit(4)]))),
                VarDecl("y", FloatType(), ArrayCell("a", [BinExpr("+", IntegerLit(1), IntegerLit(2)), ArrayCell("a", [IntegerLit(3), IntegerLit(4)])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 253))
    
    def test_54(self):
        """test expression"""
        input = """
            x : float = (a > b - x(5+3, 3)) * x();
        """
        expect = Program([
                VarDecl("x", FloatType(), BinExpr("*", BinExpr(">", Id("a"), BinExpr("-", Id("b"), FuncCall("x", [BinExpr("+", IntegerLit(5), IntegerLit(3)), IntegerLit(3)]))), FuncCall("x", [])))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 254))
    
    def test_55(self):
        """test expression"""
        input = """
            x : integer = (a > b - x(5+3, 3)) * x();
        """
        expect = Program([
                VarDecl("x", IntegerType(), BinExpr("*", BinExpr(">", Id("a"), BinExpr("-", Id("b"), FuncCall("x", [BinExpr("+", IntegerLit(5), IntegerLit(3)), IntegerLit(3)]))), FuncCall("x", [])))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 255))
    
    def test_56(self):
        """test expression"""
        input = """
            x : float = (a < b - x(5+3, 3)) * x();
        """
        expect = Program([
                VarDecl("x", FloatType(), BinExpr("*", BinExpr("<", Id("a"), BinExpr("-", Id("b"), FuncCall("x", [BinExpr("+", IntegerLit(5), IntegerLit(3)), IntegerLit(3)]))), FuncCall("x", [])))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 256))
    
    def test_57(self):
        """test expression"""
        input = """
            x : float = {15/5, foo(), {1,2}};
        """
        expect = Program([
                VarDecl("x", FloatType(), ArrayLit([BinExpr("/", IntegerLit(15), IntegerLit(5)), FuncCall("foo", []), ArrayLit([IntegerLit(1), IntegerLit(2)])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 257))
    
    def test_58(self):
        """test expression"""
        input = """
            x : integer = {15/5, f(), {7,2}};
        """
        expect = Program([
                VarDecl("x", IntegerType(), ArrayLit([BinExpr("/", IntegerLit(15), IntegerLit(5)), FuncCall("f", []), ArrayLit([IntegerLit(7), IntegerLit(2)])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 258))
    
    def test_59(self):
        """test expression"""
        input = """
            x : float = {15/5, foo()};
        """
        expect = Program([
                VarDecl("x", FloatType(), ArrayLit([BinExpr("/", IntegerLit(15), IntegerLit(5)), FuncCall("foo", [])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 259))
    
    def test_60(self):
        """test expression"""
        input = """
            x : float = 1 * 2 + 3 > 4 / 2 :: 10 < !! --4;
        """
        expect = Program([
                VarDecl("x", FloatType(), BinExpr("::", BinExpr(">", BinExpr("+", BinExpr("*", IntegerLit(1), IntegerLit(2)), IntegerLit(3)), BinExpr("/", IntegerLit(4), IntegerLit(2))), BinExpr("<", IntegerLit(10), UnExpr("!", UnExpr("!", UnExpr("-", UnExpr("-", IntegerLit(4))))))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 260))
    
    def test_61(self):
        """test expression"""
        input = """
            x : float = 2 :: 10 < !! --4;
        """
        expect = Program([
            VarDecl("x", FloatType(), BinExpr("::", IntegerLit(2), BinExpr("<", IntegerLit(10), UnExpr("!", UnExpr("!", UnExpr("-", UnExpr("-", IntegerLit(4))))))))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 261))

    def test_62(self):
        """test expression"""
        input = """
            x : float = 10 < !! --4;
        """
        expect = Program([
                VarDecl("x", FloatType(), BinExpr("<", IntegerLit(10), UnExpr("!", UnExpr("!", UnExpr("-", UnExpr("-", IntegerLit(4)))))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 262))
    
    def test_63(self):
        """test Statement"""
        input = """
            a, b : integer = 4, 5;
            foo : function void () {
                
            }
        """
        expect = Program([
                VarDecl("a", IntegerType(), IntegerLit(4)),
                VarDecl("b", IntegerType(), IntegerLit(5)),
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 263))

    def test_64(self):
        """test Statement"""
        input = """
            a, b : float = 4, 5;
            foo : function void () {
                
            }
        """
        expect = Program([
                VarDecl("a", FloatType(), IntegerLit(4)),
                VarDecl("b", FloatType(), IntegerLit(5)),
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 264))
    
    def test_65(self):
        """test Statement"""
        input = """
            foo : function void () {
                a, b : integer = 4, 5;
                c, d : float;
            }
        """
        expect = Program([
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([VarDecl("a", IntegerType(), IntegerLit(4)), VarDecl("b", IntegerType(), IntegerLit(5)), VarDecl("c", FloatType()), VarDecl("d", FloatType())]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 265))
    
    def test_66(self):
        """test Statement"""
        input = """
            foo : function void () {
                x = 1;
                x[1.0] = 1;
            }
        """
        expect = Program([
            FuncDecl("foo", VoidType(), [], "None", BlockStmt([AssignStmt(Id("x"), IntegerLit(1)), AssignStmt(ArrayCell("x", [FloatLit(1.0)]), IntegerLit(1))]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 266))
    
    def test_67(self):
        """test Statement"""
        input = """
            foo : function void () {
                x = 1;
                x[1.0] = 1;
                x[1,2] = "!";
            }
        """
        expect = Program([
            FuncDecl("foo", VoidType(), [], "None", BlockStmt([AssignStmt(Id("x"), IntegerLit(1)), AssignStmt(ArrayCell("x", [FloatLit(1.0)]), IntegerLit(1)), AssignStmt(ArrayCell("x", [IntegerLit(1), IntegerLit(2)]), StringLit("!"))]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 267))
    
    def test_68(self):
        """test Statement"""
        input = """
            foo : function void () {
                x[1,2] = "!";
            }
        """
        expect = Program([
            FuncDecl("foo", VoidType(), [], "None", BlockStmt([AssignStmt(ArrayCell("x", [IntegerLit(1), IntegerLit(2)]), StringLit("!"))]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 268))
    
    def test_69(self):
        """test Statement"""
        input = """
            foo : function auto () {
                if (true) break;
                else {}
                
                if (true)
                    if(true) return;
                    return;
                
            }
        """
        expect = Program([
            FuncDecl("foo", AutoType(), [], "None", BlockStmt([IfStmt(BooleanLit(True), BreakStmt(), BlockStmt([])), IfStmt(BooleanLit(True), IfStmt(BooleanLit(True), ReturnStmt())), ReturnStmt()]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 269))
    
    def test_70(self):
        """test Statement"""
        input = """
            foo : function auto () {
                if (true) break;
                else {}
                
                if (true)
                    if(true) return;
                    else continue;
                else break;
                
            }
        """
        expect = Program([
            FuncDecl("foo", AutoType(), [], "None", BlockStmt([IfStmt(BooleanLit(True), BreakStmt(), BlockStmt([])), IfStmt(BooleanLit(True), IfStmt(BooleanLit(True), ReturnStmt(), ContinueStmt()), BreakStmt())]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 270))
    
    def test_71(self):
        """test Statement"""
        input = """
            foo : function auto () {
                if (true) break;
                else {}
                
            }
        """
        expect = Program([
            FuncDecl("foo", AutoType(), [], "None", BlockStmt([IfStmt(BooleanLit(True), BreakStmt(), BlockStmt([]))]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 271))
    
    def test_72(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                if (true) return;
            }
        """
        expect = Program([
            FuncDecl("foo", AutoType(), [], "None", BlockStmt([IfStmt(BooleanLit(True), ReturnStmt())]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 272))
    
    def test_73(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                return;
                return 15 + 3;
            }
        """
        expect = Program([
                    FuncDecl("foo", AutoType(), [], "None", BlockStmt([ReturnStmt(), ReturnStmt(BinExpr("+", IntegerLit(15), IntegerLit(3)))]))
                ])
        self.assertTrue(TestAST.test(input, str(expect), 273))
    
    def test_74(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                return;
                return 15 / 3;
            }
        """
        expect = Program([
                    FuncDecl("foo", AutoType(), [], "None", BlockStmt([ReturnStmt(), ReturnStmt(BinExpr("/", IntegerLit(15), IntegerLit(3)))]))
                ])
        self.assertTrue(TestAST.test(input, str(expect), 274))
    
    def test_75(self):
        """test Statement"""
        input = """
            foo : function void () {  
                return;
                return 15 % 3;
            }
        """
        expect = Program([
                    FuncDecl("foo", VoidType(), [], "None", BlockStmt([ReturnStmt(), ReturnStmt(BinExpr("%", IntegerLit(15), IntegerLit(3)))]))
                ])
        self.assertTrue(TestAST.test(input, str(expect), 275))
    
    def test_76(self):
        """test Statement"""
        input = """
            foo : function void () {  
                return;
                return 15 > 3;
            }
        """
        expect = Program([
                    FuncDecl("foo", VoidType(), [], "None", BlockStmt([ReturnStmt(), ReturnStmt(BinExpr(">", IntegerLit(15), IntegerLit(3)))]))
                ])
        self.assertTrue(TestAST.test(input, str(expect), 276))
    
    def test_77(self):  
        """test Statement"""
        input = """
            foo : function void () {  
                return;
                return 15 >= 3;
            }
        """
        expect = Program([
                    FuncDecl("foo", VoidType(), [], "None", BlockStmt([ReturnStmt(), ReturnStmt(BinExpr(">=", IntegerLit(15), IntegerLit(3)))]))
                ])
        self.assertTrue(TestAST.test(input, str(expect), 277))
    
    def test_78(self):
        """test Statement"""
        input = """
            foo : function void () {  
                return;
                return 15 == 3;
            }
        """
        expect = Program([
                    FuncDecl("foo", VoidType(), [], "None", BlockStmt([ReturnStmt(), ReturnStmt(BinExpr("==", IntegerLit(15), IntegerLit(3)))]))
                ])
        self.assertTrue(TestAST.test(input, str(expect), 278))
    
    def test_79(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                foo();
                foo(6/3, 3);
            }
        """
        expect = Program([
                FuncDecl("foo", AutoType(), [], "None", BlockStmt([CallStmt("foo",[]), CallStmt("foo",[BinExpr("/", IntegerLit(6), IntegerLit(3)), IntegerLit(3)])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 279))
    
    def test_80(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                foo();
                foo(6*5, 3);
            }
        """
        expect = Program([
                FuncDecl("foo", AutoType(), [], "None", BlockStmt([CallStmt("foo",[]), CallStmt("foo",[BinExpr("*", IntegerLit(6), IntegerLit(5)), IntegerLit(3)])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 280))
    
    def test_81(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                {
                    break;
                    {{{}}}
                }
            }
        """
        expect = Program([
                FuncDecl("foo", AutoType(), [], "None", BlockStmt([BlockStmt([BreakStmt(), BlockStmt([BlockStmt([BlockStmt([])])])])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 281))
    
    def test_82(self):
        """test Statement"""
        input = """
            foo : function void () {  
                {
                    continue;
                    {{{}}}
                }
            }
        """
        expect = Program([
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([BlockStmt([ContinueStmt(), BlockStmt([BlockStmt([BlockStmt([])])])])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 282))

    def test_83(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                {
                    break;
                    continue;
                    {{{}}}
                }
            }
        """
        expect = Program([
                FuncDecl("foo", AutoType(), [], "None", BlockStmt([BlockStmt([BreakStmt(), ContinueStmt(), BlockStmt([BlockStmt([BlockStmt([])])])])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 283))
    
    def test_84(self):
        """test Statement"""
        input = """
            foo : function void () {  
                {
                    x, y : float;
                    z, t : float = 1, 2;
                    e : string = "$$";
                }
            }
        """
        expect = Program([
                    FuncDecl("foo", VoidType(), [], "None", BlockStmt([BlockStmt([VarDecl("x", FloatType()), VarDecl("y", FloatType()), VarDecl("z", FloatType(), IntegerLit(1)), VarDecl("t", FloatType(), IntegerLit(2)), VarDecl("e", StringType(), StringLit("$$"))])]))
                ])
        self.assertTrue(TestAST.test(input, str(expect), 284))
    
    def test_85(self):
        """test Statement"""
        input = """
            foo : function void () {  
                {
                    x, y : float;
                    z, t : float = 15, 5;
                    e : string = "$$#####";
                }
            }
        """
        expect = Program([
                    FuncDecl("foo", VoidType(), [], "None", BlockStmt([BlockStmt([VarDecl("x", FloatType()), VarDecl("y", FloatType()), VarDecl("z", FloatType(), IntegerLit(15)), VarDecl("t", FloatType(), IntegerLit(5)), VarDecl("e", StringType(), StringLit("$$#####"))])]))
                ])
        self.assertTrue(TestAST.test(input, str(expect), 285))
        
    def test_86(self):
        """test Statement"""
        input = """
            foo : function void () {  
                {
                    x, y : integer;
                    z, t : float = 1, 2;
                    e : string = "$$";
                }
            }
        """
        expect = Program([
                    FuncDecl("foo", VoidType(), [], "None", BlockStmt([BlockStmt([VarDecl("x", IntegerType()), VarDecl("y", IntegerType()), VarDecl("z", FloatType(), IntegerLit(1)), VarDecl("t", FloatType(), IntegerLit(2)), VarDecl("e", StringType(), StringLit("$$"))])]))
                ])
        self.assertTrue(TestAST.test(input, str(expect), 286))
    
    def test_87(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                for (i = 1, i < 10, i + 2) {
                    readInt(i);
                }
            }

        """
        expect = Program([
                FuncDecl("foo", AutoType(), [], "None", BlockStmt([ForStmt(AssignStmt(Id("i"), IntegerLit(1)), BinExpr("<", Id("i"), IntegerLit(10)), BinExpr("+", Id("i"), IntegerLit(2)), BlockStmt([CallStmt("readInt",[Id("i")])]))]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 287))
    
    def test_88(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                for (i = 1, i < 10, i + 2) {
                    writeInt(i);
                }
            }

        """
        expect = Program([
                FuncDecl("foo", AutoType(), [], "None", BlockStmt([ForStmt(AssignStmt(Id("i"), IntegerLit(1)), BinExpr("<", Id("i"), IntegerLit(10)), BinExpr("+", Id("i"), IntegerLit(2)), BlockStmt([CallStmt("writeInt",[Id("i")])]))]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 288))
    
    def test_89(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                for (i = 1, i < 10, i + 2) {
                    printInt(i);
                }
            }

        """
        expect = Program([
                FuncDecl("foo", AutoType(), [], "None", BlockStmt([ForStmt(AssignStmt(Id("i"), IntegerLit(1)), BinExpr("<", Id("i"), IntegerLit(10)), BinExpr("+", Id("i"), IntegerLit(2)), BlockStmt([CallStmt("printInt",[Id("i")])]))]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 289))
    
    def test_90(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                for (i = 1, i <= 5, i + 1) break;
            }

        """
        expect = Program([
                FuncDecl("foo", AutoType(), [], "None", BlockStmt([ForStmt(AssignStmt(Id("i"), IntegerLit(1)), BinExpr("<=", Id("i"), IntegerLit(5)), BinExpr("+", Id("i"), IntegerLit(1)), BreakStmt())]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 290))
    
    def test_91(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                do
                {
                }
                while(12.001);
            }
        """
        expect = Program([
                FuncDecl("foo", AutoType(), [], "None", BlockStmt([DoWhileStmt(FloatLit(12.001), BlockStmt([]))]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 291))
    
    def test_92(self):
        """test Statement"""
        input = """
            foo : function void () {  
                do
                {
                    return;
                }
                while(11.0);
            }
        """
        expect = Program([
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([DoWhileStmt(FloatLit(11.0), BlockStmt([ReturnStmt()]))]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 292))
    
    def test_93(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                while (true) break;
            }
        """
        expect = Program([
                FuncDecl("foo", AutoType(), [], "None", BlockStmt([WhileStmt(BooleanLit(True), BreakStmt())]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 293))
    
    def test_94(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                while (false) {break;}
            }
        """
        expect = Program([
                FuncDecl("foo", AutoType(), [], "None", BlockStmt([WhileStmt(BooleanLit(False), BlockStmt([BreakStmt()]))]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 294))
    
    def test_95(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                while (false) {}
                break;
            }
        """
        expect = Program([
                FuncDecl("foo", AutoType(), [], "None", BlockStmt([WhileStmt(BooleanLit(False), BlockStmt([])), BreakStmt()]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), 295))

    def test_96(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                for (i[1+2] = 1, i <= 5, i + 1) return;
            }
        """
        expect = Program([
            FuncDecl("foo", AutoType(), [], "None", BlockStmt([ForStmt(AssignStmt(ArrayCell("i", [BinExpr("+", IntegerLit(1), IntegerLit(2))]), IntegerLit(1)), BinExpr("<=", Id("i"), IntegerLit(5)), BinExpr("+", Id("i"), IntegerLit(1)), ReturnStmt())]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 296))
    
    def test_97(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                for (i[1+2] = 1, i <= 5, i + 1) break;
            }
        """
        expect = Program([
            FuncDecl("foo", AutoType(), [], "None", BlockStmt([ForStmt(AssignStmt(ArrayCell("i", [BinExpr("+", IntegerLit(1), IntegerLit(2))]), IntegerLit(1)), BinExpr("<=", Id("i"), IntegerLit(5)), BinExpr("+", Id("i"), IntegerLit(1)), BreakStmt())]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 297))
    
    def test_98(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                for (i[1+2] = 10, i > 0, i - 1) return;
            }
        """
        expect = Program([
            FuncDecl("foo", AutoType(), [], "None", BlockStmt([ForStmt(AssignStmt(ArrayCell("i", [BinExpr("+", IntegerLit(1), IntegerLit(2))]), IntegerLit(10)), BinExpr(">", Id("i"), IntegerLit(0)), BinExpr("-", Id("i"), IntegerLit(1)), ReturnStmt())]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 298))
    
    def test_99(self):
        """test Statement"""
        input = """
            foo : function void () {  
                for (i[1+2] = 10, i > 0, i - 1) return;
            }
        """
        expect = Program([
            FuncDecl("foo", VoidType(), [], "None", BlockStmt([ForStmt(AssignStmt(ArrayCell("i", [BinExpr("+", IntegerLit(1), IntegerLit(2))]), IntegerLit(10)), BinExpr(">", Id("i"), IntegerLit(0)), BinExpr("-", Id("i"), IntegerLit(1)), ReturnStmt())]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 299))
    
    def test_100(self):
        """test Statement"""
        input = """
            foo : function auto () {  
                for (i[1*2] = 10, i > 0, i - 1) return;
            }
        """
        expect = Program([
            FuncDecl("foo", AutoType(), [], "None", BlockStmt([ForStmt(AssignStmt(ArrayCell("i", [BinExpr("*", IntegerLit(1), IntegerLit(2))]), IntegerLit(10)), BinExpr(">", Id("i"), IntegerLit(0)), BinExpr("-", Id("i"), IntegerLit(1)), ReturnStmt())]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), 300))


