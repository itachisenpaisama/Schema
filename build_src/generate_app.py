# -*- coding: utf-8 -*-

def get_header():
    return '''  <!-- ======================================================== -->
  <!-- TOP APP HEADER WITH MODE SWITCHER                         -->
  <!-- ======================================================== -->
  <header class="no-print sticky top-0 z-30 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 px-2.5 sm:px-6 py-1.5 sm:py-2">
    <div class="max-w-4xl mx-auto flex items-center justify-between gap-2">
      
      <!-- Brand Logo & Title -->
      <div class="flex items-center gap-2 min-w-0 cursor-pointer" onclick="handleBrandClick()">
        <div id="brand-logo-icon" class="w-7 h-7 sm:w-8 sm:h-8 rounded-xl bg-gradient-to-tr from-sky-600 to-indigo-600 text-white flex items-center justify-center font-bold shadow-xs shrink-0">
          <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
          </svg>
        </div>
        <div class="min-w-0">
          <h1 id="app-main-title" class="text-xs sm:text-base font-bold tracking-tight text-slate-900 dark:text-white leading-tight truncate">Schema-Memo</h1>
          <p id="app-main-subtitle" class="text-[10px] text-slate-500 dark:text-slate-400 font-medium hidden sm:block truncate">Nach J. Young · Schematherapie</p>
        </div>
      </div>

      <!-- Header Quick Actions -->
      <div class="flex items-center gap-1 shrink-0">
        <!-- PWA Install Button -->
        <button id="btn-pwa-install" type="button" onclick="triggerPwaInstall()" class="hidden px-2 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white text-[11px] font-bold transition flex items-center gap-1 shadow-xs" title="Als echte App installieren">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
          <span>Installieren</span>
        </button>

        <!-- New Item Quick Button (Single clean plus icon) -->
        <button type="button" id="header-btn-new" onclick="handleHeaderNewClick()" class="px-2 py-1 rounded-lg bg-sky-50 dark:bg-sky-950/60 text-sky-700 dark:text-sky-300 hover:bg-sky-100 text-[11px] font-semibold transition flex items-center gap-1 shadow-xs" title="Neu anlegen">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
          <span id="header-btn-new-text">Neu</span>
        </button>

        <!-- Settings Button -->
        <button type="button" id="header-btn-settings" onclick="openSettingsModal()" class="p-1.5 rounded-lg text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800 transition" title="Einstellungen">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
        </button>

        <!-- Quick Update / Cache Clear Button -->
        <button type="button" onclick="forceAppUpdate()" class="p-1.5 rounded-lg text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800 transition" title="App aktualisieren & Cache leeren">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
        </button>

        <!-- Dark Mode Toggle -->
        <button id="theme-toggle-btn" onclick="toggleTheme()" class="p-1.5 rounded-lg text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800 transition" title="Design umschalten">
          <svg id="theme-icon-sun" class="w-4 h-4 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
          <svg id="theme-icon-moon" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        </button>
      </div>

    </div>

    <!-- PRIMARY MODULE SWITCHER: Schema-Memo vs. Daily Life & Neuro-Tracker Diary -->
    <div class="max-w-4xl mx-auto pt-1 sm:pt-1.5 flex items-center justify-center">
      <div class="inline-flex p-1 rounded-xl bg-slate-100 dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700 w-full max-w-xs shadow-inner">
        <button id="mode-btn-schema" type="button" onclick="switchAppMode('schema')" class="flex-1 py-1 px-2.5 rounded-lg text-xs font-bold transition flex items-center justify-center gap-1.5 shadow-xs bg-white dark:bg-slate-900 text-sky-700 dark:text-sky-300">
          <span>Schema-Memo</span>
        </button>
        <button id="mode-btn-diary" type="button" onclick="switchAppMode('diary')" class="flex-1 py-1 px-2.5 rounded-lg text-xs font-semibold transition flex items-center justify-center gap-1.5 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white">
          <span>Diary & Tracker</span>
        </button>
      </div>
    </div>
  </header>

  <!-- ======================================================== -->
  <!-- MAIN APP CONTAINER                                        -->
  <!-- ======================================================== -->
  <main class="max-w-4xl w-full mx-auto px-2 sm:px-6 pt-3 sm:pt-5 pb-24 sm:pb-32">
'''
