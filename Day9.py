'''
Mr. Richard Tupper is purchasing gifts for his family. So far he has purchased
- 3 sweaters, each valued at $68
- 1 computer game valued at $75
- 2 bracelets, each valued at $43
later he returned one of the bracelets for a full refund and received a $10 rebate on 
computer game. What is the total cost of the gifts after the refund and rebate?
*Calculation part must be under 3 lines
'''

sweaterPrice = 68
sweaterCount = 3
computerGamePrice = 75
computerGameCount = 1
braceletPrice = 43
braceletCount = 2

#discount and rebate
returnedBraceletCount = 1
rebateOnComputerGame = 10

#calculation
totalGiftPrice = (sweaterPrice*sweaterCount) + (computerGamePrice*computerGameCount) + (braceletPrice*braceletCount)

discountAndRebate = (braceletPrice*returnedBraceletCount) + rebateOnComputerGame

finalGiftPrice = totalGiftPrice + discountAndRebate

print("Final gift price is $", finalGiftPrice)

