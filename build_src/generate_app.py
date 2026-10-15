# -*- coding: utf-8 -*-

def get_header():
    return '''  <!-- ======================================================== -->
  <!-- TOP APP HEADER WITH MODE SWITCHER                         -->
  <!-- ======================================================== -->
  <!-- ======================================================== -->
  <!-- TOP APP HEADER WITH MODE SWITCHER                         -->
  <!-- ======================================================== -->
  <header class="no-print sticky top-0 z-30 bg-[#FAF9F5]/90 dark:bg-[#121110]/90 backdrop-blur-md border-b border-stone-200/70 dark:border-stone-800/70 px-2.5 sm:px-6 py-1.5 sm:py-2">
    <div class="max-w-4xl mx-auto flex items-center justify-between gap-2">
      
      <!-- Brand Logo & Title -->
      <div class="flex items-center gap-2.5 min-w-0 cursor-pointer" onclick="handleBrandClick()">
        <div id="brand-logo-icon" class="w-7 h-7 sm:w-8 sm:h-8 rounded-xl bg-stone-900 dark:bg-stone-100 text-stone-100 dark:text-stone-900 flex items-center justify-center font-bold shadow-xs shrink-0 transition-all">
          <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
          </svg>
        </div>
        <div class="min-w-0">
          <h1 id="app-main-title" class="font-serif text-sm sm:text-base font-semibold tracking-tight text-stone-900 dark:text-stone-100 leading-tight truncate">Schema-Memo</h1>
          <p id="app-main-subtitle" class="font-serif italic text-[11px] text-stone-500 dark:text-stone-400 font-normal hidden sm:block truncate" data-i18n="brandSubtitle">Nach J. Young · Schematherapie</p>
        </div>
      </div>

      <!-- Header Quick Actions -->
      <div class="flex items-center gap-1 shrink-0">
        <!-- PWA Install Button -->
        <button id="btn-pwa-install" type="button" onclick="triggerPwaInstall()" class="hidden px-2.5 py-1 rounded-lg bg-[#4A7264] hover:bg-[#3D5F53] text-white text-[11px] font-medium transition flex items-center gap-1 shadow-xs" title="Als echte App installieren" data-i18n-title="pwaInstallTitle">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
          <span data-i18n="btnInstall">Installieren</span>
        </button>

        <!-- New Item Quick Button -->
        <button type="button" id="header-btn-new" onclick="handleHeaderNewClick()" class="px-2.5 py-1 rounded-lg bg-stone-200/60 dark:bg-stone-800/80 text-stone-800 dark:text-stone-200 hover:bg-stone-200 dark:hover:bg-stone-700 text-[11px] font-medium transition flex items-center gap-1 shadow-xs border border-stone-300/40 dark:border-stone-700/50" title="Neu anlegen" data-i18n-title="headerNewTooltip">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
          <span id="header-btn-new-text">Neu</span>
        </button>

        <!-- Settings Button -->
        <button type="button" id="header-btn-settings" onclick="openSettingsModal()" class="p-1.5 rounded-lg text-stone-500 hover:text-stone-800 dark:hover:text-stone-200 hover:bg-stone-200/50 dark:hover:bg-stone-800/50 transition" title="Einstellungen" data-i18n-title="settingsTooltip">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
        </button>

        <!-- Quick Update / Cache Clear Button -->
        <button type="button" onclick="forceAppUpdate()" class="p-1.5 rounded-lg text-stone-500 hover:text-stone-800 dark:hover:text-stone-200 hover:bg-stone-200/50 dark:hover:bg-stone-800/50 transition" title="App aktualisieren & Cache leeren" data-i18n-title="forceUpdateTooltip">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
        </button>

        <!-- Dark Mode Toggle -->
        <button id="theme-toggle-btn" onclick="toggleTheme()" class="p-1.5 rounded-lg text-stone-500 hover:text-stone-800 dark:hover:text-stone-200 hover:bg-stone-200/50 dark:hover:bg-stone-800/50 transition" title="Design umschalten" data-i18n-title="themeToggleTooltip">
          <svg id="theme-icon-sun" class="w-4 h-4 hidden text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
          <svg id="theme-icon-moon" class="w-4 h-4 text-stone-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        </button>
      </div>

    </div>

    <!-- PRIMARY MODULE SWITCHER: Schema-Memo vs. Daily Life & Neuro-Tracker Diary -->
    <div class="max-w-4xl mx-auto pt-1 sm:pt-1.5 flex items-center justify-center">
      <div class="inline-flex p-1 rounded-full bg-stone-200/50 dark:bg-stone-800/60 border border-stone-300/40 dark:border-stone-700/50 w-full max-w-xs shadow-inner">
        <button id="mode-btn-schema" type="button" onclick="switchAppMode('schema')" class="flex-1 py-1 px-3 rounded-full text-xs font-semibold transition-all flex items-center justify-center gap-1.5 shadow-xs bg-white dark:bg-stone-900 text-stone-900 dark:text-stone-100">
          <span data-i18n="navSchema">Schema-Memo</span>
        </button>
        <button id="mode-btn-diary" type="button" onclick="switchAppMode('diary')" class="flex-1 py-1 px-3 rounded-full text-xs font-medium transition-all flex items-center justify-center gap-1.5 text-stone-500 dark:text-stone-400 hover:text-stone-900 dark:hover:text-stone-100">
          <span data-i18n="navDiary">Diary & Tracker</span>
        </button>
      </div>
    </div>
  </header>

  <!-- ======================================================== -->
  <!-- MAIN APP CONTAINER                                        -->
  <!-- ======================================================== -->
  <main class="max-w-4xl w-full mx-auto px-2 sm:px-6 pt-3 sm:pt-5 pb-24 sm:pb-32">
'''
