#напишите программу которая найдет произведение пар чисел списка.
import math

text = [1,2,3,4,5]
text2 = []
Line = math.ceil(len(text)/2)
for i in range((Line)):
    text2.append(text[i]*text[-i -1])
print(f"{text} => {text2}")
