import re, random

# print("Print a random string containing 0 or 1:")

total = ""

count_zero_patern_one = 0
count_one_patter_one = 0
count_zero_patern_two = 0
count_one_patter_two = 0
count_zero_patern_three = 0
count_one_patter_three = 0
count_zero_patern_four = 0
count_one_patter_four = 0
count_zero_patern_five = 0
count_one_patter_five = 0
count_zero_patern_six = 0
count_one_patter_six = 0
count_zero_patern_seven = 0
count_one_patter_seven = 0
count_zero_patern_eight = 0
count_one_patter_eight = 0
n = 4

triad_templates = ["000", "001", "010", "011", "100", "101", "110", "111"]

print("Please give AI some data to learn...")
print("The current data length is 0, 100 symbols left")
while True:
    print("Print a random string containing 0 or 1:" + "\n")
    custom_input = input()  # temp comment for optimazing and increasing  developing stage 3 in the end will uncomment
    # custom_input = "010100101001010101111110001001011000010101010101010010101010101001010010101010001111001010010101010010101010101" # temp variable
    filter = re.sub(r"[2-9A-Za-z_\-]", '', custom_input)
    total = total + filter
    if len(total) < 100:
        print(f"The current data length is {len(total)}, {100 - len(total)} symbols left")
        # print("Print a random string containing 0 or 1:" + "\n")
    elif len(total) == 100:
        print(f"The current data length is {len(total)}, {100 - len(total)} symbols left")
        # print("Print a random string containing 0 or 1:" + "\n")
        break
    else:
        break

split_total = [total[i:i + n] for i in range(0, len(total) - 3)]

for i in split_total:
    if i[len(i) - 1] == "0" and i[0:3] == triad_templates[0]:
        count_zero_patern_one += 1
    if i[len(i) - 1] == "1" and i[0:3] == triad_templates[0]:
        count_one_patter_one += 1
    if i[len(i) - 1] == "0" and i[0:3] == triad_templates[1]:
        count_zero_patern_two += 1
    if i[len(i) - 1] == "1" and i[0:3] == triad_templates[1]:
        count_one_patter_two += 1
    if i[len(i) - 1] == "0" and i[0:3] == triad_templates[2]:
        count_zero_patern_three += 1
    if i[len(i) - 1] == "1" and i[0:3] == triad_templates[2]:
        count_one_patter_three += 1
    if i[len(i) - 1] == "0" and i[0:3] == triad_templates[3]:
        count_zero_patern_four += 1
    if i[len(i) - 1] == "1" and i[0:3] == triad_templates[3]:
        count_one_patter_four += 1
    if i[len(i) - 1] == "0" and i[0:3] == triad_templates[4]:
        count_zero_patern_five += 1
    if i[len(i) - 1] == "1" and i[0:3] == triad_templates[4]:
        count_one_patter_five += 1
    if i[len(i) - 1] == "0" and i[0:3] == triad_templates[5]:
        count_zero_patern_six += 1
    if i[len(i) - 1] == "1" and i[0:3] == triad_templates[5]:
        count_one_patter_six += 1
    if i[len(i) - 1] == "0" and i[0:3] == triad_templates[6]:
        count_zero_patern_seven += 1
    if i[len(i) - 1] == "1" and i[0:3] == triad_templates[6]:
        count_one_patter_seven += 1
    if i[len(i) - 1] == "0" and i[0:3] == triad_templates[7]:
        count_zero_patern_eight += 1
    if i[len(i) - 1] == "1" and i[0:3] == triad_templates[7]:
        count_one_patter_eight += 1

    # if i[0] == "0" and i[-3:] == triad_templates[0]:
    #     count_zero_patern_one += 1
    # if i[0] == "1" and i[-3:] == triad_templates[0]:
    #     count_one_patter_one += 1
    # if i[0] == "0" and i[-3:] == triad_templates[1]:
    #     count_zero_patern_two += 1
    # if i[0] == "1" and i[-3:] == triad_templates[1]:
    #     count_one_patter_two += 1
    # if i[0] == "0" and i[-3:] == triad_templates[2]:
    #     count_zero_patern_three += 1
    # if i[0] == "1" and i[-3:] == triad_templates[2]:
    #     count_one_patter_three += 1
    # if i[0] == "0" and i[-3:] == triad_templates[3]:
    #     count_zero_patern_four += 1
    # if i[0] == "1" and i[-3:] == triad_templates[3]:
    #     count_one_patter_four += 1
    # if i[0] == "0" and i[-3:] == triad_templates[4]:
    #     count_zero_patern_five += 1
    # if i[0] == "1" and i[-3:] == triad_templates[4]:
    #     count_one_patter_five += 1
    # if i[0] == "0" and i[-3:] == triad_templates[5]:
    #     count_zero_patern_six += 1
    # if i[0] == "1" and i[-3:] == triad_templates[5]:
    #     count_one_patter_six += 1
    # if i[0] == "0" and i[-3:] == triad_templates[6]:
    #     count_zero_patern_seven += 1
    # if i[0] == "1" and i[-3:] == triad_templates[6]:
    # if i[len(i) - 1] == "0" and i[0:3] == triad_templates[6]:
    #     count_zero_patern_seven += 1
    # if i[len(i) - 1] == "1" and i[0:3] == triad_templates[6]:
    #     count_one_patter_seven += 1
    # if i[0] == "0" and i[-3:] == triad_templates[7]:
    #     count_zero_patern_eight += 1
    # if i[0] == "1" and i[-3:] == triad_templates[7]:
    #     count_one_patter_eight += 1
    # if i[len(i) - 1] == "0" and i[0:3] == triad_templates[7]:
    #     count_zero_patern_eight += 1
    # if i[len(i) - 1] == "1" and i[0:3] == triad_templates[7]:
    #     count_one_patter_eight += 1

# ----------------- This part print total final string _____
print()
print("Final data string:")
print(total)

# print(total)
# _______________________________________________________________

print("""
You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!
""")

balance = 1000

# This part show statistics of triad

# print(f"000: {count_zero_patern_one},{count_one_patter_one}")
# print(f"001: {count_zero_patern_two},{count_one_patter_two}")
# print(f"010: {count_zero_patern_three},{count_one_patter_three}")
# print(f"011: {count_zero_patern_four},{count_one_patter_four}")
# print(f"100: {count_zero_patern_five},{count_one_patter_five}")
# print(f"101: {count_zero_patern_six},{count_one_patter_six}")
# print(f"110: {count_zero_patern_seven},{count_one_patter_seven}")
# print(f"111: {count_zero_patern_eight},{count_one_patter_eight}")

predict_triad_zero_pattern_one = count_zero_patern_one
predict_triad_one_pattern_one = count_one_patter_one
predict_triad_zero_pattern_two = count_zero_patern_two
predict_triad_one_pattern_two = count_one_patter_two
predict_triad_zero_pattern_three = count_zero_patern_three
predict_triad_one_pattern_three = count_one_patter_three
predict_triad_zero_pattern_four = count_zero_patern_four
predict_triad_one_pattern_four = count_one_patter_four
predict_triad_zero_pattern_five = count_zero_patern_five
predict_triad_one_pattern_five = count_one_patter_five
predict_triad_zero_pattern_six = count_zero_patern_six
predict_triad_one_pattern_six = count_one_patter_six
predict_triad_zero_pattern_seven = count_zero_patern_seven
predict_triad_one_pattern_seven = count_one_patter_seven
predict_triad_zero_pattern_eight = count_zero_patern_eight
predict_triad_one_pattern_eight = count_one_patter_eight

triad_count_list = [predict_triad_zero_pattern_one, predict_triad_one_pattern_one, predict_triad_zero_pattern_two,
                    predict_triad_one_pattern_two, predict_triad_zero_pattern_three, predict_triad_one_pattern_three,
                    predict_triad_zero_pattern_four, predict_triad_one_pattern_four, predict_triad_zero_pattern_five,
                    predict_triad_one_pattern_five, predict_triad_zero_pattern_six, predict_triad_one_pattern_six,
                    predict_triad_zero_pattern_seven, predict_triad_one_pattern_seven, predict_triad_zero_pattern_eight,
                    predict_triad_one_pattern_eight]


while True:
    # print("Please enter a test string containing 0 or 1:")
    print("Print a random string containing 0 or 1:")
    print()
    user_text = input() # temp comment for optimazing and increasing  developing stage 3 in the end will uncomment
    if user_text == "enough":
        print("Game over!")
        break
    if not re.search('[a-zA-Z]', user_text):
        random_num = ""
        cycle = 0

        while cycle < 3:
            x = random.randint(0, 1)
            random_num = random_num + str(x)
            cycle += 1

        predicted_string = user_text[0:3]

        predicted_result = ""

        total = len(user_text) - 3
        s = 0
        end = 3
        for i in range(total):
            triad = user_text[s:end]
            if triad == triad_templates[0]:
                predicted_string += '0' if triad_count_list[0] >= triad_count_list[1] else '1'
            if triad == triad_templates[1]:
                predicted_string += '0' if triad_count_list[2] >= triad_count_list[3] else '1'
            if triad == triad_templates[2]:
                predicted_string += '0' if triad_count_list[4] >= triad_count_list[5] else '1'
            if triad == triad_templates[3]:
                predicted_string += '0' if triad_count_list[6] >= triad_count_list[7] else '1'
            if triad == triad_templates[4]:
                predicted_string += '0' if triad_count_list[8] >= triad_count_list[9] else '1'
            if triad == triad_templates[5]:
                predicted_string += '0' if triad_count_list[10] >= triad_count_list[11] else '1'
            if triad == triad_templates[6]:
                predicted_string += '0' if triad_count_list[12] >= triad_count_list[13] else '1'
            if triad == triad_templates[7]:
                predicted_string += '0' if triad_count_list[14] >= triad_count_list[15] else '1'
            s += 1
            end += 1

        count_guessed_num = 0

        j = 0

        for i in user_text[:-3]:
            if i == predicted_string[j]:
                count_guessed_num += 1
            j += 1

        percent_result = float(count_guessed_num / (len(user_text) - 3) * 100)

        predicted_result = random_num + predicted_string

        if count_guessed_num > 0:
            balance = balance - 2 * count_guessed_num + len(user_text) - 3
        else:
            balance += 1

        print("prediction:")
        print(predicted_string + "\n")
        print(f"Computer guessed right {count_guessed_num} out of {len(user_text) - 3} symbols ({round(percent_result, 2)} %)")
        print(f"Your balance is now ${balance}")
        print()
    else:
        print()
