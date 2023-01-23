if __name__ == '__main__':
    record = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name,score])
    score_ls = list(set([ls[1] for ls in record]))
    val_score = sorted(score_ls)[1]
    print(*(sorted([ls[0] for ls in record if ls[1] == val_score])),sep = "\n")