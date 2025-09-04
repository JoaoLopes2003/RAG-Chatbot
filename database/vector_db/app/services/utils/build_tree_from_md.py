from enum import Enum
import re
import json

class MdElement(Enum):
    HEADING = 1
    BULLET_POINTS = 2
    TABLE = 3
    TEXT = 4
    BLANK = 5

def get_md_element_type(line: str) -> MdElement:
    """Returns the type of the Markdown element present in a line."""
    stripped_line = line.strip()
    if not stripped_line:
        return MdElement.BLANK
    if re.search("^#+\s", stripped_line):
        return MdElement.HEADING
    # Check for bullet points (-, *, +) or numbered lists (1., 2.)
    elif re.search(r"^(?:[-*+]\s|\d+\.\s)", stripped_line):
        return MdElement.BULLET_POINTS
    elif re.search(r"^\|.*\|$", stripped_line):
        return MdElement.TABLE
    else:
        return MdElement.TEXT

def get_heading_level(line: str) -> int:
    """Returns the level of the heading."""
    match = re.match(r"^(#+)\s", line.strip())
    if match:
        return len(match.group(1))
    return 0

def build_tree_from_md(path: str) -> list:
    """
    Builds an element tree from a Markdown file, including character start and end positions.
    """
    tree = []
    stack = []
    is_parsing_table = False
    table_accumulator = []
    table_start_pos = 0
    current_pos = 0

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line_start_pos = current_pos
        line_end_pos = line_start_pos + len(line)
        el_type = get_md_element_type(line)
        content = line.strip()

        if el_type == MdElement.TABLE:
            if not is_parsing_table:
                # A new table has started
                is_parsing_table = True
                table_start_pos = line_start_pos
            table_accumulator.append(content)
        elif is_parsing_table:

            is_parsing_table = False
            table_content = "\n".join(table_accumulator)

            table_end_pos = line_start_pos 
            node = {
                "type": MdElement.TABLE.name,
                "content": table_content,
                "start_pos": table_start_pos,
                "end_pos": table_end_pos,
            }
            if not stack:
                tree.append(node)
            else:
                stack[-1][1]["children"].append(node)
            table_accumulator = []
        
        if is_parsing_table:
            current_pos = line_end_pos
            continue

        if el_type == MdElement.BLANK:
            current_pos = line_end_pos
            continue

        if el_type == MdElement.HEADING:
            level = get_heading_level(content)
            node = {
                "type": el_type.name,
                "level": level,
                "content": content,
                "start_pos": line_start_pos,
                "children": [],
                # end_pos will be set later
            }

            # Set the end position for parent nodes that are now being closed.
            while stack and stack[-1][0] >= level:
                closed_node_dict = stack.pop()[1]
                closed_node_dict["end_pos"] = line_start_pos

            if not stack:
                tree.append(node)
            else:
                parent_node = stack[-1][1]
                parent_node["children"].append(node)
            
            stack.append((level, node))

        elif el_type in [MdElement.TEXT, MdElement.BULLET_POINTS]:
            node = {
                "type": el_type.name,
                "content": content,
                "start_pos": line_start_pos,
                "end_pos": line_end_pos,
            }
            if not stack:
                tree.append(node)
            else:
                current_parent = stack[-1][1]
                current_parent["children"].append(node)
        
        # Update position for the next line
        current_pos = line_end_pos

    # If the file ends with a table, process it
    if is_parsing_table:
        table_content = "\n".join(table_accumulator)
        node = {
            "type": MdElement.TABLE.name,
            "content": table_content,
            "start_pos": table_start_pos,
            "end_pos": current_pos,
        }
        if not stack:
            tree.append(node)
        else:
            stack[-1][1]["children"].append(node)

    while stack:
        open_node_dict = stack.pop()[1]
        open_node_dict["end_pos"] = current_pos

    return tree