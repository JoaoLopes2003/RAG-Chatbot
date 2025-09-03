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
    Builds an element tree from a Markdown file. Levels are defined by header level.
    """
    tree = []
    stack = []

    # --- State variables for table parsing ---
    is_parsing_table = False
    table_accumulator = []

    def flush_table_to_tree():
        """Helper function to process the accumulated table and add it to the tree."""
        nonlocal is_parsing_table, table_accumulator
        if not table_accumulator:
            return

        # Join the lines and create a single node for the entire table
        table_content = "\n".join(table_accumulator)
        node = {
            "type": MdElement.TABLE.name,
            "content": table_content,
        }
        if not stack:
            tree.append(node)
        else:
            parent_node = stack[-1][1]
            parent_node["children"].append(node)

        # Reset state
        is_parsing_table = False
        table_accumulator = []


    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            el_type = get_md_element_type(line)
            content = line.strip()

            # If the current line is part of a table
            if el_type == MdElement.TABLE:
                is_parsing_table = True
                table_accumulator.append(content)
                continue

            # If we were parsing a table, but the current line is NOT a table line
            if is_parsing_table:
                # The table has ended. Process the accumulated lines.
                flush_table_to_tree()

            if el_type == MdElement.BLANK:
                continue

            if el_type == MdElement.HEADING:
                level = get_heading_level(content)
                node = {
                    "type": el_type.name,
                    "content": content,
                    "children": []
                }
                while stack and stack[-1][0] >= level:
                    stack.pop()
                if not stack:
                    tree.append(node)
                else:
                    parent_node = stack[-1][1]
                    parent_node["children"].append(node)
                stack.append((level, node))

            else: # TEXT or BULLET_POINT
                node = {
                    "type": el_type.name,
                    "content": content,
                }
                if not stack:
                    tree.append(node)
                else:
                    current_parent = stack[-1][1]
                    current_parent["children"].append(node)

    # After the loop, check if the file ended with a table
    flush_table_to_tree()

    return tree