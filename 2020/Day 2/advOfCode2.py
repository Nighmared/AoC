DAY = 2  # DAY NUMBER HERE
lines = open(f"advOfCode{DAY}.txt").readlines()

number_of_valid_pw_1 = 0
number_of_valid_pw_2 = 0


def check_char_occurence(pw: str, char: str, min: int, max: int):
    # pw must contain at lest min and at most max occurences of char
    count = pw.count(char)
    return count <= max and count >= min


def check_policy_2(pw: str, char: str, pos1: int, pos2: int):
    # check if exactly one of given positions in string equals char
    return (pw[pos1] == char) + (pw[pos2] == char) == 1


def check_policy_password(line: str) -> bool:
    # lines have format   int-int letter: string
    policy, pw = line.split(":")[:2]
    pw = pw.strip()  # get rid of leading space before password string
    policy_char = policy.split(" ")[1]
    a, b = policy.split(" ")[0].split("-")
    policy_min, policy_max = int(a), int(b)
    res1 = check_char_occurence(pw, policy_char, policy_min, policy_max)
    res2 = check_policy_2(pw, policy_char, policy_min - 1, policy_max - 1)
    return (res1, res2)


for line in lines:
    res = check_policy_password(line)
    number_of_valid_pw_1 += res[0]  # checks first policy
    number_of_valid_pw_2 += res[1]  # checks part2 policy

print("number of valid pws part1: ", number_of_valid_pw_1)
print("number of valid pws part2: ", number_of_valid_pw_2)
