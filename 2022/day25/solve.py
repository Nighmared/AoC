pubkey1 = 13316116
pubkey2 = 13651422


def find_secret(pubkey: int, subject_num: int = 1) -> int:
    iter_count = 0
    while subject_num != pubkey and iter_count < 1_000_000:
        subject_num = subject_num * 7
        subject_num = subject_num % 20201227
        iter_count += 1
    return iter_count


def get_enc(secret: int, other_pubkey: int) -> int:
    val = 1
    for i in range(secret):
        val = val * other_pubkey
        val = val % 20201227
    return val


secret = find_secret(pubkey1)
print("[Part 1]", get_enc(secret, pubkey2))
