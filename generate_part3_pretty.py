#!/usr/bin/env python3
"""Generate a cleaner Part 3 derivation tree report for all valid test cases."""

from __future__ import annotations

import datetime
import glob
import os
import re
import subprocess
import sys
import shutil


PART3_START = "PART 3: REVERSE DERIVATION TREE"
PART4_START = "PART 4: LALR(1) PARSING TABLE OUTPUT"


def extract_part3_block(parser_output: str) -> list[str]:
    lines = parser_output.splitlines()
    in_block = False
    block: list[str] = []

    for line in lines:
        if PART3_START in line:
            in_block = True
            continue
        if in_block and PART4_START in line:
            break
        if in_block:
            block.append(line.rstrip("\n"))

    # Keep only actual tree lines and remove separator lines.
    tree_lines = [ln for ln in block if "└─" in ln]
    return tree_lines


def parse_tree_line(line: str) -> tuple[int, str, str]:
    indent = len(line) - len(line.lstrip(" "))
    depth = indent // 2

    content = line.split("└─", 1)[1].strip()
    match = re.match(r"^(.*?)\s*\[(.*)\]\s*$", content)
    if match:
        symbol = match.group(1).strip()
        value = match.group(2).strip()
    else:
        symbol = content
        value = ""

    return depth, symbol, value


def run_parser(parser_bin: str, testcase: str) -> str:
    proc = subprocess.run(
        [parser_bin, testcase],
        capture_output=True,
        text=True,
        check=False,
    )
    return proc.stdout


def build_graph_model_from_postorder(tree_lines: list[str]) -> tuple[list[str], list[tuple[int, int]]]:
    """Build node labels and directed edges from post-order lines with depth metadata."""
    if not tree_lines:
        return ["No tree nodes found"], []

    nodes = [parse_tree_line(ln) for ln in tree_lines]
    rev_nodes = list(reversed(nodes))

    labels: list[str] = []
    depths: list[int] = []
    for depth, symbol, value in rev_nodes:
        if value and value != "-":
            label = f"{symbol}\\n[{value}]"
        else:
            label = symbol
        labels.append(label)
        depths.append(depth)

    edges: list[tuple[int, int]] = []
    for child_idx, child_depth in enumerate(depths):
        if child_depth == 0:
            continue
        parent_idx = -1
        for cand_idx in range(child_idx - 1, -1, -1):
            if depths[cand_idx] == child_depth - 1:
                parent_idx = cand_idx
                break
        if parent_idx >= 0:
            edges.append((parent_idx, child_idx))

    return labels, edges


def build_mermaid(labels: list[str], edges: list[tuple[int, int]]) -> str:
    if not labels:
        return "graph TD\n  A[\"No tree nodes found\"]\n"

    out = ["graph TD"]
    for i, label in enumerate(labels):
        safe = label.replace('"', "'")
        out.append(f'  n{i}["{safe}"]')
    for p, c in edges:
        out.append(f"  n{p} --> n{c}")

    return "\n".join(out) + "\n"


def build_dot(labels: list[str], edges: list[tuple[int, int]]) -> str:
    out = [
        "digraph DerivationTree {",
        "  rankdir=TB;",
        "  node [shape=box, style=rounded, fontname=\"Helvetica\"];",
    ]

    for i, label in enumerate(labels):
        safe = label.replace('"', r'\"')
        out.append(f'  n{i} [label="{safe}"];')

    for p, c in edges:
        out.append(f"  n{p} -> n{c};")

    out.append("}")
    return "\n".join(out) + "\n"


def safe_name(path: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", path)


def main() -> int:
    root = os.path.dirname(os.path.abspath(__file__))
    parser_bin = os.path.join(root, "brolang_parser")
    if not os.path.exists(parser_bin):
        print("Error: brolang_parser not found. Build first with 'make'.", file=sys.stderr)
        return 1

    testcases = sorted(glob.glob(os.path.join(root, "testcases", "valid", "*.bro")))
    if not testcases:
        print("Error: no valid testcases found.", file=sys.stderr)
        return 1

    out_path = os.path.join(root, "PART3_DERIVATION_TREE_PRETTY.md")
    graphs_dir = os.path.join(root, "part3_graphs")
    os.makedirs(graphs_dir, exist_ok=True)
    dot_bin = shutil.which("dot")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(out_path, "w", encoding="utf-8") as out:
        out.write("# Part 3 - Reverse Derivation Trees (Improved Representation)\n\n")
        out.write(f"Generated on: {now}\n\n")
        if dot_bin:
            out.write("Graph images: PNG files are available in part3_graphs/.\n\n")
        else:
            out.write("Graph images: Graphviz not found; DOT files are available in part3_graphs/.\n\n")

        for tc in testcases:
            rel_tc = os.path.relpath(tc, root)
            parser_output = run_parser(parser_bin, tc)
            tree_lines = extract_part3_block(parser_output)
            labels, edges = build_graph_model_from_postorder(tree_lines)
            mermaid = build_mermaid(labels, edges)
            dot_text = build_dot(labels, edges)

            base = safe_name(rel_tc)
            dot_path = os.path.join(graphs_dir, f"{base}.dot")
            png_path = os.path.join(graphs_dir, f"{base}.png")

            with open(dot_path, "w", encoding="utf-8") as dot_file:
                dot_file.write(dot_text)

            if dot_bin:
                subprocess.run([dot_bin, "-Tpng", dot_path, "-o", png_path], check=False)

            out.write(f"## Testcase: {rel_tc}\n\n")
            out.write("### Tree View (Post-Order)\n\n")
            out.write("```text\n")
            if tree_lines:
                for ln in tree_lines:
                    out.write(f"{ln}\n")
            else:
                out.write("(No derivation tree lines found)\n")
            out.write("```\n\n")

            out.write("### Graph View (Mermaid)\n\n")
            out.write("```mermaid\n")
            out.write(mermaid)
            out.write("```\n\n")

            out.write("### Exported Graph Files\n\n")
            out.write(f"- DOT: part3_graphs/{base}.dot\n")
            if dot_bin:
                out.write(f"- PNG: part3_graphs/{base}.png\n\n")
            else:
                out.write("- PNG: Not generated (install Graphviz to enable PNG export)\n\n")

            out.write("### Structured Reduction Trace\n\n")
            out.write("| Step | Depth | Symbol | Value |\n")
            out.write("|---:|---:|---|---|\n")

            if tree_lines:
                for i, ln in enumerate(tree_lines, start=1):
                    depth, symbol, value = parse_tree_line(ln)
                    safe_symbol = symbol.replace("|", "\\|")
                    safe_value = value.replace("|", "\\|") if value else "-"
                    out.write(f"| {i} | {depth} | {safe_symbol} | {safe_value} |\n")
            else:
                out.write("| - | - | - | - |\n")

            out.write("\n")

    print(f"Generated: {out_path}")
    if dot_bin:
        print(f"Exported DOT + PNG files in: {graphs_dir}")
    else:
        print(f"Exported DOT files in: {graphs_dir}")
        print("Note: install Graphviz ('dot') to generate PNG files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
