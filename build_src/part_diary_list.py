# -*- coding: utf-8 -*-

def get_diary_list_view_html():
    return '''    <!-- VIEW B2: TAGEBUCH-CHRONIK (Journal & Ordnerstruktur) -->
    <div id="view-diary-list" class="hidden space-y-3 sm:space-y-4">

      <!-- Header & Folder Structure Filter -->
      <div class="shadcn-card p-3 sm:p-5 space-y-3">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5">
          <div>
            <h2 class="font-serif text-base sm:text-xl font-semibold tracking-tight text-[var(--app-text)]" data-i18n="diaryListTitle">Mein Tagebuch & Lebens-Chronik</h2>
            <p class="font-serif italic text-xs text-[var(--text-muted)] mt-0.5" data-i18n="diaryListSubtitle">Alle Einträge mit Medikation, Essen, Schlaf, Steps und ADHS-Fokus chronologisch.</p>
          </div>

          <div class="flex flex-wrap items-center gap-1.5">
            <button type="button" onclick="printDiaryJournal()" class="px-2.5 py-1.5 rounded-xl border border-[var(--border-subtle)] bg-[var(--surface-subtle)] hover:bg-[var(--surface-subtle-hover)] text-[var(--app-text)] text-xs font-medium transition flex items-center gap-1.5 shadow-2xs active:scale-[0.98]">
              <svg class="w-3.5 h-3.5 text-[var(--text-muted)]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
              <span data-i18n="btnPrint">Drucken</span>
            </button>
            <button type="button" onclick="exportDiaryJSON()" class="px-2.5 py-1.5 rounded-xl border border-[var(--border-subtle)] bg-[var(--surface-subtle)] hover:bg-[var(--surface-subtle-hover)] text-[var(--app-text)] text-xs font-medium active:scale-[0.98] transition flex items-center gap-1.5 shadow-2xs">
              <svg class="w-3.5 h-3.5 text-[var(--text-muted)]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
              <span data-i18n="btnBackup">Backup</span>
            </button>
            <label class="px-2.5 py-1.5 rounded-xl border border-[var(--border-subtle)] bg-[var(--surface-subtle)] hover:bg-[var(--surface-subtle-hover)] text-[var(--app-text)] text-xs font-medium active:scale-[0.98] transition flex items-center gap-1.5 cursor-pointer shadow-2xs">
              <svg class="w-3.5 h-3.5 text-[var(--text-muted)]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l4-4m0 0l4 4m-4-4v12"/></svg>
              <span data-i18n="btnImport">Import</span>
              <input type="file" id="import-diary-file" accept=".json" onchange="importDiaryJSON(event)" class="hidden">
            </label>
          </div>
        </div>

        <!-- Search Input -->
        <div class="pt-0.5">
          <input type="text" id="diary-search-input" oninput="renderDiaryEntriesList()" placeholder="Tagebuch durchsuchen (Medis, Essen, Emotionen, Tags)..." data-i18n-placeholder="diarySearchPlaceholder" class="shadcn-input text-xs">
        </div>

        <!-- Filter Folders / Months -->
        <div class="space-y-1.5 pt-1">
          <span class="text-[10px] font-medium uppercase tracking-wider text-[var(--text-muted)]" data-i18n="diaryFoldersTitle">Monats-Ordner:</span>
          <div class="flex flex-wrap items-center gap-1 pb-0.5" id="diary-folders-container">
            <!-- Dynamically populated month folders -->
          </div>
        </div>

        <!-- Quick Filter Tags -->
        <div class="flex flex-wrap items-center gap-1.5 pt-2 border-t border-[var(--border-subtle)]">
          <span class="text-[10px] font-medium text-[var(--text-muted)] uppercase tracking-wide mr-1" data-i18n="labelFilter">Filter:</span>
          <button type="button" onclick="setDiaryQuickFilter('all')" id="qf-all" class="qf-btn active text-xs px-3 py-1 rounded-full font-medium transition shadow-xs" data-i18n="qfAll">Alle Einträge</button>
          <button type="button" onclick="setDiaryQuickFilter('meds')" id="qf-meds" class="qf-btn text-xs px-3 py-1 rounded-full font-medium transition" data-i18n="qfMeds">Medikation</button>
          <button type="button" onclick="setDiaryQuickFilter('food')" id="qf-food" class="qf-btn text-xs px-3 py-1 rounded-full font-medium transition" data-i18n="qfFood">Mahlzeiten</button>
          <button type="button" onclick="setDiaryQuickFilter('steps')" id="qf-steps" class="qf-btn text-xs px-3 py-1 rounded-full font-medium transition" data-i18n="qfSteps">&gt; 8k Schritte</button>
        </div>
      </div>

      <!-- Journal Feed Cards List -->
      <div id="diary-entries-container" class="space-y-3">
        <!-- Rendered via JavaScript -->
      </div>

    </div>
'''
