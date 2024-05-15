
tokens = [
    'EOL', 'BOOL', 'CHOICE', 'COMMENT', 'CONFIG', 'DEF_BOOL', 'DEF_TRISTATE', 'DEFAULT', 'DEPENDS', 'ENDCHOICE', 
    'ENDIF', 'ENDMENU', 'HELP', 'HEX', 'IF', 'IMPLY', 'INT', 'MAINMENU', 'MENU', 'MENUCONFIG', 'MODULES', 'ON',
    'OPTIONAL', 'PROMPT', 'RANGE', 'SELECT', 'SOURCE', 'STRING', 'TRISTATE', 'VISIBLE', 'OR', 'AND', 'EQUAL', 
    'UNEQUAL', 'LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL', 'NOT', 'OPEN_PAREN', 'CLOSE_PAREN', 'COLON_EQUAL',
    'PLUS_EQUAL', 'COMMENT_LEX', 'WHITESPACES_LEX', 'ESCAPED_NEW_LINE_LEX', 'STRING_LEX'
]


t_EOL = r'\n'
t_BOOL = r"bool"
t_CHOICE = r"choice"
t_COMMENT = r"comment"
t_CONFIG = r"config"
t_DEF_BOOL = r"def_bool"
t_DEF_TRISTATE = r"def_tristate"
t_DEFAULT = r"default"
t_DEPENDS = r"depends"
t_ENDCHOICE = r"endchoice"
t_ENDIF = r"endif"
t_ENDMENU = r"endmenu"
t_HELP = r"help"
t_HEX = r"hex"
t_IF = r"if"
t_IMPLY = r"imply"
t_INT = r"int"
t_MAINMENU = r"mainmenu"
t_MENU = r"menu"
t_MENUCONFIG = r"menuconfig"
t_MODULES = r"modules"
t_ON = r"on"
t_OPTIONAL = r"optional"
t_PROMPT = r"prompt"
t_RANGE = r"range"
t_SELECT = r"select"
t_SOURCE = r"source"
t_STRING = r"string"
t_TRISTATE = r"tristate"
t_VISIBLE = r"visible"
t_OR = r"\|\|"
t_AND = r"&&"
t_EQUAL = r"="
t_UNEQUAL = r"!="
t_LESS = r"<"
t_LESS_EQUAL = r"<="
t_GREATER = r">"
t_GREATER_EQUAL = r">="
t_NOT = r"!"
t_OPEN_PAREN = r"\("
t_CLOSE_PAREN = r"\)"
t_COLON_EQUAL = r":="
t_PLUS_EQUAL = r"\+="

t_ignore_COMMENT_LEX = r'\#.*'
t_ignore_WHITESPACES_LEX = r'[ \t]'
t_ignore_ESCAPED_NEW_LINE_LEX = r'\\\n'

t_STRING_LEX= r'\"([^\\\n]|(\\.))*?\"'


if __name__ == '__main__':
    data = '''
    mainmenu "Simple example to demo kconfig select broken dependency issue"
    config A
      bool "CONFIG A"

    config B
      bool "CONFIG B"
      depends on !A

    config C
      bool "CONFIG C"
      depends on A
      select B

    '''
    import ply.lex as lex

    lexer = lex.lex()
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
