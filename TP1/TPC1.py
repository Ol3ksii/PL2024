import sys

def on_off_summation():
    text = sys.stdin.read()
    summation_on = True
    total = 0
    num_buf = ""

    i = 0
    while i < len(text):
        c = text[i]

        if c.isdigit():
            num_buf += c
            print(c, end="")
            i += 1
            continue

        if num_buf:
            if summation_on:
                total += int(num_buf)
            num_buf = ""

        low_slice_2 = text[i:i+2].lower()
        low_slice_3 = text[i:i+3].lower()

        if low_slice_2 == "on":
            summation_on = True
            print(text[i:i+2], end="")
            i += 2
            continue
        elif low_slice_3 == "off":
            summation_on = False
            print(text[i:i+3], end="")
            i += 3
            continue

        if c == "=":
            print("=", end="")
            print(f"\n>> {total}")
        else:
            print(c, end="")

        i += 1

    if num_buf and summation_on:
        total += int(num_buf)

    print(f"\n>> {total}")

if __name__ == "__main__":
    on_off_summation()
