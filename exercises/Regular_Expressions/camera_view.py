import re

skip_num, take_num = input().split()
skip_num, take_num = int(skip_num), int(take_num)

camera = input()
views_list = []
taken_view = []
pattern = r"(\|<)([A-Za-z]+)"
view_match = re.finditer(pattern, camera)
if view_match:
    for match in view_match:
        views_list.append(match.group(2))
for view in views_list:
    current_view = view[skip_num:]
    if len(current_view) > take_num:
        taken_view.append(current_view[:take_num])
    else:
        taken_view.append(current_view)
print(", ".join(taken_view))
