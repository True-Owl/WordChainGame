import random

class WordChainGame:
    def __init__(self, filename):
        self.words = self.load_words(filename)
        
    def load_words(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            words = file.read().splitlines()
        return words

    def calculate_score(self, word):
        return len(word) * 2

    def play_word_chain(self, num_games):
        player_total_score = 0
        computer_total_score = 0

        for game in range(num_games):
            print(f"\n=== 게임 {game+1} ===")
            used_words = []
            current_word = random.choice(self.words)
            used_words.append(current_word)
            print("\033[35m 시작 단어:", current_word, '\033[0m')

            player_score = 0
            computer_score = 0

            while True:
                player_word = input("\033[33m 단어를 입력하세요: \033[0m")

                if len(player_word) < 2:
                    print("\033[31m [!] 2글자 이상만 입력할 수 있습니다. \033[0m")
                    break

                if player_word in used_words:
                    print("\033[31m 이미 사용한 단어입니다. \033[0m")
                    break

                if player_word[0] != current_word[-1]:
                    print("\033[31m 첫글자가 다릅니다! 033[0m")
                    break

                if player_word not in self.words:
                    print("\033[31m 사전에 존재하지 않는 단어입니다. \033[0m")
                    break

                used_words.append(player_word)
                player_score += self.calculate_score(player_word)

                last_char = player_word[-1]
                available_words = [word for word in self.words if word[0] == last_char and len(word) >= 2 and word not in used_words]

                if not available_words:
                    print("\033[31m 더 이상 사용 가능한 단어가 없습니다. \033[0m")
                    break

                if random.random() < 0.1:
                    print("\033[36m 컴퓨터: 생각나는 단어를 선택하지 못했습니다. \033[0m")
                    break


                computer_word = random.choice(available_words)
                used_words.append(computer_word)
                computer_score += self.calculate_score(computer_word)
                print("\033[36m 컴퓨터:", computer_word, '\033[0m')

                current_word = computer_word


            if player_score > computer_score:
                player_score -= round(player_score / 5)
            elif player_score < computer_score:
                computer_score -= round(computer_score / 5)

            print("\033[33m 게임 종료! 플레이어 점수:", player_score, "컴퓨터 점수:", computer_score, '\033[0m')
            player_total_score += player_score
            computer_total_score += computer_score

        print("\n\n\n\033[33m === 모든 게임 종료! ===")
        print("플레이어 총 점수:", player_total_score)
        print("컴퓨터 총 점수:", computer_total_score, "\033[0m \n\n")

        if player_total_score > computer_total_score:
            print("\033[92m플레이어가 이겼습니다!\033[0m")
        elif player_total_score < computer_total_score:
            print("\033[91m컴퓨터가 이겼습니다!\033[0m")
        else:
            print("\033[93m무승부입니다!\033[0m")

word_chain_game = WordChainGame('words.txt')
try:
    num_games = int(input("몇 판 플레이하시겠습니까? "))
    word_chain_game.play_word_chain(num_games)

except ValueError:
    print("\033[31m [!] 숫자만 입력해주세요. \033[0m")
