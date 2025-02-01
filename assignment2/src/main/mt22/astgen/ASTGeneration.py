from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *

#id: 2212631
class ASTGeneration(MT22Visitor):
    # Visit a parse tree produced by MT22Parser#program.
    # program: decllist  EOF ;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))
    
    # Visit a parse tree produced by MT22Parser#boollit.
    # boollit: 'true' | 'false';
    def visitBoollit(self, ctx:MT22Parser.BoollitContext):
        if ctx.getText() == 'true':
            return True
        return False


    # Visit a parse tree produced by MT22Parser#arraylit.
    #arraylit: LP exprlist RP;
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.exprlist()))


    # Visit a parse tree produced by MT22Parser#exprlist.
    #exprlist: exprprime | ;
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.exprprime())


    # Visit a parse tree produced by MT22Parser#exprprime.
    #exprprime: expr COMMA exprprime | expr;
    def visitExprprime(self, ctx:MT22Parser.ExprprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprprime())


    # Visit a parse tree produced by MT22Parser#literal.
    #literal: INTLIT | FLOATLIT | boollit | STRINGLIT | arraylit;
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.boollit():
            return BooleanLit(ctx.boollit().getText() == "true")
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        return self.visit(ctx.arraylit())

    # Visit a parse tree produced by MT22Parser#decllist.
    # decllist: decl decllist | decl;
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        if ctx.getChildCount() == 1:
            return list(self.visit(ctx.decl()))
        return list(self.visit(ctx.decl())) + self.visit(ctx.decllist())

    # Visit a parse tree produced by MT22Parser#decl.
    # decl: vardecl | funcdecl;
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        if ctx.vardecl(): 
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())

    # Visit a parse tree produced by MT22Parser#vardecl.
    # vardecl: (shortform | init) SEMI;
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        if ctx.shortform(): 
            return self.visit(ctx.shortform())
        return self.visit(ctx.init())


    # Visit a parse tree produced by MT22Parser#shortform.
    # shortform: idlist COLON typee;
    def visitShortform(self, ctx:MT22Parser.ShortformContext):
        ids = self.visit(ctx.idlist())
        return [VarDecl(x,self.visit(ctx.typee())) for x in ids]


    # Visit a parse tree produced by MT22Parser#int.
    # init: ID varlist expr;
    # varlist: COMMA ID varlist expr COMMA | COLON typee ASSIGN;
    def visitInit(self, ctx:MT22Parser.InitContext):
        name = [ctx.ID().getText()]
        expr = [self.visit(ctx.expr())]
        ctx = ctx.varlist()
        while ctx.getChildCount()==5:
            name += [ctx.ID().getText()]
            expr += [self.visit(ctx.expr())]
            ctx = ctx.varlist()
        typ = self.visit(ctx.typee())
        expr = expr[::-1]
        return [VarDecl(x, typ, y) for x, y in zip(name, expr)]


    # Visit a parse tree produced by MT22Parser#idlist.
    # idlist: ID COMMA idlist | ID;
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1: 
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.idlist())


    # Visit a parse tree produced by MT22Parser#param.
    # param: INHERIT? OUT? ID COLON typee;
    def visitParam(self, ctx:MT22Parser.ParamContext):
        name = ctx.ID().getText()
        typee = self.visit(ctx.typee())
        inherit = ctx.INHERIT() is not None
        out = ctx.OUT() is not None
        return ParamDecl(name, typee, out, inherit)
    

    # Visit a parse tree produced by MT22Parser#funcdecl.
    #funcdecl: ID COLON FUNC func_type LB paramlist RB (INHERIT ID)? block_statement;
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        name = ctx.ID(0).getText()
        typ = self.visit(ctx.func_type())
        params = self.visit(ctx.paramlist())
        if ctx.INHERIT():
            inhr = ctx.ID(1).getText()
        else:
            inhr = None
        stmt = self.visit(ctx.block_statement())
        return [FuncDecl(name,typ,params,inhr,stmt)]

    # Visit a parse tree produced by MT22Parser#paramlist.
    # paramlist: paramprime | ;
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paramprime())


    # Visit a parse tree produced by MT22Parser#paramprime.
    #paramprime: param COMMA paramprime | param;
    def visitParamprime(self, ctx:MT22Parser.ParamprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        return [self.visit(ctx.param())] + self.visit(ctx.paramprime())


    # Visit a parse tree produced by MT22Parser#index_op.
    # index_op: ID LS exprprime RS;
    def visitIndex_op(self, ctx:MT22Parser.Index_opContext):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.exprprime()))


    # Visit a parse tree produced by MT22Parser#func_call.
    #func_call: ID LB arglist RB;
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        return FuncCall(ctx.ID().getText(), self.visit(ctx.arglist()))

    # Visit a parse tree produced by MT22Parser#arglist.
    #arglist: argprime | ;
    def visitArglist(self, ctx:MT22Parser.ArglistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.argprime())
        return []


    # Visit a parse tree produced by MT22Parser#argprime.
    #argprime: expr COMMA argprime | expr;
    def visitArgprime(self, ctx:MT22Parser.ArgprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.argprime())


    # Visit a parse tree produced by MT22Parser#expr.
    #expr: expr1 CONCAT expr1 | expr1;
    
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.expr1(0))
        op = ctx.CONCAT().getText()
        left = self.visit(ctx.expr1(0))
        right = self.visit(ctx.expr1(1))
        return BinExpr(op, left, right)


    # Visit a parse tree produced by MT22Parser#expr1.
    # expr1: expr2 (EQ | NOT_EQ | LT | GT | LTE | GTE) expr2 | expr2;
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.expr2(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr2(0))
        right = self.visit(ctx.expr2(1))
        return BinExpr(op, left, right)


    # Visit a parse tree produced by MT22Parser#expr2.
    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        return BinExpr(op, left, right)


    # Visit a parse tree produced by MT22Parser#expr3.
    # expr3: expr3 (ADD | SUB) expr4 | expr4;
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        return BinExpr(op, left, right)


    # Visit a parse tree produced by MT22Parser#expr4.
    # expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())
        return BinExpr(op, left, right)


    # Visit a parse tree produced by MT22Parser#expr5.
    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        if ctx.NOT():
            return UnExpr(ctx.NOT().getText(),self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())


    # Visit a parse tree produced by MT22Parser#expr6.
    # expr6: SUB expr6 | expr7;
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        if ctx.SUB():
            return UnExpr(ctx.SUB().getText(),self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())


    # Visit a parse tree produced by MT22Parser#expr7.
    # expr7: index_op | expr8;
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        if ctx.index_op():
            return self.visit(ctx.index_op())
        return self.visit(ctx.expr8())


    # Visit a parse tree produced by MT22Parser#expr8.
    # expr8: ID | literal | LB expr RB | ID LB exprlist RB;
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.exprlist():
            return FuncCall(ctx.ID().getText(),self.visit(ctx.exprlist()))
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#assignment_statement.
    # assignment_statement: scalar ASSIGN expr SEMI;
    def visitAssignment_statement(self, ctx:MT22Parser.Assignment_statementContext):
        return AssignStmt(self.visit(ctx.scalar()),self.visit(ctx.expr()))


    # Visit a parse tree produced by MT22Parser#scalar.
    #scalar: ID | index_op;
    def visitScalar(self, ctx:MT22Parser.ScalarContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.index_op())


    # Visit a parse tree produced by MT22Parser#if_statement.
    #if_statement: IF LB expr RB statement else_st;
    def visitIf_statement(self, ctx:MT22Parser.If_statementContext):
        cd = self.visit(ctx.expr())
        stmt = self.visit(ctx.statement())
        estmt = self.visit(ctx.else_st())
        return IfStmt(cd, stmt, estmt)


    # Visit a parse tree produced by MT22Parser#else_st.
    #else_st: ELSE statement | ;
    def visitElse_st(self, ctx:MT22Parser.Else_stContext):
        if ctx.ELSE():
            return self.visit(ctx.statement())
        return None

    # Visit a parse tree produced by MT22Parser#for_statement.
    # for_statement: FOR LB scalar ASSIGN init_expr COMMA expr COMMA expr RB statement;
    def visitFor_statement(self, ctx:MT22Parser.For_statementContext):
        cd = self.visit(ctx.expr()[0])
        upd = self.visit(ctx.expr()[1])
        stmt = self.visit(ctx.statement())
        assignstmt = AssignStmt(self.visit(ctx.scalar()),self.visit(ctx.init_expr()))
        return ForStmt(assignstmt,cd,upd,stmt)


    # Visit a parse tree produced by MT22Parser#init_expr.
    # init_expr: init_expr (ADD | SUB) init_expr1 | init_expr1;
    def visitInit_expr(self, ctx:MT22Parser.Init_exprContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.init_expr1())
        left = self.visit(ctx.init_expr())
        right = self.visit(ctx.init_expr1())
        op = ctx.getChild(1).getText()
        return BinExpr(op,left,right)


    # Visit a parse tree produced by MT22Parser#init_expr1.
    # init_expr1: init_expr1 (MUL | DIV | MOD) init_expr2 | init_expr2;
    def visitInit_expr1(self, ctx:MT22Parser.Init_expr1Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.init_expr2())
        left = self.visit(ctx.init_expr1())
        right = self.visit(ctx.init_expr2())
        op = ctx.getChild(1).getText()
        return BinExpr(op,left,right)


    # Visit a parse tree produced by MT22Parser#init_expr2.
    # init_expr2: SUB init_expr2 | init_expr3;
    def visitInit_expr2(self, ctx:MT22Parser.Init_expr2Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.init_expr3())
        return UnExpr(ctx.SUB().getText(),self.visit(ctx.init_expr2()))


    # Visit a parse tree produced by MT22Parser#init_expr3.
    # init_expr3:  LB expr RB | INTLIT;
    def visitInit_expr3(self, ctx:MT22Parser.Init_expr3Context):
        if ctx.getChildCount()==1:
            return IntegerLit(int(ctx.INTLIT().getText()))
        return self.visit(ctx.expr())


    # Visit a parse tree produced by MT22Parser#while_statement.
    #while_statement: WHILE LB expr RB statement;
    def visitWhile_statement(self, ctx:MT22Parser.While_statementContext):
        return WhileStmt(self.visit(ctx.expr()),self.visit(ctx.statement()))


    # Visit a parse tree produced by MT22Parser#do_while_statement.
    #do_while_statement: DO block_statement WHILE LB expr RB SEMI;
    def visitDo_while_statement(self, ctx:MT22Parser.Do_while_statementContext):
        return DoWhileStmt(self.visit(ctx.expr()),self.visit(ctx.block_statement()))


    # Visit a parse tree produced by MT22Parser#break_statement.
    # break_statement: BREAK SEMI;
    def visitBreak_statement(self, ctx:MT22Parser.Break_statementContext):
        return BreakStmt()


    # Visit a parse tree produced by MT22Parser#continue_statement.
    # continue_statement: CONTINUE SEMI;
    def visitContinue_statement(self, ctx:MT22Parser.Continue_statementContext):
        return ContinueStmt()


    # Visit a parse tree produced by MT22Parser#return_statement.
    # return_statement: RETURN expr? SEMI;
    def visitReturn_statement(self, ctx:MT22Parser.Return_statementContext):
        if ctx.getChildCount() == 3:
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt(None)


    # Visit a parse tree produced by MT22Parser#call_statement.
    #call_statement: spec_func SEMI | func_call SEMI;
    def visitCall_statement(self, ctx:MT22Parser.Call_statementContext):
        if ctx.spec_func():
            ctx = ctx.spec_func()
            ctx = ctx.getChild(0)
            name = ctx.getChild(0).getText()
            exp = []
            if name in {"printInteger", "printBoolean", "printString", "writeFloat"}:
                exp.append(self.visit(ctx.expr()))
            elif name == "super":
                exp.extend(self.visit(ctx.exprlist()))
            return CallStmt(name, exp)
        ctx = ctx.func_call()
        name = ctx.ID().getText()
        arg = self.visit(ctx.arglist())
        return CallStmt(name, arg)


    # Visit a parse tree produced by MT22Parser#block_statement.
    # block_statement: LP blist RP;
    def visitBlock_statement(self, ctx:MT22Parser.Block_statementContext):
        return BlockStmt(self.visit(ctx.blist()))


    # Visit a parse tree produced by MT22Parser#blist.
    # blist: statement blist | vardecl blist | ;
    def visitBlist(self, ctx:MT22Parser.BlistContext):
        if ctx.statement():
            return [self.visit(ctx.statement())] + self.visit(ctx.blist())  
        elif ctx.getChildCount() == 0: 
            return []
        return self.visit(ctx.vardecl()) + self.visit(ctx.blist())

    # Visit a parse tree produced by MT22Parser#typee.
    #typee: BOOL | INT | FLOAT | STRING | AUTO | array_type;
    def visitTypee(self, ctx:MT22Parser.TypeeContext):
        if ctx.BOOL():
            return BooleanType()
        elif ctx.INT():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.AUTO():
            return AutoType()
        return self.visit(ctx.array_type())

    # Visit a parse tree produced by MT22Parser#elem_type.
    #elem_type: INT | FLOAT | STRING | BOOL;
    def visitElem_type(self, ctx:MT22Parser.Elem_typeContext):
        if ctx.BOOL():
            return BooleanType()
        elif ctx.INT():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()


    # Visit a parse tree produced by MT22Parser#array_type.
    #array_type: ARRAY LS dimen RS OF elem_type;
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return ArrayType(self.visit(ctx.dimen()), self.visit(ctx.elem_type()))


    # Visit a parse tree produced by MT22Parser#dimen.
    #dimen: INTLIT COMMA dimen | INTLIT;
    def visitDimen(self, ctx:MT22Parser.DimenContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimen())


    # Visit a parse tree produced by MT22Parser#func_type.
    #func_type: BOOL | INT | FLOAT | STRING | AUTO | array_type | VOID;
    def visitFunc_type(self, ctx:MT22Parser.Func_typeContext):
        if ctx.BOOL():
            return BooleanType()
        elif ctx.INT():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.AUTO():
            return AutoType()
        elif ctx.VOID():
            return VoidType()
        return self.visit(ctx.array_type())


    # Visit a parse tree produced by MT22Parser#spec_func.
    #spec_func: readI| printI | readF | writeF | readB | printB | readS | printS | superr | preventD;
    def visitSpec_func(self, ctx:MT22Parser.Spec_funcContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#readI.
    # readI: READI LB RB;
    def visitReadI(self, ctx:MT22Parser.ReadIContext):
        return FuncCall(ctx.READI().getText(), [])


    # Visit a parse tree produced by MT22Parser#printI.
    # printI: PRINTI LB expr RB;
    def visitPrintI(self, ctx:MT22Parser.PrintIContext):
        return FuncCall(ctx.PRINTI().getText(), self.visit(ctx.expr()))


    # Visit a parse tree produced by MT22Parser#readF.
    # readF: READF LB RB;
    def visitReadF(self, ctx:MT22Parser.ReadFContext):
        return FuncCall(ctx.READF().getText(), [])


    # Visit a parse tree produced by MT22Parser#writeF.
    # writeF: WRITEF LB expr RB;
    def visitWriteF(self, ctx:MT22Parser.WriteFContext):
        return FuncCall(ctx.WRITEB().getText(), self.visit(ctx.expr()))


    # Visit a parse tree produced by MT22Parser#readB.
    # readB: READB LB RB;
    def visitReadB(self, ctx:MT22Parser.ReadBContext):
        return FuncCall(ctx.READB().getText(), [])


    # Visit a parse tree produced by MT22Parser#printB.
    #printB: PRINTB LB expr RB;
    def visitPrintB(self, ctx:MT22Parser.PrintBContext):
        return FuncCall(ctx.PRINTB().getText(), self.visit(ctx.expr()))


    # Visit a parse tree produced by MT22Parser#readS.
    # readS: READS LB RB;
    def visitReadS(self, ctx:MT22Parser.ReadSContext):
        return FuncCall(ctx.READS().getText(),[])


    # Visit a parse tree produced by MT22Parser#printS.
    #printS: PRINTS LB expr RB;
    def visitPrintS(self, ctx:MT22Parser.PrintSContext):
        return FuncCall(ctx.PRINTS().getText(), self.visit(ctx.expr()))


    # Visit a parse tree produced by MT22Parser#superr.
    #superr: SUPER LB exprlist RB;
    def visitSuperr(self, ctx:MT22Parser.SuperrContext):
        return FuncCall(ctx.SUPER().getText(), self.visit(ctx.exprlist()))


    # Visit a parse tree produced by MT22Parser#preventD.
    #preventD: PREVENTDEFAULT LB RB;
    def visitPreventD(self, ctx:MT22Parser.PreventDContext):
        return FuncCall(ctx.PREVENTDEFAULT().getText(),[])
