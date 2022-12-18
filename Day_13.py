'''
5th graders Kara and Rani both have made lemonade stands. Kara sells her lemonade at
5 cents a glass and Rani sells at 7 cents a glass. Kara sold k number of glasses of 
lemonade today and Rani sold r  number of glasses. Who made the most money and by what amount?
k and r are user entered values..
'''

KGlassCount = int(input("Enter Kara's glass count: "))
RGlassCount = int(input("Enter Rani's glass count: "))

KGlassRate = 5
RGlassRate = 7

KaraTotalMoney = KGlassCount * KGlassRate
RaniTotalMoney = RGlassCount * RGlassRate

if KaraTotalMoney > RaniTotalMoney:
  print("Kara has earned more than Rani")
  print("Kara:",KaraTotalMoney,"cents.")
  
elif KaraTotalMoney < RaniTotalMoney:
  print("Rani has earned more than Kara")
  print("Rani:",RaniTotalMoney,"cents.")
  
elif KaraTotalMoney == RaniTotalMoney:
  print("Rani and Kara have earned equal amount.")
