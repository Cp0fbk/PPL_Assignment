# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#boollit.
    def visitBoollit(self, ctx:MT22Parser.BoollitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprprime.
    def visitExprprime(self, ctx:MT22Parser.ExprprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#shortform.
    def visitShortform(self, ctx:MT22Parser.ShortformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init.
    def visitInit(self, ctx:MT22Parser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varlist.
    def visitVarlist(self, ctx:MT22Parser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramprime.
    def visitParamprime(self, ctx:MT22Parser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_op.
    def visitIndex_op(self, ctx:MT22Parser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_call.
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arglist.
    def visitArglist(self, ctx:MT22Parser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argprime.
    def visitArgprime(self, ctx:MT22Parser.ArgprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignment_statement.
    def visitAssignment_statement(self, ctx:MT22Parser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar.
    def visitScalar(self, ctx:MT22Parser.ScalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_statement.
    def visitIf_statement(self, ctx:MT22Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#else_st.
    def visitElse_st(self, ctx:MT22Parser.Else_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_statement.
    def visitFor_statement(self, ctx:MT22Parser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr.
    def visitInit_expr(self, ctx:MT22Parser.Init_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr1.
    def visitInit_expr1(self, ctx:MT22Parser.Init_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr2.
    def visitInit_expr2(self, ctx:MT22Parser.Init_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr3.
    def visitInit_expr3(self, ctx:MT22Parser.Init_expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_statement.
    def visitWhile_statement(self, ctx:MT22Parser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_statement.
    def visitDo_while_statement(self, ctx:MT22Parser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_statement.
    def visitBreak_statement(self, ctx:MT22Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_statement.
    def visitContinue_statement(self, ctx:MT22Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_statement.
    def visitReturn_statement(self, ctx:MT22Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_statement.
    def visitCall_statement(self, ctx:MT22Parser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_statement.
    def visitBlock_statement(self, ctx:MT22Parser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blist.
    def visitBlist(self, ctx:MT22Parser.BlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typee.
    def visitTypee(self, ctx:MT22Parser.TypeeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#elem_type.
    def visitElem_type(self, ctx:MT22Parser.Elem_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimen.
    def visitDimen(self, ctx:MT22Parser.DimenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_type.
    def visitFunc_type(self, ctx:MT22Parser.Func_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#spec_func.
    def visitSpec_func(self, ctx:MT22Parser.Spec_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readI.
    def visitReadI(self, ctx:MT22Parser.ReadIContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printI.
    def visitPrintI(self, ctx:MT22Parser.PrintIContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readF.
    def visitReadF(self, ctx:MT22Parser.ReadFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#writeF.
    def visitWriteF(self, ctx:MT22Parser.WriteFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readB.
    def visitReadB(self, ctx:MT22Parser.ReadBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printB.
    def visitPrintB(self, ctx:MT22Parser.PrintBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readS.
    def visitReadS(self, ctx:MT22Parser.ReadSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printS.
    def visitPrintS(self, ctx:MT22Parser.PrintSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#superr.
    def visitSuperr(self, ctx:MT22Parser.SuperrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#preventD.
    def visitPreventD(self, ctx:MT22Parser.PreventDContext):
        return self.visitChildren(ctx)



del MT22Parser