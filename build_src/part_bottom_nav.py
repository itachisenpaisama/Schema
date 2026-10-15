# -*- coding: utf-8 -*-

def get_bottom_nav_and_toast():
    return '''  </main>

  <!-- ======================================================== -->
  <!-- NATIVE BOTTOM NAVIGATION BAR (DYNAMIC)                   -->
  <!-- ======================================================== -->
  <!-- ======================================================== -->
  <!-- NATIVE BOTTOM NAVIGATION BAR (DYNAMIC)                   -->
  <!-- ======================================================== -->
  <nav id="app-bottom-nav" class="no-print fixed bottom-0 left-0 right-0 z-40 bg-[#FAF9F5]/90 dark:bg-[#121110]/90 backdrop-blur-md border-t border-stone-200/80 dark:border-stone-800/80 flex items-center justify-around px-2 py-1.5 shadow-xs">
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
    <div class="shadcn-card w-full max-w-sm p-4 space-y-3 shadow-2xl border border-stone-200/80 dark:border-stone-800 bg-white dark:bg-[#181715] text-stone-900 dark:text-stone-100 rounded-2xl animate-in fade-in zoom-in-95">
      
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
        <button type="button" onclick="closeCustomOptionModal()" class="px-3 py-1.5 rounded-lg border border-stone-200 dark:border-stone-700 text-stone-600 dark:text-stone-300 text-xs font-semibold hover:bg-stone-100 dark:hover:bg-stone-800 transition">
          <span data-i18n="btnCancel">Abbrechen</span>
        </button>
        <button type="button" onclick="saveCustomOptionFromModal()" class="px-4 py-1.5 rounded-lg bg-[#4A7264] hover:bg-[#3D5F53] text-white text-xs font-semibold transition shadow-xs">
          <span data-i18n="btnSavePermanent">Dauerhaft speichern</span>
        </button>
      </div>

    </div>
  </div>

  <!-- ======================================================== -->
  <!-- MODAL: APP-EINSTELLUNGEN & MODUL-MANAGER (SETTINGS)       -->
  <!-- ======================================================== -->
  <div id="settings-modal" class="no-print hidden fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-stone-950/40 backdrop-blur-xs transition-opacity duration-200">
    <div class="shadcn-card w-full max-w-lg max-h-[92vh] flex flex-col shadow-2xl border border-stone-200/80 dark:border-stone-800 bg-white dark:bg-[#181715] text-stone-900 dark:text-stone-100 rounded-2xl animate-in fade-in zoom-in-95 overflow-hidden">
      
      <!-- Modal Header -->
      <div class="flex items-center justify-between px-4 py-3 border-b border-stone-100 dark:border-stone-800 shrink-0">
        <div class="flex items-center gap-2.5 min-w-0">
          <div class="w-8 h-8 rounded-lg bg-stone-100 dark:bg-stone-800 flex items-center justify-center text-stone-600 dark:text-stone-300 shrink-0">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          </div>
          <div class="min-w-0">
            <h3 id="settings-modal-heading" data-i18n="settingsHeading" class="font-serif text-sm sm:text-base font-semibold text-stone-900 dark:text-stone-100 leading-tight truncate">Einstellungen & Module</h3>
            <p id="settings-modal-subheading" data-i18n="settingsSubheading" class="text-[11px] text-stone-500 dark:text-stone-400 truncate">Passe Module, Sprache und Darstellung an deine Bedürfnisse an.</p>
          </div>
        </div>
        <button type="button" onclick="closeSettingsModal()" class="p-1 rounded-lg text-stone-400 hover:text-stone-600 dark:hover:text-stone-200 transition shrink-0" aria-label="Schließen" data-i18n-title="btnClose">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>

      <!-- Segmented Tab Navigation inside Modal -->
      <div class="px-4 pt-2.5 pb-1 border-b border-stone-100 dark:border-stone-800 bg-stone-50/50 dark:bg-stone-900/50 shrink-0">
        <div class="grid grid-cols-2 p-1 rounded-xl bg-stone-200/70 dark:bg-stone-800 border border-stone-300/60 dark:border-stone-700 text-xs font-semibold shadow-inner">
          <button type="button" id="tab-btn-modules" onclick="switchSettingsTab('modules')" class="py-1.5 px-3 rounded-lg transition text-center shadow-xs bg-white dark:bg-stone-900 text-[#4A7264] dark:text-[#7BA896] font-semibold">
            <span id="tab-label-modules" data-i18n="tabLabelModules">Tracking-Module</span>
          </button>
          <button type="button" id="tab-btn-general" onclick="switchSettingsTab('general')" class="py-1.5 px-3 rounded-lg transition text-center text-stone-600 dark:text-stone-400 hover:text-stone-900 dark:hover:text-white font-medium">
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
          <div class="p-3 rounded-xl bg-stone-100/70 dark:bg-stone-900/40 border border-stone-200/80 dark:border-stone-800 space-y-2">
            <div class="flex items-center justify-between gap-2">
              <span class="text-xs font-semibold text-stone-900 dark:text-stone-100 flex items-center gap-1.5">
                <span id="settings-presets-title" data-i18n="settingsPresetsTitle">Schnell-Vorlagen:</span>
              </span>
              <span class="text-[10px] text-[#4A7264] dark:text-[#7BA896] font-bold" id="settings-active-count-badge">13 aktiv</span>
            </div>
            <p class="text-[11px] text-stone-600 dark:text-stone-400 leading-snug" id="settings-presets-desc" data-i18n="settingsPresetsDesc">
              Passe das Tagebuch so an, dass du dich nicht überfordert fühlst. Schalte nur die Bereiche ein, die du heute wirklich tracken möchtest.
            </p>
            <div class="flex flex-wrap gap-1.5 pt-0.5">
              <button type="button" onclick="setFeaturePreset('all')" class="text-xs px-2.5 py-1 rounded-lg bg-[#4A7264] hover:bg-[#3D5F53] text-white font-semibold transition shadow-xs" data-i18n="presetAll">
                Alle an
              </button>
              <button type="button" onclick="setFeaturePreset('minimal')" class="text-xs px-2.5 py-1 rounded-lg bg-white dark:bg-stone-800 border border-stone-300 dark:border-stone-600 text-stone-700 dark:text-stone-200 hover:bg-stone-100 font-medium transition shadow-xs" data-i18n="presetMinimal">
                Nur Kern (Minimal)
              </button>
              <button type="button" onclick="setFeaturePreset('mindfulness')" class="text-xs px-2.5 py-1 rounded-lg bg-white dark:bg-stone-800 border border-stone-300 dark:border-stone-600 text-stone-700 dark:text-stone-200 hover:bg-stone-100 font-medium transition shadow-xs" data-i18n="presetMindfulness">
                Achtsamkeit
              </button>
            </div>
          </div>

          <!-- Feature Toggles List Container (Dynamically populated & synced) -->
          <div id="settings-feature-toggles-container" class="space-y-2">
            <!-- Dynamically injected feature rows with iOS-style toggles -->
          </div>

        </div>

        <!-- ============================================== -->
        <!-- TAB 2: ALLGEMEIN, SPRACHE, THEME & BACKUP     -->
        <!-- ============================================== -->
        <div id="settings-tab-general" class="hidden space-y-4">
          
          <!-- 1. SPRACHE / LANGUAGE -->
          <div class="p-3 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/40 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
                <span id="label-setting-language" data-i18n="labelSettingLanguage">Sprache / Language:</span>
              </span>
              <span id="current-lang-badge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300">Deutsch</span>
            </div>
            <div class="grid grid-cols-2 gap-2 pt-0.5">
              <button type="button" onclick="setAppLanguage('de')" id="lang-btn-de" class="py-2 px-3 rounded-xl border border-sky-500 bg-sky-50 dark:bg-sky-950/60 text-sky-800 dark:text-sky-300 font-bold text-xs flex items-center justify-center gap-1.5 transition">
                <span>Deutsch (DE)</span>
              </button>
              <button type="button" onclick="setAppLanguage('en')" id="lang-btn-en" class="py-2 px-3 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:text-slate-900 font-semibold text-xs flex items-center justify-center gap-1.5 transition">
                <span>English (EN)</span>
              </button>
            </div>
          </div>

          <!-- 2. ERSCHEINUNGSBILD / THEME -->
          <div class="p-3 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/40 space-y-2">
            <span class="text-xs font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
              <span id="label-setting-theme" data-i18n="labelSettingTheme">Erscheinungsbild:</span>
            </span>
            <div class="grid grid-cols-3 gap-1.5 pt-0.5">
              <button type="button" onclick="setAppThemeSetting('light')" id="theme-opt-light" class="theme-choice-btn py-2 px-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs font-semibold text-center transition flex flex-col items-center gap-1">
                <svg class="w-4 h-4 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
                <span class="text-[11px]" data-i18n="themeLight">Hell</span>
              </button>
              <button type="button" onclick="setAppThemeSetting('dark')" id="theme-opt-dark" class="theme-choice-btn py-2 px-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs font-semibold text-center transition flex flex-col items-center gap-1">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
                <span class="text-[11px]" data-i18n="themeDark">Dunkel</span>
              </button>
              <button type="button" onclick="setAppThemeSetting('auto')" id="theme-opt-auto" class="theme-choice-btn py-2 px-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white text-center transition flex flex-col items-center gap-1">
                <svg class="w-4 h-4 text-slate-500 dark:text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                <span class="text-[11px]" data-i18n="themeAuto">System</span>
              </button>
            </div>
          </div>

          <!-- 2.5 FARBPROFILE (Hintergrund & Text) -->
          <div class="p-3 rounded-2xl border border-stone-200/80 dark:border-stone-800 bg-[#FAF9F5]/60 dark:bg-[#1E1C1A]/40 space-y-2.5">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-stone-800 dark:text-stone-200 flex items-center gap-1.5">
                <span id="label-setting-color-profile" data-i18n="labelSettingColorProfile">Farbprofil (Hintergrund & Text):</span>
              </span>
              <span id="current-profile-badge" class="text-[10px] font-medium px-2 py-0.5 rounded-full bg-stone-200 dark:bg-stone-700 text-stone-700 dark:text-stone-300">Stoic</span>
            </div>
            <p class="text-[11px] text-stone-500 dark:text-stone-400 leading-snug" data-i18n="colorProfileDesc">
              Wähle aus verschiedenen beruhigenden Farbprofilen für Hintergrund, Karten, Text und Nuancen.
            </p>
            <div class="grid grid-cols-2 sm:grid-cols-2 lg:grid-cols-3 gap-2 pt-1" id="color-profiles-container">
              <!-- Dynamically populated via renderColorProfilesUI() -->
            </div>
          </div>

          <!-- 3. TAGESZIELE & START-ANSICHT -->
          <div class="p-3 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/40 space-y-2.5">
            <span class="text-xs font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
              <span id="label-setting-targets" data-i18n="labelSettingTargets">Tagesziele & Verhalten:</span>
            </span>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
              <div>
                <label class="block text-[10px] font-bold text-slate-500 uppercase mb-0.5" id="label-target-steps" data-i18n="labelTargetSteps">Standard Schritte-Ziel:</label>
                <input type="number" id="setting-steps-goal" min="1000" step="500" value="10000" onchange="updateGoalSettings()" class="shadcn-input text-xs py-1.5">
              </div>
              <div>
                <label class="block text-[10px] font-bold text-slate-500 uppercase mb-0.5" id="label-target-water" data-i18n="labelTargetWater">Standard Wasser-Ziel (ml):</label>
                <input type="number" id="setting-water-goal" min="500" step="250" value="2500" onchange="updateGoalSettings()" class="shadcn-input text-xs py-1.5">
              </div>
            </div>

            <div class="pt-1 border-t border-slate-200/60 dark:border-slate-800 space-y-2">
              <label class="flex items-center justify-between gap-2 cursor-pointer">
                <span class="text-xs font-medium text-slate-700 dark:text-slate-300" id="label-compact-mode" data-i18n="labelCompactMode">Karten beim Start standardmäßig zuklappen (Fokus-Modus)</span>
                <input type="checkbox" id="setting-compact-mode" onchange="updateGoalSettings()" class="w-4 h-4 rounded text-sky-600 focus:ring-sky-500 cursor-pointer accent-sky-600">
              </label>

              <div class="flex items-center justify-between gap-2 pt-1">
                <span class="text-xs font-medium text-slate-700 dark:text-slate-300" id="label-start-view" data-i18n="labelStartView">Startansicht beim Öffnen:</span>
                <select id="setting-start-view" onchange="updateGoalSettings()" class="bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-lg px-2 py-1 text-xs text-slate-700 dark:text-slate-200 font-medium focus:outline-none">
                  <option value="diary" data-i18n="startViewDiary">Daily Diary & Tracker</option>
                  <option value="schema" data-i18n="startViewSchema">Schema-Memo</option>
                  <option value="last" data-i18n="startViewLast">Zuletzt geöffnet (Auto-Merken)</option>
                </select>
              </div>
            </div>
          </div>

          <!-- 4. DATEN, BACKUP & SICHERHEIT -->
          <div class="p-3 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/40 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
                <span id="label-setting-backup" data-i18n="labelSettingBackup">Gesamt-Backup & Datensicherung:</span>
              </span>
              <span id="settings-data-stats" class="text-[10px] text-slate-400">Berechne...</span>
            </div>
            <p class="text-[11px] text-slate-500 leading-snug" id="settings-backup-desc" data-i18n="settingsBackupDesc">
              Erstelle ein Komplett-Backup aller Memos, Tagebuch-Tage und Einstellungen in einer einzigen sicheren Datei.
            </p>
            <div class="flex flex-wrap gap-2 pt-1">
              <button type="button" onclick="exportFullBackupJSON()" class="flex-1 min-w-[140px] py-2 px-3 rounded-xl bg-slate-900 hover:bg-black text-white dark:bg-white dark:text-slate-900 dark:hover:bg-slate-100 font-bold text-xs flex items-center justify-center gap-1.5 transition shadow-xs">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                <span id="btn-export-backup-text" data-i18n="btnExportBackup">Gesamt-Backup laden</span>
              </button>

              <label class="flex-1 min-w-[140px] py-2 px-3 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 font-semibold text-xs flex items-center justify-center gap-1.5 transition shadow-xs cursor-pointer">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l4-4m0 0l4 4m-4-4v12"/></svg>
                <span id="btn-import-backup-text" data-i18n="btnImportBackup">Backup einspielen</span>
                <input type="file" id="full-backup-import-file" accept=".json" onchange="importFullBackupJSON(event)" class="hidden">
              </label>
            </div>
          </div>

        </div>

      </div>

      <!-- Modal Footer -->
      <div class="flex items-center justify-between px-4 py-3 border-t border-slate-100 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-900/70 shrink-0">
        <span class="text-[10px] text-slate-400 flex items-center gap-1">
          <span class="text-emerald-500 font-bold">●</span>
          <span id="settings-footer-privacy" data-i18n="privacyNote">100% lokal & privat auf diesem Gerät</span>
        </span>
        <button type="button" onclick="closeSettingsModal()" class="px-4 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-700 text-white text-xs font-bold transition shadow-xs">
          <span id="settings-btn-done" data-i18n="settingsDone">Fertig</span>
        </button>
      </div>

    </div>
  </div>
'''
