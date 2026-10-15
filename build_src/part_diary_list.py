# -*- coding: utf-8 -*-

def get_diary_list_view_html():
    return '''    <!-- VIEW B2: TAGEBUCH-CHRONIK (Journal & Ordnerstruktur) -->
    <div id="view-diary-list" class="hidden space-y-3 sm:space-y-4">

      <!-- Header & Folder Structure Filter -->
      <div class="shadcn-card p-3 sm:p-5 space-y-3">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5">
          <div>
            <h2 class="font-serif text-base sm:text-xl font-semibold tracking-tight text-stone-900 dark:text-stone-100" data-i18n="diaryListTitle">Mein Tagebuch & Lebens-Chronik</h2>
            <p class="font-serif italic text-xs text-stone-500 dark:text-stone-400 mt-0.5" data-i18n="diaryListSubtitle">Alle Einträge mit Medikation, Essen, Schlaf, Steps und ADHS-Fokus chronologisch.</p>
          </div>

          <div class="flex flex-wrap items-center gap-1.5">
            <button onclick="printDiaryJournal()" class="px-3 py-1.5 rounded-full bg-stone-900 hover:bg-stone-800 dark:bg-stone-100 dark:hover:bg-white text-stone-100 dark:text-stone-900 text-xs font-medium transition flex items-center gap-1.5 shadow-xs active:scale-[0.98]">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
              <span data-i18n="btnPrint">Drucken</span>
            </button>
            <button onclick="exportDiaryJSON()" class="px-3 py-1.5 rounded-full border border-stone-200 dark:border-stone-700 text-stone-700 dark:text-stone-300 text-xs font-medium hover:bg-stone-100 dark:hover:bg-stone-800 active:scale-[0.98] transition flex items-center gap-1 shadow-xs">
              <span data-i18n="btnBackup">Backup</span>
            </button>
            <label class="px-3 py-1.5 rounded-full border border-stone-200 dark:border-stone-700 text-stone-700 dark:text-stone-300 text-xs font-medium hover:bg-stone-100 dark:hover:bg-stone-800 active:scale-[0.98] transition flex items-center gap-1 cursor-pointer shadow-xs">
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
          <span class="text-[10px] font-medium uppercase tracking-wider text-stone-500 dark:text-stone-400" data-i18n="diaryFoldersTitle">Monats-Ordner:</span>
          <div class="flex flex-wrap items-center gap-1 pb-0.5" id="diary-folders-container">
            <!-- Dynamically populated month folders -->
          </div>
        </div>

        <!-- Quick Filter Tags -->
        <div class="flex flex-wrap items-center gap-1.5 pt-2 border-t border-stone-200/60 dark:border-stone-800">
          <span class="text-[10px] font-medium text-stone-500 dark:text-stone-400 uppercase tracking-wide mr-1" data-i18n="labelFilter">Filter:</span>
          <button type="button" onclick="setDiaryQuickFilter('all')" id="qf-all" class="qf-btn active text-xs px-3 py-1 rounded-full border border-stone-800 dark:border-stone-200 bg-stone-900 dark:bg-stone-100 text-stone-100 dark:text-stone-900 font-medium transition shadow-xs" data-i18n="qfAll">Alle Einträge</button>
          <button type="button" onclick="setDiaryQuickFilter('meds')" id="qf-meds" class="qf-btn text-xs px-3 py-1 rounded-full border border-stone-200 dark:border-stone-700 bg-stone-100/60 dark:bg-stone-800/60 text-stone-700 dark:text-stone-300 font-medium hover:bg-stone-200/60 dark:hover:bg-stone-700/60 transition" data-i18n="qfMeds">Medikation</button>
          <button type="button" onclick="setDiaryQuickFilter('food')" id="qf-food" class="qf-btn text-xs px-3 py-1 rounded-full border border-stone-200 dark:border-stone-700 bg-stone-100/60 dark:bg-stone-800/60 text-stone-700 dark:text-stone-300 font-medium hover:bg-stone-200/60 dark:hover:bg-stone-700/60 transition" data-i18n="qfFood">Mahlzeiten</button>
          <button type="button" onclick="setDiaryQuickFilter('steps')" id="qf-steps" class="qf-btn text-xs px-3 py-1 rounded-full border border-stone-200 dark:border-stone-700 bg-stone-100/60 dark:bg-stone-800/60 text-stone-700 dark:text-stone-300 font-medium hover:bg-stone-200/60 dark:hover:bg-stone-700/60 transition" data-i18n="qfSteps">&gt; 8k Schritte</button>
        </div>
      </div>

      <!-- Journal Feed Cards List -->
      <div id="diary-entries-container" class="space-y-3">
        <!-- Rendered via JavaScript -->
      </div>

    </div>
'''
