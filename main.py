from random import choice
gallows = [['-', '-', '-', '-', '-', '-'],
           [' ', '|', ' ', ' ', '|', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           ['/', ' ', '\\', ' ', ' ', ' '], ]

def draw_gallows(error_num=0):
    def draw():
        str_gallows = ''
        for lst in gallows:
            str_gallows += ''.join(lst) + '\n'
        return str_gallows

    match error_num:
        case 1:
            gallows[2][4] = 'O'
        case 2:
            gallows[3][3] = '/'
        case 3:
            gallows[3][4] = '|'
        case 4:
            gallows[3][5] = '\\'
        case 5:
            gallows[4][3] = '/'
        case 6:
            gallows[4][5] = '\\'

    return draw()

def find_all(text: str, substring):
    result = []
    start_position = 0
    for i in range(len(text)):
        position = text.find(substring, start_position)
        if position > -1:
            result.append(position)
            start_position = position + 1
    return result

def main():
    print(draw_gallows())
    word = choice (['pizza' , 'borszcz' , 'banana', 'kielbasa'])
    answer_word = ['_' for _ in range(len(word))]
    error_count = 0
    lose = False
    print(' '.join(answer_word))
    while ''.join(answer_word) != word:
        user_input = input('Type your letter >>> ')
        if user_input in word:
            letter_indexes = find_all(word, user_input)
            for i in letter_indexes:
                answer_word[i] = user_input
            print(draw_gallows())
            print(' '.join(answer_word))
        else:
            error_count += 1
            print(draw_gallows(error_count))
            print(' '.join(answer_word))
        if error_count >= 6:
            lose = True
    if lose:
        print('Game over \n Your lose')
    else:
        print('You win!!!')


if __name__ == "__main__":
    main()
