import random


class SomeException(Exception):
    pass


class JankenPon():

    def __init__(self) -> None:
        self.counts = self.play_counts()
        self.hands = {0: 'グー', 1: 'チョキ', 2: 'パー'}
        self.jidge_sts = {0: '負け', 1: '勝ち', 2: '引分け'}
        self.win_count = {'you': 0, 'cpu': 0, 'draw': 0}
        print('\n' + '*'*45 + f'\n選択肢 : {self.hands}\n' + '*'*45 + '\n')

    def play_counts(self) -> int:
        """
        じゃんけんの回数を入力。
        """
        while True:
            try:
                counts = int(input('ジャンケンポンする回数を入力してください。(整数 : 1～10) > '))
                if 1 <= counts <= 10:
                    break
                else:
                    raise SomeException('1～10の整数を入力してください。')
            except ValueError:
                print('1～10の整数を入力してください。')
            except SomeException as e:
                print(e)
        return counts

    def final_result(self):
        """
        勝敗の最終結果を作成。引分けはノーカン。
        """
        win, lose, draw = self.win_count['you'], self.win_count['cpu'], self.win_count['draw']
        win_rate = 0 if draw == self.counts else win / (self.counts - draw)

        r = [win, lose, draw, win_rate]
        print('\n' + f'最終結果 : {r[0]}勝 {r[1]}敗 {r[2]}分け, 勝率 {r[3]:.3f}' + '\n')

    def start_playing(self):
        """
        指定回数分、じゃんけんをする。
        """
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
                jidge_key = 2
                self.win_count['draw'] += 1
            elif you == 0 and cpu == 1 or you == 1 and cpu == 2 or you == 2 and cpu == 0:
                jidge_key = 1
                self.win_count['you'] += 1
            else:
                jidge_key = 0
                self.win_count['cpu'] += 1
            return jidge_key

        for count in range(1, self.counts + 1):
            print('\n' + '-'*4 + f'{count}回目' + '-'*4)
            your_choice, cpu_choice = hand_choice()
            print(f'コンピューターの出した手 : {self.hands[cpu_choice]}')
            print(f'自分の出した手 : {self.hands[your_choice]}')
            jidge_key = win_judgment(your_choice, cpu_choice)
            print(f'結果 : {self.jidge_sts[jidge_key]}')


def main():
    janken = JankenPon()
    janken.start_playing()
    janken.final_result()

if __name__ == '__main__':
    main()
