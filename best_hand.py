def separate(d):
  left_hand = []
  right_hand = []
  for card, pos in d.items():
    card = card[:-4]
    if(pos[1] < 50):
      left_hand.append(card)
      right_hand.append(card)
    elif(pos[0] < 300):
      left_hand.append(card)
    else:
      right_hand.append(card)
  print("left_hand: ", left_hand)
  print("right_hand: ", right_hand)
  
  hands = [" ".join(left_hand), " ".join(right_hand)]
  return hands

from collections import namedtuple
 
class Card(namedtuple('Card', 'face, suit')):
    def __repr__(self):
        return ''.join(self)
 
 
suit = 'h d c s'.split()
# ordered strings of faces
faces   = '2 3 4 5 6 7 8 9 10 J Q K A'
lowaces = 'A 2 3 4 5 6 7 8 9 10 J Q K'
# faces as lists
face   = faces.split()
lowace = lowaces.split()
 
 
def straightflush(hand):
    f,fs = ( (lowace, lowaces) if any(card.face == '2' for card in hand)
             else (face, faces) )
    ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if ( all(card.suit == first.suit for card in rest) and
         ' '.join(card.face for card in ordered) in fs ):
        return '8 straight-flush', ordered[-1].face
    return False
 
def fourofakind(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) != 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 4:
            allftypes.remove(f)
            return '7 four-of-a-kind', [f, allftypes.pop()]
    else:
        return False
 
def fullhouse(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) != 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 3:
            allftypes.remove(f)
            return '6 full-house', [f, allftypes.pop()]
    else:
        return False
 
def flush(hand):
    allstypes = {s for f, s in hand}
    if len(allstypes) == 1:
        allfaces = [f for f,s in hand]
        return '5 flush', sorted(allfaces,
                               key=lambda f: face.index(f),
                               reverse=True)
    return False
 
def straight(hand):
    f,fs = ( (lowace, lowaces) if any(card.face == '2' for card in hand)
             else (face, faces) )
    ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if ' '.join(card.face for card in ordered) in fs:
        return '4 straight', ordered[-1].face
    return False
 
def threeofakind(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) <= 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 3:
            allftypes.remove(f)
            return ('3 three-of-a-kind', [f] +
                     sorted(allftypes,
                            key=lambda f: face.index(f),
                            reverse=True))
    else:
        return False
 
def twopair(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    if len(pairs) != 2:
        return False
    p0, p1 = pairs
    other = [(allftypes - set(pairs)).pop()]
    return '2 two-pair', pairs + other if face.index(p0) > face.index(p1) else pairs[::-1] + other
 
def onepair(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    if len(pairs) != 1:
        return False
    allftypes.remove(pairs[0])
    return '1 one-pair', pairs + sorted(allftypes,
                                      key=lambda f: face.index(f),
                                      reverse=True)
 
def highcard(hand):
    allfaces = [f for f,s in hand]
    return '0 high-card', sorted(allfaces,
                               key=lambda f: face.index(f),
                               reverse=True)
 
handrankorder =  (straightflush, fourofakind, fullhouse,
                  flush, straight, threeofakind,
                  twopair, onepair, highcard)
 
def rank(cards):
    hand = handy(cards)
    for ranker in handrankorder:
        rank = ranker(hand)
        if rank:
            break
    assert rank, "Invalid: Failed to rank cards: %r" % cards
    return rank
 
def handy(cards='2♥ 2♦ 2♣ k♣ q♦'):
    hand = []
    for card in cards.split():
        f, s = card[:-1], card[-1]
        assert f in face, "Invalid: Don't understand card face %r" % f
        assert s in suit, "Invalid: Don't understand card suit %r" % s
        hand.append(Card(f, s))
    assert len(hand) == 7, "Invalid: Must be 5 cards in a hand, not %i" % len(hand)
    assert len(set(hand)) == 7, "Invalid: All cards in the hand must be unique %r" % cards
    return hand
 
'''
if __name__ == '__main__':
    hands = ["2♥ 2♦ 2♣ k♣ q♦",
     "2♥ 5♥ 7♦ 8♣ 9♠",
     "a♥ 2♦ 3♣ 4♣ 5♦",
     "2♥ 3♥ 2♦ 3♣ 3♦",
     "2♥ 7♥ 2♦ 3♣ 3♦",
     "2♥ 7♥ 7♦ 7♣ 7♠",
     "10♥ j♥ q♥ k♥ a♥"] + [
     "4♥ 4♠ k♠ 5♦ 10♠",
     "q♣ 10♣ 7♣ 6♣ 4♣",
     ]
    print("%-18s %-15s %s" % ("HAND", "CATEGORY", "TIE-BREAKER"))
    for cards in hands:
        r = rank(cards)
        print("%-20r %-15s %r" % (cards, r[0], r[1]))
'''

