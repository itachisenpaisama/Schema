import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_FILE = os.path.join(os.path.dirname(BASE_DIR), "index.html")

with open(TARGET_FILE, 'r', encoding='utf-8') as f:
    text = f.read()

print('Length in chars:', len(text))
print('Total lines:', text.count('\n'))

open_scripts = text.count('<script')
close_scripts = text.count('</script>')
print(f'Script tags: open={open_scripts}, close={close_scripts}')

required_ids = [
    'mode-btn-schema', 'mode-btn-diary', 'app-bottom-nav', 'toast', 'custom-option-modal',
    'view-edit', 'view-sheet', 'view-archive', 'view-help',
    'view-diary-entry', 'view-diary-list', 'view-diary-stats',
    'input-diary-date', 'diary-mood-slider', 'diary-energy-slider',
    'today-meds-list', 'input-med-efficacy',
    'input-meal-breakfast', 'input-meal-lunch', 'input-meal-dinner', 'input-meal-snacks',
    'water-display', 'water-progress-bar', 'caffeine-display',
    'input-sleep-duration', 'input-sleep-bedtime', 'input-sleep-waketime',
    'input-steps-count', 'input-steps-goal', 'steps-progress-bar',
    'input-adhs-focus', 'input-adhs-restlessness', 'input-adhs-brainfog',
    'input-diary-highlights', 'input-diary-notes', 'stats-chart-container',
    'settings-modal', 'header-btn-settings',
    'settings-tab-modules', 'settings-tab-general',
    'settings-feature-toggles-container', 'settings-active-count-badge',
    'setting-steps-goal', 'setting-water-goal', 'setting-compact-mode', 'setting-start-view',
    'full-backup-import-file', 'diary-all-disabled-notice', 'diary-fallback-save-bar',
    'feature-container-mood', 'feature-container-emotions',
    'feature-container-meds-log', 'feature-container-meds-efficacy',
    'feature-container-meals', 'feature-container-water',
    'feature-container-caffeine', 'feature-container-sleep',
    'feature-container-adhs', 'feature-container-steps',
    'feature-container-positive-things', 'feature-container-highlights',
    'feature-container-notes'
]

missing = [i for i in required_ids if f'id="{i}"' not in text]
if missing:
    print('WARNING: Missing IDs:', missing)
else:
    print('All required IDs present and verified!')
