import SwedishWordle

game = SwedishWordle.Game(5) # skapa ett nytt wordlespel med ord som är 5 långa

guess1 = game.Guess('mössa')
print(f'Den första gissningen var mössa. Det resulterade i {guess1}. En siffra för bokstav i gissningen. 2 är rättbokstav på rätt plats, 1 bokstaven finns i rodet, bokstaven finns ej i ordet. ')


guess2 = game.Guess('skylt')
print(f'Den andra gissningen var skylt. Det resulterade i {guess2}.')

# det går att starta ett nytt game med längre ord
game2 = SwedishWordle.Game(10)
guess3 = game2.Guess('överträffa')
print(f'Den första gissningen i andra gamet var överträffa. Det resulterade i {guess3}.')

# det går att hämta och alla ord som är 10 tecken långa
print(f'Det finns {len(game2.words_in_game)} ord som är 10 bokstäver. Några av dom är {game2.words_in_game[0:14]}')

# det är viktigt att man gissar ett riktigt ord som finns i listan och är rätt längd annars ger spelet ett exception
game.Guess('läderlappen')
