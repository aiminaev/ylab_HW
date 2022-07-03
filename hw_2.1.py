from itertools import permutations


def delta(point_1, point_2):
    return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5


def shortest_path_spot(points_list):
    results = {}

    for x in permutations(points_list[1:]):
        distance = []
        for i in range(len(x) - 1):
            distance.append(delta(x[i], x[i + 1]))
        distance = [delta(points_list[0], x[0])] + distance + [delta(x[-1], points_list[0])]
        points_path = [points_list[0]] + list(x) + [points_list[0]]
        results[sum(distance)] = {'path': points_path, 'distance': distance}

    min_value = sorted(results)[0]
    shortest_path = results[min_value]

    output_data = f"{shortest_path['path'][0]}"
    for i in range(len(shortest_path['path']) - 1):
        output_data += f" -> {shortest_path['path'][i + 1]}[{shortest_path['distance'][i]}]"
    output_data += f" = {min_value}"

    return output_data


if __name__ == '__main__':
    points_list = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
    print(shortest_path_spot(points_list))
