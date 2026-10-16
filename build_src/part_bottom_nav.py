# -*- coding: utf-8 -*-

def get_bottom_nav_and_toast():
    return '''  </main>

  <!-- ======================================================== -->
  <!-- NATIVE BOTTOM NAVIGATION BAR (DYNAMIC)                   -->
  <!-- ======================================================== -->
  <!-- ======================================================== -->
  <!-- NATIVE BOTTOM NAVIGATION BAR (DYNAMIC)                   -->
  <!-- ======================================================== -->
  <nav id="app-bottom-nav" class="no-print fixed bottom-0 left-0 right-0 z-40 backdrop-blur-md border-t flex items-center justify-around px-2 py-1.5 shadow-xs transition-colors duration-200">
    <!-- Populated dynamically via switchAppMode() -->
  </nav>

  <!-- Toast Notification -->
  <div id="toast" class="no-print pointer-events-none fixed top-4 left-1/2 -translate-x-1/2 z-50 transform -translate-y-20 opacity-0 transition-all duration-300 max-w-xs w-auto bg-stone-900/95 dark:bg-stone-800/95 text-stone-100 px-4 py-2 rounded-full shadow-2xl flex items-center gap-2 border border-stone-700/60 text-xs font-medium backdrop-blur-md">
    <div id="toast-icon" class="text-[#6B9A88] font-bold">✓</div>
    <span id="toast-message" data-i18n="toastSaved">Gespeichert</span>
  </div>

  <!-- ======================================================== -->
  <!-- MODAL: EIGENE OPTION PERMANENT HINZUFÜGEN (+)            -->
  <!-- ======================================================== -->
  <div id="custom-option-modal" class="no-print hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-stone-950/40 backdrop-blur-xs transition-opacity duration-200">
    <div class="shadcn-card w-full max-w-sm p-4 space-y-3 shadow-2xl rounded-2xl animate-in fade-in zoom-in-95">
      
      <!-- Modal Header -->
      <div class="flex items-center justify-between pb-2 border-b border-stone-100 dark:border-stone-800">
        <div class="flex items-center gap-2">
          <span id="custom-modal-icon" class="text-base font-bold text-[#4A7264] dark:text-[#7BA896]">+</span>
          <h3 id="custom-modal-title" class="font-serif text-sm font-semibold" data-i18n="customModalTitle">Eigene Option hinzufügen</h3>
        </div>
        <button type="button" onclick="closeCustomOptionModal()" class="p-1 rounded-lg text-stone-400 hover:text-stone-600 dark:hover:text-stone-200 transition" aria-label="Schließen" data-i18n-title="btnClose">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>

      <!-- Modal Fields Container (Injected by category) -->
      <div id="custom-modal-fields" class="space-y-2">
        <!-- Dynamically injected input(s) -->
      </div>

      <!-- Existing Custom Items List (User can delete them anytime) -->
      <div id="custom-modal-existing-wrapper" class="space-y-1.5 pt-1 border-t border-stone-100 dark:border-stone-800 hidden">
        <span class="text-[10px] font-bold uppercase tracking-wider text-stone-400" data-i18n="customModalExistingTitle">Deine bisherigen eigenen Einträge:</span>
        <div id="custom-modal-existing-list" class="flex flex-wrap gap-1 max-h-28 overflow-y-auto p-0.5">
          <!-- Injected items with delete button -->
        </div>
      </div>

      <!-- Modal Action Buttons -->
      <div class="flex items-center justify-end gap-2 pt-1 border-t border-stone-100 dark:border-stone-800">
        <button type="button" onclick="closeCustomOptionModal()" class="px-3 py-1.5 rounded-full border border-stone-200 dark:border-stone-700 text-stone-600 dark:text-stone-300 text-xs font-medium hover:bg-stone-100 dark:hover:bg-stone-800 transition">
          <span data-i18n="btnCancel">Abbrechen</span>
        </button>
        <button type="button" onclick="saveCustomOptionFromModal()" class="px-4 py-1.5 rounded-full btn-primary-theme text-xs font-medium transition shadow-xs">
          <span data-i18n="btnSavePermanent">Dauerhaft speichern</span>
        </button>
      </div>

    </div>
  </div>

  <!-- ======================================================== -->
  <!-- MODAL: APP-EINSTELLUNGEN & MODUL-MANAGER (SETTINGS)       -->
  <!-- ======================================================== -->
  <div id="settings-modal" class="no-print hidden fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-stone-950/40 backdrop-blur-xs transition-opacity duration-200">
    <div class="shadcn-card w-full max-w-lg max-h-[92vh] flex flex-col shadow-2xl rounded-2xl animate-in fade-in zoom-in-95 overflow-hidden">
      
      <!-- Modal Header -->
      <div class="flex items-center justify-between px-4 py-3 border-b border-[var(--border-subtle)] shrink-0">
        <div class="flex items-center gap-2.5 min-w-0">
          <div class="w-8 h-8 rounded-lg bg-[var(--surface-subtle)] border border-[var(--border-subtle)] flex items-center justify-center text-[var(--accent-primary)] shrink-0">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          </div>
          <div class="min-w-0">
            <h3 id="settings-modal-heading" data-i18n="settingsHeading" class="font-serif text-sm sm:text-base font-semibold text-[var(--app-text)] leading-tight truncate">Einstellungen & Module</h3>
            <p id="settings-modal-subheading" data-i18n="settingsSubheading" class="text-[11px] text-[var(--text-muted)] truncate">Passe Module, Sprache und Darstellung an deine Bedürfnisse an.</p>
          </div>
        </div>
        <button type="button" onclick="closeSettingsModal()" class="p-1 rounded-lg text-[var(--text-muted)] hover:text-[var(--app-text)] transition shrink-0" aria-label="Schließen" data-i18n-title="btnClose">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>

      <!-- Segmented Tab Navigation inside Modal -->
      <div class="px-4 pt-2.5 pb-1 border-b border-[var(--border-subtle)] bg-[var(--surface-subtle)] shrink-0">
        <div class="grid grid-cols-2 p-1 rounded-xl bg-[var(--app-bg)] border border-[var(--border-subtle)] text-xs font-semibold shadow-inner">
          <button type="button" id="tab-btn-modules" onclick="switchSettingsTab('modules')" class="settings-tab-btn active py-1.5 px-3 rounded-lg transition text-center shadow-xs">
            <span id="tab-label-modules" data-i18n="tabLabelModules">Tracking-Module</span>
          </button>
          <button type="button" id="tab-btn-general" onclick="switchSettingsTab('general')" class="settings-tab-btn py-1.5 px-3 rounded-lg transition text-center font-medium">
            <span id="tab-label-general" data-i18n="tabLabelGeneral">Allgemein & Sprache</span>
          </button>
        </div>
      </div>

      <!-- Modal Body (Scrollable) -->
      <div class="flex-1 overflow-y-auto p-4 space-y-4">
        
        <!-- ============================================== -->
        <!-- TAB 1: TRACKING-MODULE (FEATURE TOGGLES)       -->
        <!-- ============================================== -->
        <div id="settings-tab-modules" class="space-y-3.5">
          
          <!-- Banner & Presets -->
          <div class="settings-group-panel p-3 rounded-2xl space-y-2.5">
            <div class="flex items-center justify-between gap-2">
              <span class="text-xs font-semibold text-[var(--app-text)] flex items-center gap-1.5">
                <span id="settings-presets-title" data-i18n="settingsPresetsTitle">Schnell-Vorlagen:</span>
              </span>
              <span class="text-[10px] text-[var(--accent-primary)] font-bold" id="settings-active-count-badge">13 aktiv</span>
            </div>
            <p class="text-[11px] text-[var(--text-muted)] leading-snug" id="settings-presets-desc" data-i18n="settingsPresetsDesc">
              Passe das Tagebuch so an, dass du dich nicht überfordert fühlst. Schalte nur die Bereiche ein, die du heute wirklich tracken möchtest.
            </p>
            <div class="flex flex-wrap gap-1.5 pt-0.5">
              <button type="button" onclick="setFeaturePreset('minimal')" class="settings-preset-btn btn-primary-theme text-xs px-2.5 py-1 rounded-lg font-medium transition shadow-xs" data-i18n="presetMinimal">
                Minimal (1-2 Bereiche)
              </button>
              <button type="button" onclick="setFeaturePreset('adhs')" class="settings-preset-btn text-xs px-2.5 py-1 rounded-lg font-medium transition shadow-xs" data-i18n="presetAdhs">
                ADHS & Fokus
              </button>
              <button type="button" onclick="setFeaturePreset('vital')" class="settings-preset-btn text-xs px-2.5 py-1 rounded-lg font-medium transition shadow-xs" data-i18n="presetVital">
                Vital & Routine
              </button>
              <button type="button" onclick="setFeaturePreset('all')" class="settings-preset-btn text-xs px-2.5 py-1 rounded-lg font-medium transition shadow-xs" data-i18n="presetAll">
                Alle an
              </button>
            </div>
          </div>

          <!-- Card Reordering & Master Visibility Section -->
          <div class="settings-group-panel p-3 rounded-2xl space-y-2.5">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-[var(--app-text)] flex items-center gap-1.5">
                <span data-i18n="cardOrderTitle">Karten-Reihenfolge & Hauptbereiche:</span>
              </span>
              <button type="button" onclick="resetCardOrder()" class="text-[10px] text-[var(--text-muted)] hover:text-[var(--app-text)] transition" data-i18n="cardOrderReset">Standard-Reihenfolge</button>
            </div>
            <p class="text-[11px] text-[var(--text-muted)] leading-snug" data-i18n="cardOrderDesc">
              Verschiebe die Karten per Drag & Drop oder mit den Pfeilen, um deinen Check-in genau an deine Routine anzupassen.
            </p>
            <div id="settings-card-order-container" class="space-y-1.5 pt-0.5">
              <!-- Dynamically populated via renderSettingsCardOrderUI() -->
            </div>
          </div>

          <!-- Fine-Grained Feature Toggles Section -->
          <div class="space-y-2 pt-1 border-t border-[var(--border-subtle)]">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-[var(--app-text)]" data-i18n="subFeaturesTitle">Detail-Optionen pro Bereich:</span>
            </div>
            <!-- Feature Toggles List Container (Dynamically populated & synced) -->
            <div id="settings-feature-toggles-container" class="space-y-2">
              <!-- Dynamically injected feature rows with iOS-style toggles -->
            </div>
          </div>

        </div>

        <!-- ============================================== -->
        <!-- TAB 2: ALLGEMEIN, SPRACHE, THEME & BACKUP     -->
        <!-- ============================================== -->
        <div id="settings-tab-general" class="hidden space-y-4">
          
          <!-- 1. SPRACHE / LANGUAGE -->
          <div class="settings-group-panel p-3 rounded-xl space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-[var(--app-text)] flex items-center gap-1.5">
                <span id="label-setting-language" data-i18n="labelSettingLanguage">Sprache / Language:</span>
              </span>
              <span id="current-lang-badge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-[var(--surface-subtle)] text-[var(--accent-primary)] border border-[var(--border-subtle)]">Deutsch</span>
            </div>
            <div class="grid grid-cols-2 gap-2 pt-0.5">
              <button type="button" onclick="setAppLanguage('de')" id="lang-btn-de" class="settings-choice-btn active py-2 px-3 rounded-xl font-bold text-xs flex items-center justify-center gap-1.5 transition">
                <span>Deutsch (DE)</span>
              </button>
              <button type="button" onclick="setAppLanguage('en')" id="lang-btn-en" class="settings-choice-btn py-2 px-3 rounded-xl font-semibold text-xs flex items-center justify-center gap-1.5 transition">
                <span>English (EN)</span>
              </button>
            </div>
          </div>

          <!-- 2. ERSCHEINUNGSBILD / THEME -->
          <div class="settings-group-panel p-3 rounded-xl space-y-2">
            <span class="text-xs font-bold text-[var(--app-text)] flex items-center gap-1.5">
              <span id="label-setting-theme" data-i18n="labelSettingTheme">Erscheinungsbild:</span>
            </span>
            <div class="grid grid-cols-3 gap-1.5 pt-0.5">
              <button type="button" onclick="setAppThemeSetting('light')" id="theme-opt-light" class="theme-choice-btn settings-choice-btn py-2 px-2 rounded-xl text-xs font-semibold text-center transition flex flex-col items-center gap-1">
                <svg class="w-4 h-4 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
                <span class="text-[11px]" data-i18n="themeLight">Hell</span>
              </button>
              <button type="button" onclick="setAppThemeSetting('dark')" id="theme-opt-dark" class="theme-choice-btn settings-choice-btn py-2 px-2 rounded-xl text-xs font-semibold text-center transition flex flex-col items-center gap-1">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
                <span class="text-[11px]" data-i18n="themeDark">Dunkel</span>
              </button>
              <button type="button" onclick="setAppThemeSetting('auto')" id="theme-opt-auto" class="theme-choice-btn settings-choice-btn py-2 px-2 rounded-xl text-xs font-semibold text-center transition flex flex-col items-center gap-1">
                <svg class="w-4 h-4 text-slate-500 dark:text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                <span class="text-[11px]" data-i18n="themeAuto">System</span>
              </button>
            </div>
          </div>

          <!-- 2.5 FARBPROFILE (Hintergrund & Text) -->
          <div class="settings-group-panel p-3 rounded-2xl space-y-2.5">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-[var(--app-text)] flex items-center gap-1.5">
                <span id="label-setting-color-profile" data-i18n="labelSettingColorProfile">Farbprofil (Hintergrund & Text):</span>
              </span>
              <div class="flex items-center gap-1.5">
                <button type="button" onclick="resetToDefaultTheme()" class="settings-reset-theme-btn text-[10px] px-2 py-0.5 rounded-full transition flex items-center gap-1 shadow-2xs" title="Standard-Farben wiederherstellen" data-i18n="btnResetDefaultColors">
                  <svg class="w-3 h-3 text-[var(--text-muted)]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
                  <span>Standard</span>
                </button>
                <span id="current-profile-badge" class="text-[10px] font-medium px-2 py-0.5 rounded-full bg-[var(--surface-subtle)] text-[var(--accent-primary)] border border-[var(--border-subtle)]">Stoic</span>
              </div>
            </div>
            <p class="text-[11px] text-[var(--text-muted)] leading-snug" data-i18n="colorProfileDesc">
              Wähle aus verschiedenen beruhigenden Farbprofilen für Hintergrund, Karten, Text und Nuancen.
            </p>
            <div class="grid grid-cols-2 sm:grid-cols-2 lg:grid-cols-3 gap-2 pt-1" id="color-profiles-container">
              <!-- Dynamically populated via renderColorProfilesUI() -->
            </div>
          </div>

          <!-- 3. TAGESZIELE & START-ANSICHT -->
          <div class="settings-group-panel p-3 rounded-xl space-y-2.5">
            <span class="text-xs font-bold text-[var(--app-text)] flex items-center gap-1.5">
              <span id="label-setting-targets" data-i18n="labelSettingTargets">Tagesziele & Verhalten:</span>
            </span>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
              <div>
                <label class="block text-[10px] font-bold text-[var(--text-muted)] uppercase mb-0.5" id="label-target-steps" data-i18n="labelTargetSteps">Standard Schritte-Ziel:</label>
                <input type="number" id="setting-steps-goal" min="1000" step="500" value="10000" onchange="updateGoalSettings()" class="shadcn-input text-xs py-1.5">
              </div>
              <div>
                <label class="block text-[10px] font-bold text-[var(--text-muted)] uppercase mb-0.5" id="label-target-water" data-i18n="labelTargetWater">Standard Wasser-Ziel (ml):</label>
                <input type="number" id="setting-water-goal" min="500" step="250" value="2500" onchange="updateGoalSettings()" class="shadcn-input text-xs py-1.5">
              </div>
            </div>

            <div class="pt-1 border-t border-[var(--border-subtle)] space-y-2">
              <label class="flex items-center justify-between gap-2 cursor-pointer">
                <span class="text-xs font-medium text-[var(--app-text)]" id="label-compact-mode" data-i18n="labelCompactMode">Karten beim Start standardmäßig zuklappen (Fokus-Modus)</span>
                <input type="checkbox" id="setting-compact-mode" onchange="updateGoalSettings()" class="w-4 h-4 rounded focus:ring-[var(--accent-primary)] cursor-pointer accent-[var(--accent-primary)]">
              </label>

              <div class="flex items-center justify-between gap-2 pt-1">
                <span class="text-xs font-medium text-[var(--app-text)]" id="label-start-view" data-i18n="labelStartView">Startansicht beim Öffnen:</span>
                <select id="setting-start-view" onchange="updateGoalSettings()" class="shadcn-input px-2 py-1 text-xs font-medium focus:outline-none">
                  <option value="diary" data-i18n="startViewDiary">Daily Diary & Tracker</option>
                  <option value="schema" data-i18n="startViewSchema">Schema-Memo</option>
                  <option value="last" data-i18n="startViewLast">Zuletzt geöffnet (Auto-Merken)</option>
                </select>
              </div>
            </div>
          </div>

          <!-- 4. DATEN, BACKUP & SICHERHEIT -->
          <div class="settings-group-panel p-3 rounded-xl space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-[var(--app-text)] flex items-center gap-1.5">
                <span id="label-setting-backup" data-i18n="labelSettingBackup">Gesamt-Backup & Datensicherung:</span>
              </span>
              <span id="settings-data-stats" class="text-[10px] text-[var(--text-muted)]">Berechne...</span>
            </div>
            <p class="text-[11px] text-[var(--text-muted)] leading-snug" id="settings-backup-desc" data-i18n="settingsBackupDesc">
              Erstelle ein Komplett-Backup aller Memos, Tagebuch-Tage und Einstellungen in einer einzigen sicheren Datei.
            </p>
            <div class="flex flex-wrap items-center gap-2 pt-1">
              <button type="button" onclick="exportFullBackupJSON()" class="btn-primary-theme px-3.5 py-1.5 rounded-xl font-semibold text-xs flex items-center justify-center gap-1.5 transition shadow-xs active:scale-[0.98]">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                <span id="btn-export-backup-text" data-i18n="btnExportBackup">Gesamt-Backup laden</span>
              </button>

              <label class="settings-backup-import-btn px-3.5 py-1.5 rounded-xl font-medium text-xs flex items-center justify-center gap-1.5 transition shadow-xs cursor-pointer active:scale-[0.98]">
                <svg class="w-3.5 h-3.5 text-[var(--text-muted)]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l4-4m0 0l4 4m-4-4v12"/></svg>
                <span id="btn-import-backup-text" data-i18n="btnImportBackup">Backup einspielen</span>
                <input type="file" id="full-backup-import-file" accept=".json" onchange="importFullBackupJSON(event)" class="hidden">
              </label>
            </div>
          </div>

        </div>

      </div>

      <!-- Modal Footer -->
      <div class="flex items-center justify-between px-4 py-3 border-t border-[var(--border-subtle)] bg-[var(--surface-subtle)] shrink-0">
        <span class="text-[10px] text-[var(--text-muted)] flex items-center gap-1">
          <span class="text-emerald-500 font-bold">●</span>
          <span id="settings-footer-privacy" data-i18n="privacyNote">100% lokal & privat auf diesem Gerät</span>
        </span>
        <button type="button" onclick="closeSettingsModal()" class="px-4 py-1.5 rounded-full btn-primary-theme text-xs font-medium transition shadow-xs">
          <span id="settings-btn-done" data-i18n="settingsDone">Fertig</span>
        </button>
      </div>

    </div>
  </div>
'''
