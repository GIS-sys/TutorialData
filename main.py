from creator import Creator


data = [
    ['x', 'y'],
    [1, 2, 3],
    ['a']
]
Creator.xlsx(data, "simple_random.xlsx")
Creator.csv(data, "simple_random.csv")
