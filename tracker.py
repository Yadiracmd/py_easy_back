import numpy as np
import random


def generate_mouse_path(coordinate_strings, min_step=1, max_step=3, jitter=1.2):
    def generate_path_with_jitter(start, end):
        path = []
        x_diff = end[0] - start[0]
        y_diff = end[1] - start[1]
        distance = np.hypot(x_diff, y_diff)
        num_steps = int(distance // min_step)
        x_step = x_diff / num_steps
        y_step = y_diff / num_steps

        current_pos = list(start)
        path.append(current_pos)

        while distance > max_step:
            step_size = random.uniform(min_step, max_step)
            current_pos = [
                current_pos[0] + x_step * step_size + random.uniform(-jitter, jitter),
                current_pos[1] + y_step * step_size + random.uniform(-jitter, jitter)
            ]
            path.append([round(current_pos[0]), round(current_pos[1])])
            distance -= step_size

        path.append(list(end))
        return path

    parsed_coordinates = [tuple(map(int, coord.split(','))) for coord in coordinate_strings]

    full_path = []
    for i in range(len(parsed_coordinates) - 1):
        start = parsed_coordinates[i]
        end = parsed_coordinates[i + 1]
        path_segment = generate_path_with_jitter(start, end)
        full_path.extend(path_segment)

    if list(parsed_coordinates[-1]) not in full_path:
        full_path.append(list(parsed_coordinates[-1]))

    # 转换为指定的形式
    formatted_path = [{'clientX': point[0], 'clientY': point[1]} for point in full_path]

    return formatted_path

# if __name__ == '__main__':
#     # 使用示例
#     coordinates = ['252,66', '102,74', '180,94']
#     mouse_path = generate_mouse_path(coordinates)
#
#     # 输出结果
#     print(mouse_path)
#     print(len(mouse_path))


# [{'clientX': 140, 'clientY': 119}, {'clientX': 141, 'clientY': 118}, {'clientX': 141, 'clientY': 115}, {'clientX': 142, 'clientY': 113}, {'clientX': 143, 'clientY': 111}, {'clientX': 144, 'clientY': 109}, {'clientX': 143, 'clientY': 107}, {'clientX': 143, 'clientY': 105}, {'clientX': 144, 'clientY': 101}, {'clientX': 143, 'clientY': 100}, {'clientX': 144, 'clientY': 98}, {'clientX': 145, 'clientY': 96}, {'clientX': 145, 'clientY': 93}, {'clientX': 146, 'clientY': 91}, {'clientX': 145, 'clientY': 89}, {'clientX': 145, 'clientY': 87}, {'clientX': 146, 'clientY': 84}, {'clientX': 146, 'clientY': 82}, {'clientX': 146, 'clientY': 79}, {'clientX': 146, 'clientY': 75}, {'clientX': 146, 'clientY': 73}, {'clientX': 147, 'clientY': 71}, {'clientX': 148, 'clientY': 68}, {'clientX': 149, 'clientY': 66}, {'clientX': 150, 'clientY': 63}, {'clientX': 150, 'clientY': 60}, {'clientX': 149, 'clientY': 59}, {'clientX': 149, 'clientY': 58}, {'clientX': 150, 'clientY': 56}, {'clientX': 150, 'clientY': 54}, {'clientX': 150, 'clientY': 53}, {'clientX': 150, 'clientY': 51}, {'clientX': 150, 'clientY': 49}, {'clientX': 150, 'clientY': 48}, {'clientX': 151, 'clientY': 46}, {'clientX': 150, 'clientY': 44}, {'clientX': 151, 'clientY': 41}, {'clientX': 152, 'clientY': 40}, {'clientX': 153, 'clientY': 38}, {'clientX': 152, 'clientY': 35}, {'clientX': 153, 'clientY': 33}, {'clientX': 153, 'clientY': 29}, {'clientX': 147, 'clientY': 30}, {'clientX': 147, 'clientY': 30}, {'clientX': 145, 'clientY': 31}, {'clientX': 142, 'clientY': 30}, {'clientX': 141, 'clientY': 29}, {'clientX': 140, 'clientY': 29}, {'clientX': 138, 'clientY': 29}, {'clientX': 135, 'clientY': 29}, {'clientX': 134, 'clientY': 29}, {'clientX': 132, 'clientY': 28}, {'clientX': 130, 'clientY': 28}, {'clientX': 130, 'clientY': 28}, {'clientX': 127, 'clientY': 28}, {'clientX': 125, 'clientY': 27}, {'clientX': 123, 'clientY': 27}, {'clientX': 121, 'clientY': 26}, {'clientX': 119, 'clientY': 27}, {'clientX': 118, 'clientY': 27}, {'clientX': 117, 'clientY': 28}, {'clientX': 115, 'clientY': 28}, {'clientX': 114, 'clientY': 29}, {'clientX': 111, 'clientY': 30}, {'clientX': 109, 'clientY': 30}, {'clientX': 108, 'clientY': 30}, {'clientX': 107, 'clientY': 29}, {'clientX': 105, 'clientY': 29}, {'clientX': 103, 'clientY': 30}, {'clientX': 100, 'clientY': 31}, {'clientX': 99, 'clientY': 31}, {'clientX': 96, 'clientY': 31}, {'clientX': 93, 'clientY': 31}, {'clientX': 91, 'clientY': 32}, {'clientX': 89, 'clientY': 31}, {'clientX': 88, 'clientY': 31}, {'clientX': 84, 'clientY': 31}, {'clientX': 83, 'clientY': 32}, {'clientX': 80, 'clientY': 32}, {'clientX': 78, 'clientY': 32}, {'clientX': 76, 'clientY': 32}, {'clientX': 74, 'clientY': 33}, {'clientX': 71, 'clientY': 34}, {'clientX': 66, 'clientY': 35}]
