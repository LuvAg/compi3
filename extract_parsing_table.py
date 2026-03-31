#!/usr/bin/env python3
import re

def extract_parsing_table():
    """Extract complete parsing table from brolang_parser.output"""
    
    with open('brolang_parser.output', 'r') as f:
        content = f.read()
    
    # Extract all states
    state_pattern = r'State (\d+)\n(.*?)(?=State \d+|$)'
    matches = re.finditer(state_pattern, content, re.DOTALL)
    
    states = {}
    for match in matches:
        state_num = int(match.group(1))
        state_content = match.group(2).strip()
        states[state_num] = state_content
    
    print(f"Total States Extracted: {len(states)}\n")
    
    # Generate C code for complete table
    print("/* AUTO-GENERATED: Complete parsing table from brolang_parser.output */")
    print(f"#define TOTAL_STATES {len(states)}\n")
    
    # Print each state
    for i in range(len(states)):
        if i in states:
            state_data = states[i]
            # Extract key information
            items = re.findall(r'^\s+(\d+.*?)$', state_data, re.MULTILINE)
            actions = re.findall(r'\s+([\w$]+)\s+(shift|reduce|go to|accept)\s*(.*?)$', state_data, re.MULTILINE)
            
            print(f"// State {i}")
            for action in actions[:5]:  # Show first 5 actions
                print(f"//   {action[0]} -> {action[1]} {action[2]}")
            if len(actions) > 5:
                print(f"//   ... ({len(actions)-5} more)")
            print()

if __name__ == '__main__':
    extract_parsing_table()
