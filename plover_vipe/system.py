
KEYS = (
    '#',
    'S-', 'T-', 'K-', 'P-', 'V-', 'H-', 'R-',
    'A-', 'O-',
    '*',
    '-E', '-U',
    '-F', '-R', '-P', '-B', '-L', '-G', '-T', '-S', '-D', '-N',
)

IMPLICIT_HYPHEN_KEYS = ('A-', 'O-', '-E', '-U', '*')

SUFFIX_KEYS = ('-R', '-G', '-S', '-D', '-N')

NUMBER_KEY = '#'

NUMBERS = {
    'S-': '1-',
    'T-': '2-',
    'P-': '3-',
    'H-': '4-',
    'A-': '5-',
    'O-': '0-',
    '-F': '-6',
    '-P': '-7',
    '-L': '-8',
    '-T': '-9',
}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = [
        # == +ene ==
    # e + ene = ene
    (r"^(.+)e \^ ene$", r"\1ene"),
    
        # == +er ==
	# re + er = rer
	(r"^(.+)re \^ er$", r"\1rer"),
	# se + er = ser
	(r"^(.+)se \^ er$", r"\1ser"),
    # ke + er = ker
	(r"^(.+)ke \^ er$", r"\1ker"),
    
        # == +es ==
    # e + es = es
	(r"^(.+)e \^ es$", r"\1es"),
    
        # == +en ==
	# e + en = en
	(r"^(.+)e \^ en$", r"\1en"),
	# m + en = mmen
	(r"^(.+)m \^ en$", r"\1mmen"),
    
        # == +et ==
	# m + et = mmet
	(r"^(.+)m \^ et$", r"\1mmet"),
]	

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Gemini PR': {
        '#'         : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
        'S-'        : ('S1-', 'S2-'),
        'T-'        : 'T-',
        'K-'        : 'K-',
        'P-'        : 'P-',
        'V-'        : 'W-',
        'H-'        : 'H-',
        'R-'        : 'R-',
        'A-'        : 'A-',
        'O-'        : 'O-',
        '*'         : ('*1', '*2', '*3', '*4'),
        '-E'        : '-E',
        '-U'        : '-U',
        '-F'        : '-F',
        '-R'        : '-R',
        '-P'        : '-P',
        '-B'        : '-B',
        '-L'        : '-L',
        '-G'        : '-G',
        '-T'        : '-T',
        '-S'        : '-S',
        '-D'        : '-D',
        '-N'        : '-Z',
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'S-'        : ('a', 'q'),
        'T-'        : 'w',
        'K-'        : 's',
        'P-'        : 'e',
        'V-'        : 'd',
        'H-'        : 'r',
        'R-'        : 'f',
        'A-'        : 'c',
        'O-'        : 'v',
        '*'         : ('t', 'g', 'y', 'h'),
        '-E'        : 'n',
        '-U'        : 'm',
        '-F'        : 'u',
        '-R'        : 'j',
        '-P'        : 'i',
        '-B'        : 'k',
        '-L'        : 'o',
        '-G'        : 'l',
        '-T'        : 'p',
        '-S'        : ';',
        '-D'        : '[',
        '-N'        : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
    'Passport': {
        '#'    : '#',
        'S-'   : ('S', 'C'),
        'T-'   : 'T',
        'K-'   : 'K',
        'P-'   : 'P',
        'V-'   : 'W',
        'H-'   : 'H',
        'R-'   : 'R',
        'A-'   : 'A',
        'O-'   : 'O',
        '*'    : ('~', '*'),
        '-E'   : 'E',
        '-U'   : 'U',
        '-F'   : 'F',
        '-R'   : 'Q',
        '-P'   : 'N',
        '-B'   : 'B',
        '-L'   : 'L',
        '-G'   : 'G',
        '-T'   : 'Y',
        '-S'   : 'X',
        '-D'   : 'D',
        '-N'   : 'Z',
        'no-op': ('!', '^', '+'),
    },
    'Stentura': {
        '#'    : '#',
        'S-'   : 'S-',
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'V-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-U'   : '-U',
        '-F'   : '-F',
        '-R'   : '-R',
        '-P'   : '-P',
        '-B'   : '-B',
        '-L'   : '-L',
        '-G'   : '-G',
        '-T'   : '-T',
        '-S'   : '-S',
        '-D'   : '-D',
        '-N'   : '-Z',
        'no-op': '^',
    },
    'TX Bolt': {
        '#'    : '#',
        'S-'   : 'S-',
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'V-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-U'   : '-U',
        '-F'   : '-F',
        '-R'   : '-R',
        '-P'   : '-P',
        '-B'   : '-B',
        '-L'   : '-L',
        '-G'   : '-G',
        '-T'   : '-T',
        '-S'   : '-S',
        '-D'   : '-D',
        '-N'   : '-Z',
    },
    'Treal': {
        '#'    : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B'),
        'S-'   : ('S1-', 'S2-'),
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'V-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : ('*1', '*2'),
        '-E'   : '-E',
        '-U'   : '-U',
        '-F'   : '-F',
        '-R'   : '-R',
        '-P'   : '-P',
        '-B'   : '-B',
        '-L'   : '-L',
        '-G'   : '-G',
        '-T'   : '-T',
        '-S'   : '-S',
        '-D'   : '-D',
        '-N'   : '-Z',
        'no-op': ('X1-', 'X2-', 'X3'),
    },
}

DICTIONARIES_ROOT: str = 'asset:plover_vipe:dictionaries'
DEFAULT_DICTIONARIES = ('vipe_main.json', 'vipe_commands.json')
