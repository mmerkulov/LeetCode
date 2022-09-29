# Определите, сколько рублей и копеек нужно заплатить за N пирожков, если пирожок в столовой стоит А рублей и В копеек.
# На вход 3 числа: рубли, копейки и количество пирожков. На выходе 2 числа: рубли и копейки.

# 5, 3, 66 = 5*3 = 15 + 5*66/100 (330) = 18 rub 30 penny
# 5, 3, 50 = 5*3 = 15 + 5*50/100 (250) = 17 rub 50 penny
def total_price(amount_cooky, rub, penny):  # 5, 3, 66 = 5*3 = 15 + 5*66/100 (330) = 18 rub 30 penny
    total = amount_cooky * rub + amount_cooky * penny / 100
    rub_final = int(total)
    penny_position = str(total).find('.') + 1
    # print(f'penny_pos = {penny_position}')
    penny_final = int(str(total)[penny_position:])
    # print(f'total = {total}')
    return rub_final, penny_final


amount_cooky = 5
rub = 3
penny = 66

print(f'Amount cooky = {amount_cooky}', f'rub = {rub}', f'penny = {penny}')
print(total_price(amount_cooky, rub, penny))
