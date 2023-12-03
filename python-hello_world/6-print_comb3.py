for d1 in range(10):
    for t2 in range(d1 + 1, 10):
        print("{}{}".format(d1, t2), end=', ' if not (d1 == 8 and t2 == 9) else '')

# Print a newline after the inner loop
print()
