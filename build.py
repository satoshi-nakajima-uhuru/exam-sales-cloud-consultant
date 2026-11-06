"""data/*.json の問題を app.template.html に埋め込み、index.html を生成する。

使い方: python3 build.py
"""
import json
import pathlib

root = pathlib.Path(__file__).parent
questions = []
seen = set()
for f in sorted((root / "data").glob("*.json")):
    for q in json.loads(f.read_text(encoding="utf-8")):
        if q["id"] in seen:
            raise SystemExit(f"duplicate id {q['id']} in {f.name}")
        seen.add(q["id"])
        assert len(q["choices"]) >= 2 and q["answer"], q["id"]
        assert all(0 <= a < len(q["choices"]) for a in q["answer"]), q["id"]
        questions.append(q)

tpl = (root / "app.template.html").read_text(encoding="utf-8")
data = json.dumps(questions, ensure_ascii=False).replace("</", "<\\/")
(root / "index.html").write_text(tpl.replace("/*__DATA__*/[]", data), encoding="utf-8")

by_domain = {}
for q in questions:
    by_domain[q["domain"]] = by_domain.get(q["domain"], 0) + 1
print(f"{len(questions)} questions -> index.html")
for d, n in by_domain.items():
    print(f"  {d}: {n}")
