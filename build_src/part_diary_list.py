# -*- coding: utf-8 -*-

def get_diary_list_view_html():
    return '''    <!-- VIEW B2: TAGEBUCH-CHRONIK (Journal & Ordnerstruktur) -->
    <div id="view-diary-list" class="hidden space-y-3 sm:space-y-4">

      <!-- Header & Folder Structure Filter -->
      <div class="shadcn-card p-3 sm:p-5 space-y-3">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5">
          <div>
            <h2 class="text-base sm:text-xl font-bold tracking-tight text-slate-900 dark:text-white" data-i18n="diaryListTitle">Mein Tagebuch & Lebens-Chronik</h2>
            <p class="text-xs text-slate-500 dark:text-slate-400" data-i18n="diaryListSubtitle">Alle Einträge mit Medikation, Essen, Schlaf, Steps und ADHS-Fokus chronologisch.</p>
          </div>

          <div class="flex flex-wrap items-center gap-1.5">
            <button onclick="printDiaryJournal()" class="px-2.5 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-700 text-white text-xs font-bold transition flex items-center gap-1 shadow-xs">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
              <span data-i18n="btnPrint">Drucken</span>
            </button>
            <button onclick="exportDiaryJSON()" class="px-2.5 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-xs font-semibold hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1">
              <span data-i18n="btnBackup">Backup</span>
            </button>
            <label class="px-2.5 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-xs font-semibold hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1 cursor-pointer">
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
        <div class="space-y-1 pt-0.5">
          <span class="text-[10px] font-bold uppercase tracking-wider text-slate-500" data-i18n="diaryFoldersTitle">Monats-Ordner:</span>
          <div class="flex flex-wrap items-center gap-1 pb-0.5" id="diary-folders-container">
            <!-- Dynamically populated month folders -->
          </div>
        </div>

        <!-- Quick Filter Tags -->
        <div class="flex flex-wrap items-center gap-1 pt-1.5 border-t border-slate-100 dark:border-slate-800">
          <span class="text-[10px] font-bold text-slate-500 uppercase mr-1" data-i18n="labelFilter">Filter:</span>
          <button type="button" onclick="setDiaryQuickFilter('all')" id="qf-all" class="qf-btn active text-xs px-2.5 py-1 rounded-full border border-emerald-500 bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 font-bold transition" data-i18n="qfAll">Alle Einträge</button>
          <button type="button" onclick="setDiaryQuickFilter('meds')" id="qf-meds" class="qf-btn text-xs px-2.5 py-1 rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium transition" data-i18n="qfMeds">Medikation</button>
          <button type="button" onclick="setDiaryQuickFilter('food')" id="qf-food" class="qf-btn text-xs px-2.5 py-1 rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium transition" data-i18n="qfFood">Mahlzeiten</button>
          <button type="button" onclick="setDiaryQuickFilter('steps')" id="qf-steps" class="qf-btn text-xs px-2.5 py-1 rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium transition" data-i18n="qfSteps">&gt; 8k Schritte</button>
        </div>
      </div>

      <!-- Journal Feed Cards List -->
      <div id="diary-entries-container" class="space-y-3">
        <!-- Rendered via JavaScript -->
      </div>

    </div>
'''
