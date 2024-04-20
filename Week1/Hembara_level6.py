def is_valid_walk(walk):
    # Перевірка, чи кількість кроків дорівнює 10
    if len(walk) != 10:
        return False
    
    # Початкова кількість кроків на кожному напрямку
    direction_count = {
        'n': 0,
        's': 0,
        'e': 0,
        'w': 0
    }
    
    # Підрахунок кількості кроків на кожному напрямку
    for direction in walk:
        direction_count[direction] += 1
    
    # Перевірка збалансованості кількості кроків на північ/південь і схід/захід
    if direction_count['n'] == direction_count['s'] and direction_count['e'] == direction_count['w']:
        return True
    else:
        return False
    
# Розвʼязок задачі, яку згенерував ChatGPT, всі тести пройшли з першого разу
    


def is_valid_walk(walk):
  """
  This function checks if a walk will take 10 minutes and return you to the starting point.

  Args:
      walk: A list of characters representing directions ('n', 's', 'w', 'e').

  Returns:
      True if the walk takes 10 minutes and returns to starting point, False otherwise.
  """
  if len(walk) != 10:  # Check if walk is 10 minutes (10 blocks)
    return False

  # Initialize position trackers
  x = 0
  y = 0

  # Loop through directions and update positions
  for direction in walk:
    if direction == 'n':
      y += 1
    elif direction == 's':
      y -= 1
    elif direction == 'e':
      x += 1
    elif direction == 'w':
      x -= 1

  # Check if final position is (0, 0) - starting point
  return x == 0 and y == 0

# Розвʼязок, який надав Google Gemini, всі тести пройшли зразу