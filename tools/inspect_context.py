from pathlib import Path
files = [
    ('tools/bindings-generator/generator.py', 812, 852),
    ('template/multi-platform-lua/proj.marmalade/cccopy.py', 30, 50),
    ('samples/Lua/TestLua/proj.marmalade/cccopy.py', 30, 50),
]
for rel, start, end in files:
    p = Path(rel)
    lines = p.read_text(encoding='utf-8').splitlines()
    print('FILE', rel)
    for i in range(start - 1, end):
        if 0 <= i < len(lines):
            print(f'{i + 1}: {lines[i]!r}')
    print('---')
