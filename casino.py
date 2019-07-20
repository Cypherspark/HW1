import random
# import matpoltlib as mtp

random.seed()

class game():
    rounds = 0
    def __init__(self, players):
         self.players = players
         game.rounds += 1


    def round_number(self):
        print("round number {game.rounds}".format(game=game))


    def play(self):
        self.oc = random.randrange(1,33)

        if self.oc % 2 == 0 :
            self.oc_type = 'even'
        else:
             self.oc_type = 'odd'

    def gather_stakes(self):
       
        for u in self.players:
            u.make_stake()
		    
    def share_slices(self):
        for u in self.players:
            u.amount += u.winamount()
	
	

class player():
    #includes amount of bet , rounds of playing...
    count = 0
    def __init__(self, name, initial_amount, bet):    
         self.name = name 
         self.amount = initial_amount
         self.bet = bet
         player.count += 1
         self.status = 'loser'

    def numbers(self):
        print("{player.count} players are in the game".format(player=player))

    def bookkeeper(self):
        bkeep = []
        bkeep.append(self.amount) 
        wns = []
        wns.append(self.winamount())


    def make_stake(self, stake=random.randrange(25,70)):
        self.stake = stake

    def winamount(self):
        if self.status == "winner":
            if type(self.bet) == int:
                win_chance = 1/32
            elif type(self.bet) == str:
                win_chance = 0.5
            elif type(self.bet) == range:
                win_chance =  len(list(self.bet))/32
            return int((1-win_chance)*self.stake) 
        else :
            return -(self.stake)

class Table(game):
    def __init__(self, players):
        super().__init__(players)
        game.rounds -= 1
        
        
    
    def bet_table(self):
        table = {}
        for player in self.players:
            table[player.name] = player.bet
        print('players bets list :', table) 
    
    def share_table(self):
        table1 = {}
        for player in self.players:
            table1[player.name] = player.winamount()
        print('win or loss of money :', table1)

    def amounts(self):
        table1 = {}
        for player in self.players:
            table1[player.name] = player.amount
        print('player cash :', table1)


class Bet(game):
    def new_bets(self):
        a = random.choice(['even','odd'])
        b = random.choice(list(range(1,33)))
        x = random.randrange(1,32)
        y = random.randrange(x+1,33)
        c = range(x,y)
        for u in self.players:
            u.bet = random.choice([a,b,c])



class outcome(Table):
    def __init__(self, players):
       super().play()
       super().__init__(players)
       self.players = players

    def __str__(self):
        return "outcome is {self.oc}".format(self=self)

    def match_result(self):
        for u in self.players:
            if self.oc == u.bet:
                u.status = 'winner'
            if self.oc_type == u.bet:
                u.status = 'winner'
            try:
                if self.oc in u.bet:
                     u.status = 'winner'
            except TypeError:
                pass
            
    def winers(self):
        wns = []
        for u in self.players:
           if u.status == 'winner':
               wns.append(u.name)
        return wns

    def losers(self):
        ls = []
        for u in self.players:
           if u.status == 'loser':
               ls.append(u.name)
        return ls




playerinstances = [
    player('num 1', 2000, 'odd'),
    player('num 2', 5000, range(5,10)),
    player('num3',500, 20)
]



for u in range(1):
    roullete = game(playerinstances)
    playerinstances[0].make_stake()
    playerinstances[1].make_stake()
    playerinstances[2].make_stake() 
    # roullete.gather_stakes()
    roullete = outcome(playerinstances)
    roullete.round_number()
    print(roullete)
    roullete.bet_table()
    roullete.match_result()
    print('winners are :',roullete.winers())
    print('losers are :',roullete.losers())
    roullete.share_table()
    roullete.share_slices()
    roullete.amounts()
    a = Bet(playerinstances)
    a.new_bets()


# a = outcome()
# a.round_number()
# print(a,'\n')
