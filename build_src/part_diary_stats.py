# -*- coding: utf-8 -*-

def get_diary_stats_view_html():
    return '''    <!-- VIEW B3: TAGEBUCH-STATISTIKEN & NEURO-TRENDS -->
    <div id="view-diary-stats" class="hidden space-y-3 sm:space-y-4">

      <!-- Stats Header & Timeframe Selector -->
      <div class="shadcn-card p-3 sm:p-5 space-y-3">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5">
          <div>
            <h2 class="text-base sm:text-xl font-bold tracking-tight text-slate-900 dark:text-white" data-i18n="statsTitle">Statistiken, Trends & Neuro-Insights</h2>
            <p class="text-xs text-slate-500 dark:text-slate-400" data-i18n="statsSubtitle">Verstehe Zusammenhänge zwischen Medikation, Schlaf, Essen, Bewegung und mentalem Fokus.</p>
          </div>

          <button onclick="printStatsSummary()" class="px-2.5 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-xs font-semibold hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1 self-start sm:self-auto">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
            <span data-i18n="btnPrint">Drucken</span>
          </button>
        </div>

        <!-- Time Range Selector -->
        <div class="inline-flex p-1 rounded-xl bg-slate-100 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 w-full flex-wrap gap-1">
          <button type="button" onclick="setStatsTimeframe(7)" class="stats-time-btn flex-1 sm:flex-initial px-2.5 py-1 sm:py-1.5 rounded-lg text-xs font-bold transition active bg-white dark:bg-slate-900 text-sky-700 dark:text-sky-300 shadow-xs" data-days="7" data-i18n="statsDays7">7 Tage</button>
          <button type="button" onclick="setStatsTimeframe(14)" class="stats-time-btn flex-1 sm:flex-initial px-2.5 py-1 sm:py-1.5 rounded-lg text-xs font-medium text-slate-600 dark:text-slate-400 transition" data-days="14" data-i18n="statsDays14">14 Tage</button>
          <button type="button" onclick="setStatsTimeframe(30)" class="stats-time-btn flex-1 sm:flex-initial px-2.5 py-1 sm:py-1.5 rounded-lg text-xs font-medium text-slate-600 dark:text-slate-400 transition" data-days="30" data-i18n="statsDays30">30 Tage</button>
          <button type="button" onclick="setStatsTimeframe(90)" class="stats-time-btn flex-1 sm:flex-initial px-2.5 py-1 sm:py-1.5 rounded-lg text-xs font-medium text-slate-600 dark:text-slate-400 transition" data-days="90" data-i18n="statsDays90">90 Tage</button>
          <button type="button" onclick="setStatsTimeframe('month')" class="stats-time-btn flex-1 sm:flex-initial px-2.5 py-1 sm:py-1.5 rounded-lg text-xs font-medium text-slate-600 dark:text-slate-400 transition" data-days="month" data-i18n="statsDaysMonth">Monat</button>
          <button type="button" onclick="setStatsTimeframe('all')" class="stats-time-btn flex-1 sm:flex-initial px-2.5 py-1 sm:py-1.5 rounded-lg text-xs font-medium text-slate-600 dark:text-slate-400 transition" data-days="all" data-i18n="statsDaysAll">Alle</button>
        </div>
      </div>

      <!-- 6 METRIC KPI CARDS GRID -->
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2">
        
        <!-- 1. Mood -->
        <div class="shadcn-card p-2.5 sm:p-3 space-y-0.5">
          <span class="text-slate-500 text-[10px] font-bold uppercase tracking-wider" data-i18n="statsKpiMood">Ø Stimmung</span>
          <div id="stats-kpi-avg" class="text-lg sm:text-2xl font-black text-emerald-600 dark:text-emerald-400">--</div>
          <div id="stats-kpi-trend" class="text-[10px] text-slate-400 truncate">Trend...</div>
        </div>

        <!-- 2. Sleep -->
        <div class="shadcn-card p-2.5 sm:p-3 space-y-0.5">
          <span class="text-slate-500 text-[10px] font-bold uppercase tracking-wider" data-i18n="statsKpiSleep">Ø Schlaf</span>
          <div id="stats-kpi-sleep" class="text-lg sm:text-2xl font-black text-indigo-600 dark:text-indigo-400">--</div>
          <div id="stats-kpi-sleep-qual" class="text-[10px] text-slate-400 truncate">-- Qualität</div>
        </div>

        <!-- 3. Steps -->
        <div class="shadcn-card p-2.5 sm:p-3 space-y-0.5">
          <span class="text-slate-500 text-[10px] font-bold uppercase tracking-wider" data-i18n="statsKpiSteps">Ø Schritte</span>
          <div id="stats-kpi-steps" class="text-lg sm:text-2xl font-black text-blue-600 dark:text-blue-400">--</div>
          <div id="stats-kpi-steps-total" class="text-[10px] text-slate-400 truncate">0 gesamt</div>
        </div>

        <!-- 4. Med Adherence -->
        <div class="shadcn-card p-2.5 sm:p-3 space-y-0.5">
          <span class="text-slate-500 text-[10px] font-bold uppercase tracking-wider" data-i18n="statsKpiMeds">Med-Treue</span>
          <div id="stats-kpi-meds" class="text-lg sm:text-2xl font-black text-violet-600 dark:text-violet-400">--</div>
          <div class="text-[10px] text-slate-400" data-i18n="statsKpiMedsDesc">Tage mit Medis</div>
        </div>

        <!-- 5. ADHD Focus -->
        <div class="shadcn-card p-2.5 sm:p-3 space-y-0.5">
          <span class="text-slate-500 text-[10px] font-bold uppercase tracking-wider" data-i18n="statsKpiFocus">Ø ADHS-Fokus</span>
          <div id="stats-kpi-focus" class="text-lg sm:text-2xl font-black text-violet-600 dark:text-violet-400">--</div>
          <div class="text-[10px] text-slate-400" data-i18n="statsKpiFocusDesc">Fokus (1-10)</div>
        </div>

        <!-- 6. Streak -->
        <div class="shadcn-card p-2.5 sm:p-3 space-y-0.5">
          <span class="text-slate-500 text-[10px] font-bold uppercase tracking-wider" data-i18n="statsKpiStreak">Aktive Serie</span>
          <div id="stats-kpi-streak" class="text-lg sm:text-2xl font-black text-amber-500">0 d</div>
          <div class="text-[10px] text-slate-400" data-i18n="statsKpiStreakDesc">Tage in Folge</div>
        </div>

      </div>

      <!-- INTERACTIVE DUAL-LINE TIMELINE CHART (MOOD & FOCUS) -->
      <section class="shadcn-card p-3 sm:p-5 space-y-2.5">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5">
          <div>
            <h3 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2" data-i18n="statsChartTitle">
              Stimmung & ADHS-Fokus im Verlauf
            </h3>
            <p class="text-[11px] text-slate-500" data-i18n="statsChartSubtitle">Vergleiche deine Stimmungskurve direkt mit deinem Konzentrationslevel</p>
          </div>
          <div class="flex items-center gap-3 text-xs font-semibold">
            <span class="flex items-center gap-1 text-emerald-600 dark:text-emerald-400">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span> <span data-i18n="statsLegendMood">Stimmung</span>
            </span>
            <span class="flex items-center gap-1 text-violet-600 dark:text-violet-400">
              <span class="w-2.5 h-2.5 rounded-full bg-violet-500"></span> <span data-i18n="statsLegendFocus">ADHS-Fokus</span>
            </span>
          </div>
        </div>

        <!-- Chart container: 100% width, no horizontal scroll, auto-responsive SVG -->
        <div class="w-full pb-1 overflow-hidden" id="stats-chart-wrapper">
          <div id="stats-chart-container" class="w-full h-[180px] sm:h-[210px] flex items-center justify-center">
            <!-- Rendered via SVG -->
          </div>
        </div>
      </section>

      <!-- NEURO-INSIGHT CORRELATION CARD -->
      <section class="p-3 sm:p-4 rounded-2xl bg-gradient-to-tr from-violet-500/10 to-indigo-500/10 border border-violet-200 dark:border-violet-800/60 space-y-1.5">
        <div class="flex items-center gap-2">
          <svg class="w-4 h-4 text-violet-600 dark:text-violet-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>
          <h4 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-white" data-i18n="statsInsightTitle">Neuro-Insight & Lebensstil-Muster</h4>
        </div>
        <p id="stats-insight-text" class="text-xs text-slate-700 dark:text-slate-300 leading-relaxed">
          Erfasse regelmäßig deine Einträge, damit die App automatisch Muster zwischen Schlafdauer, Medikation, Bewegung und deinem Fokus erkennt.
        </p>
      </section>

      <!-- TWO COLUMNS: DAY OF WEEK TENDENCY & TOP EMOTIONS -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 sm:gap-3">
        
        <!-- Day of Week Analysis (Mo - So) -->
        <div class="shadcn-card p-3 sm:p-4 space-y-2">
          <div class="flex items-center justify-between">
            <h4 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-white" data-i18n="statsWeekdayTitle">
              Tendenzen nach Wochentag
            </h4>
          </div>
          <p class="text-[11px] text-slate-500" data-i18n="statsWeekdaySubtitle">An welchen Wochentagen geht es dir im Schnitt am besten?</p>
          <div id="stats-weekday-bars" class="space-y-1.5 pt-1">
            <!-- Injected via JavaScript -->
          </div>
        </div>

        <!-- Top Emotions Frequency -->
        <div class="shadcn-card p-3 sm:p-4 space-y-2">
          <h4 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-white" data-i18n="statsTopEmotionsTitle">
            Häufigste Emotionen
          </h4>
          <p class="text-[11px] text-slate-500" data-i18n="statsTopEmotionsSubtitle">Welche Gefühle haben dich im gewählten Zeitraum am meisten begleitet?</p>
          <div id="stats-top-emotions" class="space-y-1.5 pt-1">
            <!-- Injected via JavaScript -->
          </div>
        </div>

      </div>

    </div>
'''
