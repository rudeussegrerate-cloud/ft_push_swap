# from queue import Queue


# frontier = []
# frontier.append(("Strasbourg", 0))
# reached = []
# reached.append("Strasoburg")
# graph = {
#    'Paris': [('Lyon', 1), ('Lille', 1)],
#     'Lille': [('Paris', 1), ('Strasbourg', 1)],
#     'Lyon': [('Paris', 1), ('Strasbourg', 1), ('Marseille', 1)],
#     'Strasbourg': [('Lille', 1), ('Lyon', 1), ('Marseille', 1)],
#     'Marseille': [('Lyon', 1), ('Strasbourg', 1)]
# }
# path = []
# min = ('', 0)
# path.append(frontier[0])
# while frontier:
#     current = frontier.pop(0)
#     for next in graph[current[0]]:
#         if next not in reached:
#             frontier.append(next)
#             reached.append(next)
#     min = ('', 0)
#     for e in frontier:
#        if e[1] > min[1]:
#            min = e
#     if (min[1] and min[0] not in path):
#         path.append(min)
# print(path)
