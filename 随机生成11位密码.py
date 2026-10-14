import random
import string


def generate_password():
    lower_pool = string.ascii_lowercase  # 26个小写字母
    upper_pool = string.ascii_uppercase  # 26个大写字母
    digits_pool = string.digits  # 0～9
    symbol_pool = string.punctuation  # 特殊字符
    all_pool = lower_pool + upper_pool + digits_pool + symbol_pool
    first_pool = lower_pool + upper_pool
    c_lower = random.choice(lower_pool)
    c_upper = random.choice(upper_pool)
    c_digits = random.choice(digits_pool)
    c_symbol = random.choice(symbol_pool)

    rest = random.choices(all_pool, k=6)

    tail_list = [c_lower, c_upper, c_digits, c_symbol] + rest
    random.shuffle(tail_list)

    password = random.choice(first_pool) + "".join(tail_list)
    return password


if __name__ == '__main__':
    for i in range(10):
        print(generate_password())
