import random


class SomeException(Exception):
    pass


def play_counts() -> int:
    """
    じゃんけんの回数を決める。
    """
    while True:
        try:
            counts = int(input('じゃんけんする回数を入力してください。(整数 : 1～10) > '))
            if 1 <= counts <= 10:
                break
            else:
                raise SomeException('1～10の整数を入力してください。')
        except ValueError:
            print('1～10の整数を入力してください。')
        except SomeException as e:
            print(e)

    return counts


def final_result(win_count:dict, counts:int) -> list:
    """
    勝敗の最終結果を作成。引分けはノーカン。
    """
    win, lose, draw = win_count['you'], win_count['cpu'], win_count['draw']
    win_rate = 0 if draw == counts else win / (counts - draw)

    return [win, lose, draw, win_rate]


def start_playing(counts:int) -> dict:
    """
    指定回数分、じゃんけんをする。
    """
    ### inner function
    def hand_choice() -> tuple:
        """
        自分が出す手を入力し、CPUの出す手を自動選択する。
        {0: 'グー', 1: 'チョキ', 2: 'パー'}
        """
        while True:
            try:
                your_choice = int(input('自分が出す手を入力してください(整数 : 0, 1, 2) > '))
                if 0 <= your_choice <= 2:
                    break
                else:
                    raise SomeException('0～2の整数を入力してください。')
            except ValueError:
                print('0～2の整数を入力してください。')
            except SomeException as e:
                print(e)

        cpu_choice = random.randint(0, 2)
        return your_choice, cpu_choice

    def win_judgment(you:int, cpu:int) -> int:
        """
        勝敗を判定。
        {0: '負け', 1: '勝ち', 2: '引分け'}
        
        結果をカウントアップ。
        win_count = {'you': 0, 'cpu': 0, 'draw': 0}
        """
        if you == cpu:
            key = 2
            win_count['draw'] += 1
        elif you == 0 and cpu == 1 or you == 1 and cpu == 2 or you == 2 and cpu == 0:
            key = 1
            win_count['you'] += 1
        else:
            key = 0
            win_count['cpu'] += 1
        return key


    ### init dict
    hands = {0: 'グー', 1: 'チョキ', 2: 'パー'}
    judgment = {0: '負け', 1: '勝ち', 2: '引分け'}
    win_count = {'you': 0, 'cpu': 0, 'draw': 0}
    ### Play Start
    print('\n' + '*'*45 + f'\n選択肢 : {hands}\n' + '*'*45 + '\n')
    for count in range(1, counts + 1):
        print('\n' + '-'*4 + f'{count}回目' + '-'*4)
        your_choice, cpu_choice = hand_choice()
        print(f'コンピューターの出した手 : {hands[cpu_choice]}')
        print(f'自分の出した手 : {hands[your_choice]}')
        r_key = win_judgment(your_choice, cpu_choice)
        print(f'結果 : {judgment[r_key]}')

    return win_count


if __name__ == '__main__':
    counts = play_counts()
    win_count = start_playing(counts)
    r = final_result(win_count, counts)
    print('\n' + f'最終結果 : {r[0]}勝 {r[1]}敗 {r[2]}分け, 勝率 {r[3]:.3f}' + '\n')
