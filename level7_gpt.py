def sea_sick(sea):
    # Count the number of changes from calm to wave or from wave to calm
    changes = sum(1 for i in range(1, len(sea)) if sea[i] != sea[i-1])

    # Check if the number of changes is more than 20% of the length of the string
    if changes > 0.2 * len(sea):
        return "Throw Up"
    else:
        return "No Problem"