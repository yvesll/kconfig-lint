import ply.lex as lex

# List of token names.
tokens = [
    'EOL', 'BOOL', 'CHOICE', 'COMMENT', 'CONFIG', 'DEF_BOOL', 'DEF_TRISTATE', 'DEFAULT', 'DEPENDS', 'ENDCHOICE',
    'ENDIF', 'ENDMENU', 'HELP', 'HEX', 'IF', 'IMPLY', 'INT', 'MAINMENU', 'MENU', 'MENUCONFIG', 'MODULES', 'ON',
    'OPTIONAL', 'PROMPT', 'RANGE', 'SELECT', 'SOURCE', 'STRING', 'TRISTATE', 'VISIBLE', 'OR', 'AND', 'EQUAL',
    'UNEQUAL', 'LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL', 'NOT', 'OPEN_PAREN', 'CLOSE_PAREN', 'COLON_EQUAL',
    'PLUS_EQUAL', 'WORD', 'WORD_QUOTE', 'ASSIGN_VAL', 'STRING_LITERAL', 'COMMENT_LITERAL', 'HELP_TEXT'
]

# Keyword rules
def t_BOOL(t):
    r'bool'
    return t

def t_CHOICE(t):
    r'choice'
    return t

def t_COMMENT(t):
    r'comment'
    return t

def t_CONFIG(t):
    r'config'
    return t

def t_DEF_BOOL(t):
    r'def_bool'
    return t

def t_DEF_TRISTATE(t):
    r'def_tristate'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DEPENDS(t):
    r'depends'
    return t

def t_ENDCHOICE(t):
    r'endchoice'
    return t

def t_ENDIF(t):
    r'endif'
    return t

def t_ENDMENU(t):
    r'endmenu'
    return t

def t_HELP(t):
    r'help'
    return t

def t_HEX(t):
    r'hex'
    return t

def t_IF(t):
    r'if'
    return t

def t_IMPLY(t):
    r'imply'
    return t

def t_INT(t):
    r'int'
    return t

def t_MAINMENU(t):
    r'mainmenu'
    return t

def t_MENU(t):
    r'menu'
    return t

def t_MENUCONFIG(t):
    r'menuconfig'
    return t

def t_MODULES(t):
    r'modules'
    return t

def t_ON(t):
    r'on'
    return t

def t_OPTIONAL(t):
    r'optional'
    return t

def t_PROMPT(t):
    r'prompt'
    return t

def t_RANGE(t):
    r'range'
    return t

def t_SELECT(t):
    r'select'
    return t

def t_SOURCE(t):
    r'source'
    return t

def t_STRING(t):
    r'string'
    return t

def t_TRISTATE(t):
    r'tristate'
    return t

def t_VISIBLE(t):
    r'visible'
    return t

# Operators and punctuation
t_OR = r'\|\|'
t_AND = r'&&'
t_EQUAL = r'='
t_UNEQUAL = r'!='
t_LESS = r'<'
t_LESS_EQUAL = r'<='
t_GREATER = r'>'
t_GREATER_EQUAL = r'>='
t_NOT = r'!'
t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_COLON_EQUAL = r':='
t_PLUS_EQUAL = r'\+='

# Define a rule for newline
def t_EOL(t):
    r'\n'
    t.lexer.lineno += 1
    return t

# Define string literals
def t_STRING_LITERAL(t):
    r'\"[^\"]*\"|\'[^\']*\''
    t.value = t.value[1:-1]
    return t

# Define words (identifiers)
def t_WORD(t):
    r'[a-zA-Z_][a-zA-Z0-9_.]*'
    return t

# Define a rule for comments
def t_COMMENT_LITERAL(t):
    r'\#.*'
    pass

# Define assignment values
def t_ASSIGN_VAL(t):
    r'[^ \t\n]+.*'
    t.value = t.value.strip()
    return t



# Ignore whitespace
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# String and help state rules
states = (
    ('string', 'exclusive'),
    ('HELP', 'exclusive'),
)

# Ignore spaces and tabs in string state
t_string_ignore = ' \t'

# Ignore spaces and tabs in help state
t_HELP_ignore = ' \t'

def t_INITIAL_string(t):
    r'\"|\''
    t.lexer.push_state('string')
    t.lexer.string_start = t.lexer.lexpos
    t.lexer.string_quote = t.value
    t.lexer.string_value = ""
    return

def t_string_end(t):
    r'\"|\''
    if t.value == t.lexer.string_quote:
        t.lexer.pop_state()
        t.value = t.lexer.string_value
        return t

def t_string_content(t):
    r'[^\"\'\\]+'
    t.lexer.string_value += t.value

def t_string_escape(t):
    r'\\.'
    t.lexer.string_value += t.value[1]

def t_string_error(t):
    print(f"Illegal character in string '{t.value[0]}'")
    t.lexer.skip(1)

# Help state rules
def t_INITIAL_HELP(t):
    r'\s+'
    t.lexer.push_state('help')
    t.lexer.help_indent = len(t.value)
    t.lexer.help_text = ""
    return

def t_HELP_end(t):
    r'\n[^\s]'
    t.lexer.pop_state()
    t.lexer.lexpos -= len(t.value)
    t.type = 'HELP_TEXT'
    t.value = t.lexer.help_text
    return t

def t_HELP_content(t):
    r'.+'
    t.lexer.help_text += t.value

def t_HELP_error(t):
    print(f"Illegal character in help text '{t.value[0]}'")
    t.lexer.skip(1)

if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as f:
        data = f.read()

    lexer = lex.lex()
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
