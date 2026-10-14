# -*- coding: utf-8 -*-
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from build_index import get_head_and_styles
from generate_app import get_header
from part_schema_views import get_schema_views_html
from part_diary_entry import get_diary_entry_view_html
from part_diary_list import get_diary_list_view_html
from part_diary_stats import get_diary_stats_view_html
from part_bottom_nav import get_bottom_nav_and_toast
from part_js_logic import get_javascript_code

TARGET_FILE = os.path.join(os.path.dirname(BASE_DIR), "index.html")

def main():
    print(f"Assembling {TARGET_FILE}...")
    content = []
    content.append(get_head_and_styles())
    content.append(get_header())
    content.append(get_schema_views_html())
    content.append(get_diary_entry_view_html())
    content.append(get_diary_list_view_html())
    content.append(get_diary_stats_view_html())
    content.append(get_bottom_nav_and_toast())
    content.append(get_javascript_code())

    full_html = "".join(content)
    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"Assembly completed successfully! Total chars: {len(full_html)}")

if __name__ == "__main__":
    main()
