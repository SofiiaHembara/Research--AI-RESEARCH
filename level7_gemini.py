def sea_sick(sea):
    """
    This function determines whether someone will get seasick based on a string representing wave conditions.

    Args:
        sea: A string made up of '~' and '_' characters representing waves and calm water, respectively.

    Returns:
        "Throw Up" if the number of changes in wave conditions is more than 20% of the string's length, 
        "No Problem" otherwise.
    """
    # Initialize a counter for the number of changes in wave conditions.
    changes = 0
    # Iterate over the characters in the string, comparing them to the previous character.
    for i in range(1, len(sea)):
        if sea[i] != sea[i-1]:
            changes += 1

    # Check if the number of changes is more than 20% of the string's length.
    if changes > len(sea) * 0.2:
        return "Throw Up"
    else:
        return "No Problem"