#Задайте список из вещественных чисел и найдите разницу между макс и мин значениеями дробной части


text = [1.1,1.2,3.1,4,10.05]
text2 = []
for i in range(len(text)):
    if text[i] % 1 !=0:
        text2.append(text[i])
text3 = [round(text2[i] % 1, 2)
for i in range(len(text2))]
print(f"{text3} -> {max(text3) - min(text3)}")
