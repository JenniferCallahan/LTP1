def is_valid_word(wordlist, word):
    return word in wordlist


def make_str_from_row(board, row_index):
    row_str = ''
    for item in board[row_index]:
        row_str = row_str + item
    return row_str


def make_str_from_column(board, column_index):
    col_str = ''
    for item in board:
        col_str = col_str + item[column_index]
    return col_str
    

def board_contains_word_in_row(board, word):
    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True
    return False


def board_contains_word_in_column(board, word):
    for col_index in range(len(board[0])):
        if word in make_str_from_column(board, col_index):
            return True
    return False
  
	
def board_contains_word(board, word):
    if board_contains_word_in_row(board, word):
        return True
    elif board_contains_word_in_column(board, word):
        return True
    else:
        return False


def word_score(word):
    length = len(word)
    if length < 3: 
       score = 0
    if 2 < length < 7:
        score = length
    if 6 < length < 10:
      score = length * 2
    if length >= 10:
      score = length * 3 
    return score


def update_score(player_info, word):
    player_info[1] = player_info[1] + word_score(word)


def num_words_on_board(board, words):
    word_count = 0
    for item in words:
        if board_contains_word(board, item):
            word_count = word_count + 1
    return word_count


def read_words(words_file):
    list = []
    for item in words_file:
        list.append(item.rstrip('\n'))
    return list


def read_board(board_file):
    list1 = []
    for item in board_file:
        item = item.rstrip('\n')
        list2 = []
        for char in item:
            list2.append(char)
        list1.append(list2)
    return list1




#boardX =[['D','A','B','S','A','X','E','D'], ['R','U','M','B','L','E','S','R'], ['U','T','A','H','B','R','K','O'], ['D','U','U','N','S','O','S','O'], ['G','M','L','A','B','S','U','P',], ['E','N','S','U','R','E','R','E'], ['R','S','U','D','D','E','N','O'], ['Y','M','A','C','E','D','E','N']]

#wordlistX = ['DABS','SAX','AXED','RUMBLE','RUMBLES','UTAH','LABS','SUP','ENSURE','ENSURER','SUDDEN','MACE','ACE','MACED','DRUDGERY','DRUDGE','AUTUMN','AUTUMNS','MAUL','MAULS','ALB', 'ALBS','SEE', 'SEED', 'DROOP','PEON']


