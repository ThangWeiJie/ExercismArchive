def value(colors: list[str]) -> int:
    ans = 0

    color_resistance_map = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    for color_index in range(0, 2):
        curr_color = colors[color_index]
        resistance = color_resistance_map.get(curr_color)

        ans = ans * 10 + resistance

    return ans
