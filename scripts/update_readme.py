import re
import urllib.request
from collections import Counter
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS = ROOT / "Data Structures & Algorithms"
README = ROOT / "README.md"
NEETCODE = "https://neetcode.io/"

DIFFICULTIES = ["Easy", "Medium", "Hard", "Unknown"]


def fetch_problems():
    html = urllib.request.urlopen(NEETCODE).read().decode()
    bundle = urllib.request.urlopen(NEETCODE + re.search(r"main\.[0-9a-f]+\.js", html)[0]).read().decode()
    entries = sorted(re.findall(r'\{problem:"[^{}]*\}', bundle), key=lambda e: "neetcode150:!0" not in e)
    problems = {}
    for entry in entries:
        fields = dict(re.findall(r'(\w+):"([^"]*)"', entry))
        if "ncLink" in fields:
            problems.setdefault(fields["ncLink"].strip("/"), (fields["pattern"], fields["difficulty"], fields["problem"]))
    if not problems:
        raise SystemExit("Found no problem data in the NeetCode bundle")
    return problems


def latest_submission(problem_dir):
    return max(
        problem_dir.glob("submission-*.*"), key=lambda p: int(re.search(r"\d+", p.stem).group()), default=None
    )


def render():
    problems = fetch_problems()
    topic_order = list(dict.fromkeys(topic for topic, _, _ in problems.values())) + ["Other"]
    by_topic = {}
    difficulty_counts = Counter()
    for problem_dir in sorted(p for p in SOLUTIONS.iterdir() if p.is_dir()):
        slug = problem_dir.name
        topic, difficulty, title = problems.get(slug, ("Other", "Unknown", slug))
        submission = latest_submission(problem_dir)
        if submission is None:
            continue
        latest = submission.relative_to(ROOT).as_posix()
        by_topic.setdefault(topic, []).append((
            title,
            f'<td><a href="https://neetcode.io/problems/{slug}">{escape(title)}</a></td>'
            f'<td>{difficulty}</td><td><a href="{quote(latest)}">code</a></td>',
        ))
        difficulty_counts[difficulty] += 1

    solved = sum(difficulty_counts.values())
    breakdown = " · ".join(f"{difficulty_counts[d]} {d}" for d in DIFFICULTIES if difficulty_counts[d])
    lines = [
        f"**{solved} problems solved** ({breakdown})",
        "",
        "<table>",
        "<tr><th>Topic</th><th>Problem</th><th>Difficulty</th><th>Latest</th></tr>",
    ]
    for topic in topic_order:
        rows = sorted(by_topic.get(topic, []))
        for i, (_, row) in enumerate(rows):
            topic_cell = f'<td rowspan="{len(rows)}">{escape(topic)}</td>' if i == 0 else ""
            lines.append(f"<tr>{topic_cell}{row}</tr>")
    lines.append("</table>")
    return "\n".join(lines)


def main():
    readme = README.read_text()
    updated, count = re.subn(
        r"(<!-- progress:start -->).*?(<!-- progress:end -->)",
        lambda m: f"{m[1]}\n{render()}\n{m[2]}",
        readme,
        flags=re.DOTALL,
    )
    if count != 1:
        raise SystemExit("README.md needs exactly one progress:start/progress:end marker pair")
    README.write_text(updated)


if __name__ == "__main__":
    main()
