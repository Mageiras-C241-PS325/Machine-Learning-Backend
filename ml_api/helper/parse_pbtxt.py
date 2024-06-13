import re

def parse_pbtxt(pbtxt_content):
    # Regular expressions for extracting id, name, and display_name
    id_pattern = re.compile(r'id:\s*(\d+)')
    name_pattern = re.compile(r'name:\s*"([^"]+)"')
    display_name_pattern = re.compile(r'display_name:\s*"([^"]+)"')

    label_map = []

    items = pbtxt_content.split('item {')
    for item in items:
        if not item.strip():
            continue
        
        id_match = id_pattern.search(item)
        name_match = name_pattern.search(item)
        display_name_match = display_name_pattern.search(item)
        
        if id_match and name_match:
            item_dict = {
                'id': int(id_match.group(1)),
                'name': name_match.group(1),
                'display_name': display_name_match.group(1) if display_name_match else name_match.group(1)
            }
            label_map.append(item_dict)

    return label_map