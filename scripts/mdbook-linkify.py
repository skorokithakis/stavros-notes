#!/usr/bin/env python3
import json
import re
import sys

# Bare URL matcher (kept intentionally simple)
URL_RE = re.compile(r"\bhttps?://[^\s<>()]+")
TRAILING_PUNCT = ".,;:!?)\"'"

# Things we should NOT touch
FENCED_CODE_RE = re.compile(r"(^|\n)(```|~~~)[^\n]*\n.*?\n\2[ \t]*(?=\n|$)", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
# Raw HTML tags should be left as-is, including attributes with URLs.
HTML_TAG_RE = re.compile(r"<[^>]+>")
# Inline links & images: [text](dest) and ![alt](dest)
# This is a pragmatic regex; it won't perfectly handle all nested parentheses,
# but it avoids breaking normal links like the one you showed.
INLINE_LINK_RE = re.compile(r"!?(\[[^\]]*\])\([^\)]*\)")
# HTML attributes containing URLs (href, src, value, etc.). Matches both single and
# double quoted attributes. This prevents linkifying URLs that are already in HTML.
HTML_ATTR_RE = re.compile(r'(?:href|src|value)\s*=\s*["\'][^"\']*["\']')


def mask(text: str, pattern: re.Pattern, store: list, tag: str) -> str:
    def repl(m: re.Match) -> str:
        store.append(m.group(0))
        return f"@@{tag}{len(store)-1}@@"

    return pattern.sub(repl, text)


def unmask(text: str, store: list, tag: str) -> str:
    # Replace placeholders back to originals
    def repl(m: re.Match) -> str:
        idx = int(m.group(1))
        return store[idx]

    return re.sub(rf"@@{tag}(\d+)@@", repl, text)


def linkify_bare_urls(text: str) -> str:
    def repl(m: re.Match) -> str:
        url = m.group(0)
        suffix = ""
        while url and url[-1] in TRAILING_PUNCT:
            suffix = url[-1] + suffix
            url = url[:-1]
        return f"<{url}>{suffix}"

    return URL_RE.sub(repl, text)


def transform_markdown(text: str) -> str:
    store = []

    # Mask in a safe order: big structures first.
    text = mask(text, FENCED_CODE_RE, store, "M")
    text = mask(text, HTML_TAG_RE, store, "M")
    text = mask(text, INLINE_LINK_RE, store, "M")
    text = mask(text, INLINE_CODE_RE, store, "M")
    text = mask(text, HTML_ATTR_RE, store, "M")

    text = linkify_bare_urls(text)

    text = unmask(text, store, "M")
    return text


def walk_items(items):
    for item in items:
        if "Chapter" in item:
            ch = item["Chapter"]
            if isinstance(ch.get("content"), str):
                ch["content"] = transform_markdown(ch["content"])
            sub = ch.get("sub_items")
            if isinstance(sub, list):
                walk_items(sub)


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "supports":
        renderer = sys.argv[2] if len(sys.argv) >= 3 else ""
        sys.exit(0 if renderer in ("html", "markdown") else 1)

    ctx, book = json.load(sys.stdin)

    if isinstance(book, dict):
        if isinstance(book.get("sections"), list):
            walk_items(book["sections"])
        elif isinstance(book.get("items"), list):
            walk_items(book["items"])

    json.dump(book, sys.stdout)


if __name__ == "__main__":
    main()
