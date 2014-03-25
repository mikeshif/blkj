 import tkinter
from tkinter import Tk, Canvas, Frame, Button
import sys
#from 'C:\\PIL-1.1.7a2-py2.5-macosx10.5.mpkg' import ImageFile as PILImageFile
#import Image # precompiled from C:\py21\PIL\Image.pyc
from random import shuffle
#from urllib import urlopen
#opener = urllib.FancyURLopener(proxies)
from urllib.request import urlopen
import io

images = []
photos = []
card = []

class Deck(object):
    
    def __init__(self):
        self.suits = ['C', 'S', 'H', 'D']
        self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        self.deck = [(rank, suit) for rank in self.ranks for suit in self.suits] 
        self.shuffle()
        self.card_size = (73,98)
        self.played_cards = []
        self.card_face = ['http://imageshack.us/a/img9/6783/n8k4.jpg', 'http://imageshack.us/a/img577/9144/lkpr.jpg', 'http://imageshack.us/a/img16/7974/kz19.jpg', 'http://imageshack.us/a/img341/1584/kow9.jpg',\
                          'http://imageshack.us/a/img96/3832/9sij.jpg', 'http://imageshack.us/a/img593/5210/ax4f.jpg', 'http://imageshack.us/a/img18/5531/wv1t.jpg', 'http://imageshack.us/a/img534/4296/zpdb.jpg',\
                          'http://imageshack.us/a/img189/846/s6m5.jpg', 'http://imageshack.us/a/img819/5116/h39j.jpg', 'http://imageshack.us/a/img59/161/jnxb.jpg', 'http://imageshack.us/a/img35/3619/ykxe.jpg',\
                          'http://imageshack.us/a/img51/4187/ubrw.jpg', 'http://imageshack.us/a/img35/4148/8etg.jpg', 'http://imageshack.us/a/img856/8139/k233.jpg', 'http://imageshack.us/a/img713/5533/k6ld.jpg',\
                          'http://imageshack.us/a/img854/1117/vvj.jpg', 'http://imageshack.us/a/img5/9364/38va.jpg', 'http://imageshack.us/a/img401/4606/m635.jpg', 'http://imageshack.us/a/img600/1197/zdm9.jpg',\
                          'http://imageshack.us/a/img27/9006/83a6.jpg', 'http://imageshack.us/a/img5/6156/mslt.jpg', 'http://imageshack.us/a/img9/7453/j6i1.jpg', 'http://imageshack.us/a/img221/2149/7w3p.jpg',\
                          'http://imageshack.us/a/img266/2544/0eku.jpg', 'http://imageshack.us/a/img407/6823/r3r.jpg', 'http://imageshack.us/a/img834/6500/kllb.jpg', 'http://imageshack.us/a/img842/8531/u14b.jpg',\
                          'http://imageshack.us/a/img580/1034/x0od.jpg', 'http://imageshack.us/a/img191/7715/a8x0.jpg', 'http://imageshack.us/a/img801/1125/fq3r.jpg', 'http://imageshack.us/a/img845/5820/eaep.jpg',\
                          'http://imageshack.us/a/img13/6573/6ro1.jpg', 'http://imageshack.us/a/img834/4240/yvfm.jpg', 'http://imageshack.us/a/img841/6792/hcy5.jpg', 'http://imageshack.us/a/img42/9787/oz7a.jpg',\
                          'http://imageshack.us/a/img163/3135/gm7x.jpg', 'http://imageshack.us/a/img833/6261/z9yv.jpg', 'http://imageshack.us/a/img585/7933/8ark.jpg', 'http://imageshack.us/a/img832/8133/8mre.jpg',\
                          'http://imageshack.us/a/img838/6276/3h69.jpg', 'http://imageshack.us/a/img22/7359/w5cu.jpg', 'http://imageshack.us/a/img542/4223/6yqn.jpg', 'http://imageshack.us/a/img23/1951/suh1.jpg',\
                          'http://imageshack.us/a/img7/8003/xpiq.jpg', 'http://imageshack.us/a/img577/7663/olgf.jpg', 'http://imageshack.us/a/img703/5393/0kie.jpg', 'http://imageshack.us/a/img837/8590/dr3d.jpg',\
                          'http://imageshack.us/a/img600/5778/pn39.jpg', 'http://imageshack.us/a/img109/5589/5ndc.jpg', 'http://imageshack.us/a/img826/6804/pl79.jpg', 'http://imageshack.us/a/img402/482/6ne8.jpg',\
                          'http://imageshack.us/a/img40/413/aei7.jpg']

        self.card_face_index = ['CA','C2','C3','C4','C5','C6','C7','C8','C9','CT','CJ','CQ','CK',\
                                'SA','S2','S3','S4','S5','S6','S7','S8','S9','ST','SJ','SQ','SK',\
                                'HA','H2','H3','H4','H5','H6','H7','H8','H9','HT','HJ','HQ','HK',\
                                'DA','D2','D3','D4','D5','D6','D7','D8','D9','DT','DJ','DQ','DK']

    def shuffle(self):
        shuffle(self.deck)

    def get_card(self):
        card = self.deck[0]
        self.played_cards.append(card)
        del self.deck[0]
        return card
    
    def add_card_back(self, *cards):
        for card in cards:
            if card not in self.deck:
                self.deck.append(card)
                if card in self.played_cards:
                    a=self.played_cards.index(card)
                    del self.played_cards[a]
                    
    def card_face_to_show(self, card):
        card_to_show = card[1]+card[0]
        card = self.card_face_index.index(card_to_show)
        return card

class BlackJack(Deck):
    
    def __init__(self):
        super(BlackJack, self).__init__()
        self.score = 1
        self.player_hand_value = 0
        self.dealer_hand_value = 0
        self.player_hand = []
        self.dealer_hand = []
        self.player_bust = False
        self.dealer_bust = False
        self.dealer_turn = False
        self.result =''
        self.resultd ='Dealer has ' + str(self.dealer_hand_value) + ' showing'
        self.resultp = str(self.player_hand_value) + self.result
        self.card_face_position = []
        self.win = False
        self.double = False
        self.values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
        self.card_positions_player = [[350, 550], [450, 550],\
                               [312.5, 575], [400, 575], [487.5, 575],\
                               [275, 600],[458.33, 600], [441.66, 600], [525, 600],\
                               [311.5, 625], [478.16, 625]]
                             
        self.card_positions_dealer = [[350, 100], [450, 100],\
                               [312.5, 125], [400, 125], [487.5, 125],\
                               [275, 150],[358.33, 150], [441.66, 150], [525, 150],\
                               [311.5, 175], [478.16, 175]]
        
    def deck_size(self):
        if len(self.deck) == 0:
            temp = []
            
            if len(self.player_hand) > 0:
                for cards in range(len(self.player_hand)):
                    temp.append(self.player_hand[cards])
            
            if len(self.dealer_hand) > 0:
                for cards in range(len(self.dealer_hand)):
                    temp.append(self.dealer_hand[cards])
            
            if len(temp) > 0:
                for cards in temp:
                    index_of_card=self.played_cards.index(cards)
                    del self.played_cards[index_of_card]
            
            vv=self.played_cards[:]
            self.add_card_back(*vv)
            
            if len(temp) > 0:
                for cards in temp:
                    self.played_cards.append(cards)
            
            self.shuffle()
        
    def deal_hand(self):
        if not self.win:
            self.score -= 1
            
        self.player_hand = []
        self.dealer_hand = []
        self.player_bust = False
        self.dealer_bust = False
        self.dealer_turn = False
        self.win = False
        self.delay_count = 0
        
        for a in range(4):
            self.deck_size()
            card = self.get_card()
            
            if not a % 2:
                self.player_hand.append(card)
            else:
                self.dealer_hand.append(card)
        
        self.player_hand_value = self.total_hand(self.player_hand)
        self.dealer_hand_value = self.total_hand(self.dealer_hand)
        
    def hit(self):
        if not self.win:
            
            if not self.player_bust:
                
                if not self.dealer_turn and len(self.player_hand) < 11:
                    self.deck_size()                
                    card = self.get_card()
                    self.player_hand.append(card)
                
            if not self.dealer_bust:
                
                if self.dealer_turn and len(self.dealer_hand) < 11:
                    self.deck_size()                
                    card = self.get_card()
                    self.dealer_hand.append(card)

            self.dealer_hand_value = self.total_hand(self.dealer_hand)
            self.player_hand_value = self.total_hand(self.player_hand)
            self.bust()
            
    def bust(self):
        if self.player_hand_value > 21 and not self.player_bust:
                self.score -= 1
                self.result = str(self.player_hand_value)+' showing, ' + 'Busted,  New Deal?'
                self.player_bust = True
                self.win = True
                if self.double:
                    self.score -= 1
            
        if self.dealer_hand_value > 21 and not self.dealer_bust:
                self.score += 1
                self.result = 'Dealer busts, Player wins,  New Deal?'
                self.dealer_bust = True
                self.win = True
                if self.double:
                    self.score += 1 

    def stand(self):
        if not self.win:
            self.dealer_turn = True
           
    def dealer(self):
        if not self.win:
            
            if self.dealer_hand_value < 17:
                self.hit()
                
            elif self.player_hand_value == self.dealer_hand_value:
                self.result = str(self.player_hand_value)+' showing, Tie ' + 'Player Wins,  New Deal?'
                self.score += 1
                self.win = True
                if self.double:
                    self.score += 1
                
            elif self.player_hand_value < self.dealer_hand_value:
                self.result = str(self.player_hand_value)+' showing, ' + 'Dealer Wins,  New Deal?'
                self.score -= 1
                self.win = True
                if self.double:
                    self.score -= 1
               
            elif self.player_hand_value > self.dealer_hand_value > 16:
                self.result = str(self.player_hand_value)+' showing, ' + 'Player Wins,  New Deal?'
                self.score +=1
                self.win = True
                if self.double:
                    self.score += 1

    def total_hand(self, hand):
        value = 0
        for a in hand:
            value += self.values[a[0]]
            
        for a in hand:
            if a[0] == 'A' and value -1  < 11:
                value +=10
        
        return value
                
    def show_results(self):
        if not self.player_bust and not self.win:
             self.result = str(self.player_hand_value)+' showing, Hit or Stand?'
       
        if self.dealer_turn:
            self.resultd ='Dealer has ' + str(self.dealer_hand_value) + ' showing'
            
        elif not self.dealer_turn and self.dealer_hand[0][0] == 'A': 
            self.resultd ='Dealer has an ' + str(self.dealer_hand[0][0]) + ' showing'
            
        else:
            self.resultd ='Dealer has ' + str(self.values[self.dealer_hand[0][0]]) + ' showing'
            
        return self.result, self.resultd
    
    def update(self, card, pd='player'):
        if pd == 'player':
            cl = self.card_face_to_show(self.player_hand[card])
            cpp = self.card_positions_player[card]
            
        elif pd !='player' and card == 1 and not self.dealer_turn:
            cpp = self.card_positions_dealer[card]
            return 0, 52, (71, 96), cpp, self.show_results()
        
        elif pd !='player' and self.dealer_turn:
            cl = self.card_face_to_show(self.dealer_hand[card])
            cpp = self.card_positions_dealer[card]
            return 1, cl, (73, 98), cpp, self.show_results()
        
        else:
            cl = self.card_face_to_show(self.dealer_hand[card])
            cpp = self.card_positions_dealer[card]
            return 1, cl, (73, 98), cpp, self.show_results()
        
        self.show_results()
        
        if self.dealer_turn and (not self.win):
            self.delay()
            
        return cl, cpp, self.show_results()

    def delay(self):
        self.delay_count +=1
        
        if self.delay_count == 120:
            self.delay_count = 0
            self.dealer()

def deal():
    for a in range(len(game.dealer_hand)):
        i, cl, cs, cpp, result = game.update(a,'dealer')
        table_area.coords(card[cl],0,1600)

    for a in range(len(game.player_hand)):
        cl, cpp, result = game.update(a,'player')
        table_area.coords(card[cl],0,1600)
    game.double = False
    game.deal_hand()
    
def hit():
    game.hit()
    
def stand():
    game.stand()
    
def double():
    game.double = True
    game.hit()
    game.stand()
    
def init():
    global game , card_face
    for a in range(len(card)):
        table_area.coords(card[a],0,1600)
   
    game = BlackJack()
    game.shuffle()
    game.deal_hand()
    
init()
                 
def draw():
    
    for a in range(len(game.dealer_hand)):
        i, cl, cs, cpp, result = game.update(a,'dealer')
        if i == 1:
        	table_area.coords(card[52], 0,800)
        	table_area.coords(card[cl], cpp[0],cpp[1])
        	table_area.tag_raise(card[cl])
        	table_area.itemconfig(dealer_messages, text = result[1], fill = 'white')

    for a in range(len(game.player_hand)):
        cl,cpp, result = game.update(a)
        table_area.coords(card[cl], cpp[0],cpp[1])
        table_area.tag_raise(card[cl])
        table_area.itemconfig(player_messages, text = result[0], fill = 'white')

    table_area.itemconfig(score, text = 'score ' + str(game.score), fill = 'white')

    table_area.after(16,draw)

root = Tk()
root.title("BlackJack")
root.geometry("1025x815+100+100")

control_area = Frame(root)
control_area.pack(side='top')
control_area.grid_columnconfigure(0, weight=0)
control_area.grid_columnconfigure(1, weight=0)

table_area = Canvas(control_area, width=800, height=800)
table_area.configure(bg='Dark Green')
table_area.grid(row=0, column=1, rowspan = 20)


#background = urlopen('http://imageshack.us/a/img521/620/1vwl.png').read()
#background = Image.open(io.BytesIO(background)).convert('RGBA')
#bgd = ImageTk.PhotoImage(background)
#bg = table_area.create_image(400,400, image=bgd)

deal = Button(control_area, text = 'Deal', command = deal, fg = 'black')
deal.grid(row=0, column=0)

hit = Button(control_area, text = 'Hit', command = hit, fg = 'black')
hit.grid(row=1, column=0)

stand = Button(control_area, text = 'Stand', command = stand, fg = 'black')
stand.grid(row=2, column=0)

double = Button(control_area, text = 'Double Down', command = double, fg = 'black')
double.grid(row=3, column=0)

reset = Button(control_area, text = 'Reset Game', command = init, fg = 'black')
reset.grid(row=7, column=0)

dealer_messages = table_area.create_text(400, 25, text = '', font = ("Helvetica", 30), fill = 'white')
player_messages = table_area.create_text(400, 770, text = '', font = ("Helvetica", 30), fill = 'white')
score = table_area.create_text(60, 300, text = '', font = ("Helvetica", 20), fill = 'white')

"""for a in range(len(game.card_face)):
    img = urlopen(game.card_face[a]).read() 
    images.append(Image.open(io.BytesIO(img)).convert('RGBA'))
    photos.append(ImageTk.PhotoImage(images[a]))
    card.append(table_area.create_image(0,1600, image=photos[a]))"""

draw()
root.mainloop()
