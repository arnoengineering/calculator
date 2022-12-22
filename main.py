class button:
    def __init__(self):
        pass


class small_buton(button):
    def __init__(self, fr, sec=None, tr=None):
        self.pr = fr
        self.sec = sec
        self.tr = tr
        super().__init__()
        pass


class large_button(button):
    def __init__(self):
        super().__init__()
        pass


class exicution_button(button):
    def __init__(self):
        super().__init__()
        pass


# main numpad 4x3: 0,.,10^n,range bot to top
# same first row to right 1x2 (del ac)
# second row 3x2: [x,div,+,-,ans,eq]


# for range 1:9 run n sec
num = ['stat/dist', 'cmplx', 'base',
       'matrix', 'vector', 'verify',
       'const', 'conv', 'clr']

# full bot ans =
num_bot = ['rnd', ['ran#', 'ranint'], ['pi', 'e'], ['drg', 'PreAns']]
# todo add explain for each: on hover
# also add right click second
side_num = {'del': 'ins', 'ac': 'off',
            'X': ['npr', 'gcd'], 'div': ['ncr', 'lcm'],
            '+': ['pol', 'int'], '-': ['rec', 'intg']}

# top left4x2
top_left = {'calc': ['solve', '=='],'_inte_': ['_dydx_', ':'],
            '_fraction_': ['_mixed fraction_', 'div_R'], '_sqrt_': ['_cuberoot_', '_repeating_'],
            '_(-)_': ['angel__purple', 'A_green'], 'min_sec': ['FACT', 'B_green'],
            'RCL':'STO', 'ENG': ['<--', 'i_purp']}
