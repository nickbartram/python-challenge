profit_loss = [9,9,9,8,7,6,5,7,8,9,5,50]

for i in range(len(profit_loss)-1):

    profit_loss_difference = profit_loss[i + 1] - profit_loss[i]

print(profit_loss_difference)