# Solution 2: adding a dynamic curCast to put all casts into result_list as a list of lists
# The idea of such recursion is weaker because we use looping in essence


def HollywoodBlockBusterGenerator(names, casting_size):
    # TODO
    result_list = []
    generateBillboard(names, casting_size, result_list, 0, [])
    print("All the possible casts: ")
    for cast in result_list:
        print(cast)

    print(f"\nThe total number of casting: {len(result_list)}")


def generateBillboard(names, casting_size, result_list, position, curCast):
    # curCast is list; result_list is list of lists
    # TODO
    # If the current combination is of the desired size, add it to the results
    if len(curCast) == casting_size:
        result_list.append(curCast[:])
        return

    for i in range(position, len(names)):
        # Include the i-th term
        curCast.append(names[i])
        generateBillboard(names, casting_size, result_list, i + 1, curCast)
        # Exclude the i-th term and move to the next position
        curCast.pop()


casting = [
    "Gal Gadot",
    "Al Pacino",
    "Gong Li",
    "Hu Ge",
    "Denzel Washington",
    "Zhang Ziyi",
    "Brad Pitt",
]
HollywoodBlockBusterGenerator(casting, 2)
