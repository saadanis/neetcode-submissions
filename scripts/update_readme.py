"""Regenerate the progress section of README.md from the synced submissions."""

import re
from collections import Counter
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS = ROOT / "Data Structures & Algorithms"
README = ROOT / "README.md"

# NeetCode doesn't sync problem metadata, so new problems need a line here.
# Unlisted ones still show up, under "Other".
PROBLEMS = {
    "duplicate-integer": ("Arrays & Hashing", "Easy"),
    "is-anagram": ("Arrays & Hashing", "Easy"),
    "two-integer-sum": ("Arrays & Hashing", "Easy"),
    "anagram-groups": ("Arrays & Hashing", "Medium"),
    "top-k-elements-in-list": ("Arrays & Hashing", "Medium"),
    "string-encode-and-decode": ("Arrays & Hashing", "Medium"),
    "products-of-array-discluding-self": ("Arrays & Hashing", "Medium"),
    "longest-consecutive-sequence": ("Arrays & Hashing", "Medium"),
    "three-integer-sum": ("Two Pointers", "Medium"),
    "max-water-container": ("Two Pointers", "Medium"),
    "buy-and-sell-crypto": ("Sliding Window", "Easy"),
    "longest-substring-without-duplicates": ("Sliding Window", "Medium"),
    "longest-repeating-substring-with-replacement": ("Sliding Window", "Medium"),
    "minimum-window-with-characters": ("Sliding Window", "Hard"),
    "validate-parentheses": ("Stack", "Easy"),
    "find-minimum-in-rotated-sorted-array": ("Binary Search", "Medium"),
    "find-target-in-rotated-sorted-array": ("Binary Search", "Medium"),
    "reverse-a-linked-list": ("Linked List", "Easy"),
    "merge-two-sorted-linked-lists": ("Linked List", "Easy"),
    "linked-list-cycle-detection": ("Linked List", "Easy"),
    "reorder-linked-list": ("Linked List", "Medium"),
    "remove-node-from-end-of-linked-list": ("Linked List", "Medium"),
    "merge-k-sorted-linked-lists": ("Linked List", "Hard"),
    "invert-a-binary-tree": ("Trees", "Easy"),
    "depth-of-binary-tree": ("Trees", "Easy"),
    "same-binary-tree": ("Trees", "Easy"),
    "subtree-of-a-binary-tree": ("Trees", "Easy"),
    "lowest-common-ancestor-in-binary-search-tree": ("Trees", "Medium"),
    "level-order-traversal-of-binary-tree": ("Trees", "Medium"),
}
TOPIC_ORDER = list(dict.fromkeys(topic for topic, _ in PROBLEMS.values())) + ["Other"]
DIFFICULTIES = ["Easy", "Medium", "Hard"]


def latest_submission(problem_dir):
    return max(problem_dir.glob("submission-*.*"), key=lambda p: int(re.search(r"\d+", p.stem).group()))


def render():
    by_topic = {}
    difficulty_counts = Counter()
    for problem_dir in sorted(p for p in SOLUTIONS.iterdir() if p.is_dir()):
        slug = problem_dir.name
        topic, difficulty = PROBLEMS.get(slug, ("Other", "—"))
        latest = latest_submission(problem_dir).relative_to(ROOT).as_posix()
        title = slug.replace("-", " ").title()
        by_topic.setdefault(topic, []).append(
            f'<td><a href="https://neetcode.io/problems/{slug}">{title}</a></td>'
            f'<td>{difficulty}</td><td><a href="{quote(latest)}">code</a></td>'
        )
        difficulty_counts[difficulty] += 1

    solved = sum(difficulty_counts.values())
    breakdown = " · ".join(f"{difficulty_counts[d]} {d}" for d in DIFFICULTIES)
    # Markdown tables can't merge cells, so this is HTML for the topic rowspan.
    lines = [
        f"**{solved} problems solved** ({breakdown})",
        "",
        "<table>",
        "<tr><th>Topic</th><th>Problem</th><th>Difficulty</th><th>Latest</th></tr>",
    ]
    for topic in TOPIC_ORDER:
        rows = by_topic.get(topic, [])
        for i, row in enumerate(rows):
            topic_cell = f'<td rowspan="{len(rows)}">{escape(topic)}</td>' if i == 0 else ""
            lines.append(f"<tr>{topic_cell}{row}</tr>")
    lines.append("</table>")
    return "\n".join(lines)


def main():
    readme = README.read_text()
    updated = re.sub(
        r"(<!-- progress:start -->\n).*?(<!-- progress:end -->)",
        lambda m: f"{m[1]}{render()}\n{m[2]}",
        readme,
        flags=re.DOTALL,
    )
    README.write_text(updated)


if __name__ == "__main__":
    main()
