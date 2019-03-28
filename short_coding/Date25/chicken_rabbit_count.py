def chicken_rabbit_count(heads, legs):
    for chicken in range(0, heads + 1):
        rabbit = heads - chicken
        total = 4 * rabbit + 2 * chicken
        if total == legs:
            print("chicken:{} rabbit:{}".format(chicken,rabbit))


heads = 28
legs = 82
chicken_rabbit_count(heads, legs)

# heads=> a+b=35
# legs=>2a+4b=94
