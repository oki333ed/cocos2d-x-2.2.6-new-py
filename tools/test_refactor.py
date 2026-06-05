from pathlib import Path
from fissix import refactor
import traceback
fixers = refactor.get_fixers_from_package('fissix.fixes')
tool = refactor.RefactoringTool(fixers)
files = [
    'tools/bindings-generator/generator.py',
    'tools/jenkins_scripts/mac/iOS_SikuliTest.sikuli/iOS_SikuliTest.py',
    'template/multi-platform-lua/proj.marmalade/cccopy.py',
    'samples/Lua/TestLua/proj.marmalade/cccopy.py',
]
for rel in files:
    p = Path(rel)
    text = p.read_text(encoding='utf-8')
    print('TRY', rel)
    try:
        tool.refactor_string(text, str(p))
        print('OK', rel)
    except Exception:
        traceback.print_exc()
    print('---')
