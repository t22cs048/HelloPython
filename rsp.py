def rsp():
    import random
    #hand1に0,1,2からランダムに代入
    hand1 = random.randint(0, 2)
    hand2 = random.randint(0, 2)
    hands = ["グー", "チョキ", "パー"]
    print(f"Aの手は{hands[hand1]}")
    print(f"Bの手は{hands[hand2]}")
    if hand1 == hand2:
        print("引き分け")
    elif hand1 == 0 and hand2 == 1:
        print("Bの勝ち")
    elif hand1 == 0 and hand2 == 2:
        print("Aの勝ち")
    elif hand1 == 1 and hand2 == 0:
        print("Aの勝ち")
    elif hand1 == 1 and hand2 == 2:
        print("Bの勝ち")
    elif hand1 == 2 and hand2 == 0:
        print("Bの勝ち")
    elif hand1 == 2 and hand2 == 1:
        print("Aの勝ち")