def get_fractions(frac1, frac2):
    numerator1, divider1 = map(int, frac1.split("/"))
    numerator2, divider2 = map(int, frac2.split("/"))

    sum_new_numerator = numerator1 * divider2 + numerator2 * divider1
    sum_new_divider = divider1 * divider2
    sum_fraction = str(sum_new_numerator) + '/' + str(sum_new_divider)

    multiplication_new_numerator = numerator1 * numerator2
    multiplication_new_divider = divider1 * divider2
    multiplication_fraction = str(multiplication_new_numerator) + '/' + str(multiplication_new_divider)

    return sum_fraction, multiplication_fraction

frac1 = "1/3"
frac2 = "2/4"
sum_fraction, multiplication_fraction = get_fractions(frac1, frac2)

print(f"Сумма дробей {frac1} и {frac2} равна {sum_fraction}")
print(f"Произведение дробей {frac1} и {frac2} равна {multiplication_fraction}")