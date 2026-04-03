/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_BROLANG_PARSER_TAB_H_INCLUDED
# define YY_YY_BROLANG_PARSER_TAB_H_INCLUDED
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif
#line 1 "brolang_parser.y"

#include "parser_utils.h"

#line 53 "brolang_parser.tab.h"

#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    HIBRO = 258,                   /* HIBRO  */
    BYEBRO = 259,                  /* BYEBRO  */
    BRO = 260,                     /* BRO  */
    PAKKA = 261,                   /* PAKKA  */
    NUM = 262,                     /* NUM  */
    STR = 263,                     /* STR  */
    BOOL = 264,                    /* BOOL  */
    NALLA = 265,                   /* NALLA  */
    SAHI = 266,                    /* SAHI  */
    GALAT = 267,                   /* GALAT  */
    NIL = 268,                     /* NIL  */
    BOLBRO = 269,                  /* BOLBRO  */
    BROASSERT = 270,               /* BROASSERT  */
    AGARBRO = 271,                 /* AGARBRO  */
    NAITOBRO = 272,                /* NAITOBRO  */
    WARNABRO = 273,                /* WARNABRO  */
    JABTAKBRO = 274,               /* JABTAKBRO  */
    BASKARBRO = 275,               /* BASKARBRO  */
    AGLADEHBRO = 276,              /* AGLADEHBRO  */
    ADD_ASSIGN = 277,              /* ADD_ASSIGN  */
    SUB_ASSIGN = 278,              /* SUB_ASSIGN  */
    MUL_ASSIGN = 279,              /* MUL_ASSIGN  */
    DIV_ASSIGN = 280,              /* DIV_ASSIGN  */
    EQ = 281,                      /* EQ  */
    NEQ = 282,                     /* NEQ  */
    LE = 283,                      /* LE  */
    GE = 284,                      /* GE  */
    LT = 285,                      /* LT  */
    GT = 286,                      /* GT  */
    ASSIGN = 287,                  /* ASSIGN  */
    PLUS = 288,                    /* PLUS  */
    MINUS = 289,                   /* MINUS  */
    MUL = 290,                     /* MUL  */
    DIV = 291,                     /* DIV  */
    SEMICOLON = 292,               /* SEMICOLON  */
    COMMA = 293,                   /* COMMA  */
    LPAREN = 294,                  /* LPAREN  */
    RPAREN = 295,                  /* RPAREN  */
    LBRACE = 296,                  /* LBRACE  */
    RBRACE = 297,                  /* RBRACE  */
    IDENTIFIER = 298,              /* IDENTIFIER  */
    NUMBER_LITERAL = 299,          /* NUMBER_LITERAL  */
    STRING_LITERAL = 300           /* STRING_LITERAL  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 22 "brolang_parser.y"

    char* str;
    ParseTreeNode* node;

#line 120 "brolang_parser.tab.h"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif 
