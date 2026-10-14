# -*- coding: utf-8 -*-

def get_diary_entry_view_html():
    return '''    <!-- ======================================================== -->
    <!-- MODULE B: DAILY LIFE DIARY & NEURO-TRACKER VIEWS          -->
    <!-- ======================================================== -->

    <!-- VIEW B1: TAGES-CHECK-IN (Ultra-Kompakt, 5 Unified Cards, Accordion & Focus-Modus) -->
    <div id="view-diary-entry" class="hidden space-y-2.5">

      <!-- TOP CONTROL CARD: DATE, VORTAG & FOCUS-NAV -->
      <section class="shadcn-card p-2.5 sm:p-3 space-y-2">
        
        <!-- Row 1: Check-in Status & Actions -->
        <div class="flex items-center justify-between pb-1.5 border-b border-slate-100 dark:border-slate-800 gap-2">
          <div class="flex items-center gap-1.5 min-w-0">
            <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-100 dark:bg-emerald-950/70 text-emerald-800 dark:text-emerald-300 shrink-0">
              Check-in
            </span>
            <span id="diary-current-day-label" class="text-xs font-bold text-slate-800 dark:text-slate-200 truncate">Heute</span>
          </div>

          <div class="flex items-center gap-1.5 shrink-0">
            <!-- Quick routine copy from yesterday -->
            <button type="button" onclick="copyRoutineFromPreviousDay()" class="text-[11px] font-bold px-2 py-1 rounded-lg border border-sky-200 dark:border-sky-800 bg-sky-50 dark:bg-sky-950/40 text-sky-700 dark:text-sky-300 hover:bg-sky-100 transition flex items-center gap-1 shadow-xs" title="Kopiert Medikation & Ziele vom Vortag">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
              <span>Vortag</span>
            </button>

            <button type="button" onclick="resetDiaryFormWithConfirm()" class="text-[11px] font-semibold px-2 py-1 rounded-lg border border-slate-200 dark:border-slate-700 text-rose-600 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/30 transition shadow-xs" title="Zurücksetzen">
              Leeren
            </button>
          </div>
        </div>

        <!-- Row 2: Date Selector & Accordion Toggle -->
        <div class="flex flex-wrap items-center justify-between gap-2 pt-0.5">
          <div class="flex items-center gap-1.5 min-w-0">
            <label for="input-diary-date" class="text-[11px] font-bold text-slate-500 uppercase tracking-wider shrink-0" id="label-diary-date">Datum:</label>
            <input type="date" id="input-diary-date" onchange="updateDiaryDateDisplay()" class="bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg px-2.5 py-1 text-xs text-slate-800 dark:text-slate-200 font-semibold focus:outline-none cursor-pointer">
          </div>

          <div class="flex items-center gap-1.5 shrink-0">
            <!-- Quick Accordion Toggle -->
            <button type="button" id="btn-toggle-all-cards" onclick="toggleAllCardsState()" class="shrink-0 px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white text-[11px] font-bold transition flex items-center gap-1 shadow-xs" title="Alle Karten ein-/ausklappen">
              <span id="label-toggle-all-cards">⤓ Zuklappen</span>
            </button>
          </div>
        </div>

        <!-- Row 3: Section Focus Navigation Bar (Smooth swipe on mobile) -->
        <div class="flex items-center gap-1 overflow-x-auto no-scrollbar py-0.5 pt-1.5 border-t border-slate-100 dark:border-slate-800">
          <button type="button" onclick="filterCheckinSections('all')" id="sec-nav-all" class="sec-nav-btn active px-2.5 py-1 rounded-lg bg-slate-900 text-white dark:bg-white dark:text-slate-900 font-bold transition shrink-0 text-xs">
            Alles
          </button>
          <button type="button" onclick="filterCheckinSections('mood')" id="sec-nav-mood" class="sec-nav-btn px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition shrink-0 text-xs">
            Mood
          </button>
          <button type="button" onclick="filterCheckinSections('meds')" id="sec-nav-meds" class="sec-nav-btn px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition shrink-0 text-xs">
            Medis
          </button>
          <button type="button" onclick="filterCheckinSections('vital')" id="sec-nav-vital" class="sec-nav-btn px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition shrink-0 text-xs">
            Vitales
          </button>
          <button type="button" onclick="filterCheckinSections('adhs')" id="sec-nav-adhs" class="sec-nav-btn px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition shrink-0 text-xs">
            ADHS & Steps
          </button>
          <button type="button" onclick="filterCheckinSections('mind')" id="sec-nav-mind" class="sec-nav-btn px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition shrink-0 text-xs">
            Journal
          </button>
        </div>

      </section>

      <!-- ======================================================== -->
      <!-- CARD 1: 🌈 GEMÜT, ENERGIE & GEFÜHLE                      -->
      <!-- ======================================================== -->
      <section id="card-diary-mood" class="checkin-card shadcn-card p-2.5 sm:p-3.5 space-y-2.5 transition-all duration-200 scroll-mt-28">
        
        <!-- Accordion Header -->
        <div onclick="toggleDiaryCard('mood')" class="flex items-center justify-between cursor-pointer select-none">
          <div class="flex items-center gap-2">
            <h3 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-white">
              1. Gemüt, Energie & Gefühle
            </h3>
          </div>
          <div class="flex items-center gap-1.5">
            <span id="badge-summary-mood" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950/70 text-emerald-800 dark:text-emerald-300">
              8/10 · Gut
            </span>
            <svg id="chevron-mood" class="w-4 h-4 text-slate-400 transition-transform duration-200 transform rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </div>
        </div>

        <!-- Accordion Body -->
        <div id="body-diary-mood" class="space-y-2.5 pt-1 border-t border-slate-100 dark:border-slate-800">
          
          <!-- FEATURE CONTAINER: MOOD & ENERGY -->
          <div id="feature-container-mood" class="space-y-2.5">
            <!-- Mood (1 - 10) -->
            <div class="space-y-1.5">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-slate-800 dark:text-slate-200">Wie ging es dir heute?</span>
                <span id="diary-mood-badge" class="px-2 py-0.5 rounded-full text-[11px] font-bold shadow-xs">8 / 10 · Gut</span>
              </div>

              <!-- Compact Visual Mood Banner -->
              <div id="diary-mood-banner" class="rounded-xl p-2 sm:p-2.5 flex items-center justify-between transition-colors duration-200 gap-2">
                <div class="flex items-center gap-2 min-w-0">
                  <span id="diary-mood-emoji" class="text-2xl shrink-0">😊</span>
                  <div class="min-w-0">
                    <div id="diary-mood-title" class="text-xs font-extrabold truncate">Zufrieden & Gut</div>
                    <div id="diary-mood-desc" class="text-[10px] opacity-90 truncate">Der Tag war stabil und angenehm.</div>
                  </div>
                </div>
                <div id="diary-mood-number" class="w-7 h-7 rounded-lg bg-white/40 dark:bg-black/20 flex items-center justify-center text-center text-sm font-black shrink-0">8</div>
              </div>

              <!-- Responsive Mood Slider -->
              <div class="space-y-1 pt-0.5">
                <input type="range" id="diary-mood-slider" min="1" max="10" value="8" step="1" oninput="updateMoodScore(this.value)" class="w-full h-2 bg-slate-200 dark:bg-slate-700 rounded-lg appearance-none cursor-pointer">
                <div class="flex justify-between text-[10px] text-slate-400 px-0.5 font-medium">
                  <span>1 = Tiefpunkt / Krise</span>
                  <span>5 = Neutral</span>
                  <span>10 = Hervorragend</span>
                </div>
              </div>
            </div>

            <!-- Energy Level (1 - 10) -->
            <div class="space-y-1 pt-1.5 border-t border-slate-100 dark:border-slate-800">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-slate-800 dark:text-slate-200">Energielevel & Vitalität</span>
                <span id="diary-energy-badge" class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-50 dark:bg-amber-950/60 text-amber-700 dark:text-amber-300">
                  7 / 10 · Aktiv
                </span>
              </div>
              <input type="range" id="diary-energy-slider" min="1" max="10" value="7" step="1" oninput="updateEnergyScore(this.value)" class="w-full h-1.5 bg-slate-200 dark:bg-slate-700 rounded-lg appearance-none cursor-pointer">
              <div class="flex justify-between text-[9px] text-slate-400 px-0.5">
                <span>1 = Erschöpft</span>
                <span>5 = Normal</span>
                <span>10 = Voll aufgeladen</span>
              </div>
            </div>
          </div>

          <!-- FEATURE CONTAINER: EMOTIONS & REFLECTION -->
          <div id="feature-container-emotions" class="space-y-2 pt-1.5 border-t border-slate-100 dark:border-slate-800">
            <!-- Emotionen Chips with Permanent Add (+) Button -->
            <div class="space-y-1.5">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-slate-800 dark:text-slate-200">
                  Gefühle heute: <span class="text-[10px] text-slate-400 font-normal">(Mehrfachauswahl möglich)</span>
                </span>
                <button type="button" onclick="openAddCustomModal('emotions')" class="px-2.5 py-1 rounded-lg border border-dashed border-emerald-400 dark:border-emerald-700 text-emerald-600 dark:text-emerald-400 text-xs font-bold hover:bg-emerald-50 dark:hover:bg-emerald-950/40 transition inline-flex items-center gap-1" title="Eigene Emotion hinzufügen">
                  <span>+ Neu</span>
                </button>
              </div>

              <!-- Pleasant Emotions -->
              <div class="space-y-0.5">
                <span class="text-[9px] font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Angenehm:</span>
                <div class="flex flex-wrap gap-1" id="pleasant-emotions-chips">
                  <!-- Dynamically populated -->
                </div>
              </div>

              <!-- Challenging Emotions -->
              <div class="space-y-0.5 pt-0.5">
                <span class="text-[9px] font-bold uppercase tracking-wider text-amber-600 dark:text-amber-400">Fordernd:</span>
                <div class="flex flex-wrap gap-1" id="challenging-emotions-chips">
                  <!-- Dynamically populated -->
                </div>
              </div>
            </div>

            <!-- Dynamic Emotion Reflection Notes -->
            <div id="diary-emotion-notes-wrapper" class="space-y-1 pt-1 border-t border-slate-100 dark:border-slate-800 hidden">
              <div class="flex items-center justify-between">
                <h4 class="text-xs font-bold text-slate-700 dark:text-slate-300">Gefühls-Reflexion:</h4>
                <span id="emotion-notes-count-badge" class="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-slate-100 dark:bg-slate-800 text-slate-500">0</span>
              </div>
              <div id="diary-emotion-notes-container" class="space-y-1.5">
                <!-- Dynamically injected cards -->
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- ======================================================== -->
      <!-- CARD 2: 💊 MEDIKATION, WIRKUNG & REBOUND                 -->
      <!-- ======================================================== -->
      <section id="card-diary-meds" class="checkin-card shadcn-card p-2.5 sm:p-3.5 space-y-2.5 transition-all duration-200 scroll-mt-28">
        
        <!-- Accordion Header -->
        <div onclick="toggleDiaryCard('meds')" class="flex items-center justify-between cursor-pointer select-none">
          <div class="flex items-center gap-2">
            <h3 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-white">
              2. Medikation & Wirkung
            </h3>
          </div>
          <div class="flex items-center gap-1.5">
            <span id="badge-summary-meds" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-violet-100 dark:bg-violet-950/70 text-violet-700 dark:text-violet-300">
              0 erfasst
            </span>
            <svg id="chevron-meds" class="w-4 h-4 text-slate-400 transition-transform duration-200 transform rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </div>
        </div>

        <!-- Accordion Body -->
        <div id="body-diary-meds" class="space-y-2.5 pt-1 border-t border-slate-100 dark:border-slate-800">
          
          <!-- FEATURE CONTAINER: MEDS LOG -->
          <div id="feature-container-meds-log" class="space-y-2.5">
            <!-- 1-Click Quick Meds Presets + Small (+) Button -->
            <div class="space-y-1">
              <div class="flex items-center justify-between">
                <span class="text-[10px] font-bold uppercase tracking-wider text-slate-500">Schnell-Auswahl (1-Klick):</span>
                <button type="button" onclick="openAddCustomModal('meds')" class="px-2.5 py-1 rounded-lg border border-dashed border-violet-400 dark:border-violet-700 text-violet-600 dark:text-violet-400 text-xs font-bold hover:bg-violet-50 dark:hover:bg-violet-950/40 transition inline-flex items-center gap-1" title="Eigenes Medikament dauerhaft hinzufügen">
                  <span>+ Neu</span>
                </button>
              </div>
              <div class="flex flex-wrap gap-1" id="quick-meds-chips-container">
                <!-- Dynamically populated with defaults + user custom meds -->
              </div>
            </div>

            <!-- Today's Logged Medications with Editable Time Field -->
            <div class="space-y-1.5">
              <div class="flex items-center justify-between">
                <span class="text-[10px] font-bold uppercase tracking-wider text-slate-500">Heute eingenommen:</span>
                <span id="meds-count-badge" class="text-[10px] font-bold text-violet-600 dark:text-violet-400">0 Medis</span>
              </div>
              <div id="today-meds-list" class="space-y-1">
                <!-- Dynamically populated with direct time input right on the pill -->
              </div>
            </div>
          </div>

          <!-- FEATURE CONTAINER: MEDS EFFICACY & REBOUND -->
          <div id="feature-container-meds-efficacy" class="space-y-2.5 pt-1 border-t border-slate-100 dark:border-slate-800">
            <!-- EFFICACY / WIRKUNGSBEWERTUNG (Single-Select Dropdown) -->
            <div class="p-2.5 rounded-xl bg-violet-50/50 dark:bg-violet-950/20 border border-violet-100 dark:border-violet-900/30 space-y-2">
              <div class="flex items-center justify-between">
                <label for="select-med-efficacy" class="text-xs font-bold text-violet-900 dark:text-violet-300">
                  Wie haben die Medis heute gewirkt?
                </label>
                <span id="med-efficacy-badge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-violet-100 dark:bg-violet-900/60 text-violet-700 dark:text-violet-300">
                  Noch offen
                </span>
              </div>

              <!-- Single-select Dropdown -->
              <select id="select-med-efficacy" onchange="setMedEfficacyRating(this.value)" class="shadcn-input text-xs py-2 font-semibold">
                <option value="none">-- Wirkung auswählen (Einzelauswahl) --</option>
                <option value="optimal">Optimal / Flow (fokussiert & ruhig)</option>
                <option value="gut">Gut & Stabil (gute Unterstützung)</option>
                <option value="schwach">Kaum Wirkung / Zu schwach</option>
                <option value="zu_stark">Zu intensiv / Überstimuliert</option>
                <option value="nebenwirkung">Nebenwirkungen / Unangenehm</option>
              </select>

              <!-- Efficacy Notes Textarea -->
              <textarea id="input-med-efficacy" rows="2" placeholder="Wirkungsbeobachtung (z. B. Fokus setzte nach 45 Min ein, ab 15 Uhr leichte Unruhe, kein Herzrasen)..." class="shadcn-input text-xs py-1.5 leading-relaxed"></textarea>
            </div>

            <!-- Rebound & Wirkungsende Box (Single-Select Dropdown) -->
            <div class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/40 border border-slate-200 dark:border-slate-700 space-y-1.5">
              <div class="flex items-center justify-between">
                <label for="select-med-rebound" class="text-xs font-bold text-slate-800 dark:text-slate-200">
                  Rebound / Wirkungsende?
                </label>
                <span id="rebound-badge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-300">Kein Rebound</span>
              </div>

              <select id="select-med-rebound" onchange="setReboundLevel(this.value)" class="shadcn-input text-xs py-2 font-semibold">
                <option value="none">Kein Rebound (sanftes Ausklingen)</option>
                <option value="leicht">Leicht (milde Erschöpfung)</option>
                <option value="spuerbar">Moderat (Reizbarkeit / Unruhe)</option>
                <option value="stark">Stark (Crasherlebnis / Tiefe Erschöpfung)</option>
              </select>

              <div class="grid grid-cols-1 sm:grid-cols-4 gap-2 pt-0.5">
                <div class="sm:col-span-1 min-w-0">
                  <input type="time" id="input-med-rebound-time" class="shadcn-input text-xs py-1.5 block w-full" placeholder="Uhrzeit" title="Rebound Uhrzeit">
                </div>
                <div class="sm:col-span-3 min-w-0">
                  <input type="text" id="input-med-rebound-notes" placeholder="Symptome (z. B. Konzentrationsabfall, Müdigkeit)..." class="shadcn-input text-xs py-1.5 block w-full">
                </div>
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- ======================================================== -->
      <!-- CARD 3: 🌿 VITAL-HUB: ESSEN, TRINKEN & SCHLAF             -->
      <!-- ======================================================== -->
      <section id="card-diary-vital" class="checkin-card shadcn-card p-2.5 sm:p-3.5 space-y-2.5 transition-all duration-200 scroll-mt-28">
        
        <!-- Accordion Header -->
        <div onclick="toggleDiaryCard('vital')" class="flex items-center justify-between cursor-pointer select-none">
          <div class="flex items-center gap-2">
            <h3 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-white">
              3. Vital-Hub: Mahlzeiten, Trinken & Schlaf
            </h3>
          </div>
          <div class="flex items-center gap-1.5">
            <span id="badge-summary-vital" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-sky-100 dark:bg-sky-950/70 text-sky-800 dark:text-sky-300">
              0 ml · 7.5h
            </span>
            <svg id="chevron-vital" class="w-4 h-4 text-slate-400 transition-transform duration-200 transform rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </div>
        </div>

        <!-- Accordion Body -->
        <div id="body-diary-vital" class="space-y-2.5 pt-1 border-t border-slate-100 dark:border-slate-800">
          
          <!-- FEATURE CONTAINER: MEALS -->
          <div id="feature-container-meals" class="space-y-1">
            <div class="flex items-center justify-between">
              <span class="text-[10px] font-bold uppercase tracking-wider text-slate-500">Mahlzeiten: <span class="text-[9px] text-slate-400 font-normal normal-case">(Mehrfachauswahl für Tags)</span></span>
              <button type="button" onclick="openAddCustomModal('meal_tags')" class="px-2.5 py-1 rounded-lg border border-dashed border-amber-400 dark:border-amber-700 text-amber-600 dark:text-amber-400 text-xs font-bold hover:bg-amber-50 dark:hover:bg-amber-950/40 transition inline-flex items-center gap-1" title="Eigenen Mahlzeiten-Tag hinzufügen">
                <span>+ Neu</span>
              </button>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
              <!-- Breakfast -->
              <div class="p-2 sm:p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-900/60 space-y-1.5 min-w-0">
                <span class="text-[11px] font-bold text-slate-900 dark:text-white block">Frühstück:</span>
                <textarea id="input-meal-breakfast" rows="2" placeholder="z. B. Rühreier mit Vollkornbrot..." class="shadcn-input text-xs py-1.5 px-2.5 block w-full resize-none !min-h-[46px]"></textarea>
              </div>

              <!-- Lunch -->
              <div class="p-2 sm:p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-900/60 space-y-1.5 min-w-0">
                <span class="text-[11px] font-bold text-slate-900 dark:text-white block">Mittag:</span>
                <textarea id="input-meal-lunch" rows="2" placeholder="z. B. Reisbowl mit Gemüse & Hähnchen..." class="shadcn-input text-xs py-1.5 px-2.5 block w-full resize-none !min-h-[46px]"></textarea>
              </div>

              <!-- Dinner -->
              <div class="p-2 sm:p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-900/60 space-y-1.5 min-w-0">
                <span class="text-[11px] font-bold text-slate-900 dark:text-white block">Abend:</span>
                <textarea id="input-meal-dinner" rows="2" placeholder="z. B. Gemüsesuppe, Salat, Lachs..." class="shadcn-input text-xs py-1.5 px-2.5 block w-full resize-none !min-h-[46px]"></textarea>
              </div>

              <!-- Snacks -->
              <div class="p-2 sm:p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-900/60 space-y-1.5 min-w-0">
                <span class="text-[11px] font-bold text-slate-900 dark:text-white block">Snacks:</span>
                <textarea id="input-meal-snacks" rows="2" placeholder="z. B. Nüsse, Proteinriegel, Apfel..." class="shadcn-input text-xs py-1.5 px-2.5 block w-full resize-none !min-h-[46px]"></textarea>
              </div>
            </div>

            <!-- Meal Tags Chips Container -->
            <div class="flex flex-wrap items-center gap-1 pt-0.5" id="meal-tags-container">
              <!-- Dynamically populated -->
            </div>
          </div>

          <!-- Hydration & Koffein Side-by-Side (Compact 2 Cols) -->
          <div id="vital-drinks-row" class="grid grid-cols-1 sm:grid-cols-2 gap-1.5 pt-1 border-t border-slate-100 dark:border-slate-800">
            <!-- FEATURE CONTAINER: WATER -->
            <div id="feature-container-water" class="p-2 rounded-xl border border-sky-100 dark:border-sky-900/40 bg-sky-50/40 dark:bg-sky-950/20 space-y-1.5 min-w-0">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-sky-900 dark:text-sky-300">Wasser:</span>
                <span id="water-display" class="text-xs font-bold text-sky-600 dark:text-sky-400">0 ml / 2500 ml</span>
              </div>
              <div class="w-full bg-slate-200 dark:bg-slate-700 h-2 rounded-full overflow-hidden">
                <div id="water-progress-bar" class="h-full bg-gradient-to-r from-sky-500 to-teal-500 transition-all duration-300 rounded-full" style="width: 0%"></div>
              </div>
              <div class="flex items-center gap-1">
                <button type="button" onclick="addWater(250)" class="text-[11px] font-bold px-2 py-0.5 rounded-lg bg-sky-600 hover:bg-sky-700 text-white transition shadow-xs">+ 250 ml</button>
                <button type="button" onclick="addWater(500)" class="text-[11px] font-bold px-2 py-0.5 rounded-lg bg-sky-600 hover:bg-sky-700 text-white transition shadow-xs">+ 500 ml</button>
                <button type="button" onclick="addWater(-250)" class="text-[11px] font-semibold px-1.5 py-0.5 rounded-lg border border-slate-300 dark:border-slate-600 text-slate-600 dark:text-slate-300 hover:bg-slate-100 transition">- 250</button>
                <button type="button" onclick="resetWater()" class="text-[10px] text-slate-400 hover:text-slate-600 ml-auto transition">Reset</button>
              </div>
            </div>

            <!-- FEATURE CONTAINER: CAFFEINE (INDEPENDENT COFFEE & ENERGY TRACKING) -->
            <div id="feature-container-caffeine" class="p-2.5 rounded-xl border border-amber-200 dark:border-amber-900/40 bg-amber-50/50 dark:bg-amber-950/20 space-y-1.5 min-w-0">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-amber-900 dark:text-amber-300">
                  Koffein & Stimulanzien:
                </span>
                <span id="caffeine-total-badge" class="text-xs font-extrabold text-amber-700 dark:text-amber-300 px-2 py-0.5 rounded-full bg-amber-100 dark:bg-amber-900/60 shadow-xs">
                  <span id="caffeine-display">0 mg</span>
                </span>
              </div>
              <p class="text-[10px] text-slate-500 dark:text-slate-400 leading-tight">
                Getrennt tracken und mixen · Wechselwirkung mit Medis beachten.
              </p>

              <!-- Two Independent Counters: Coffee & Energy Drink -->
              <div class="space-y-1.5 pt-0.5">
                <!-- Coffee Row -->
                <div class="flex items-center justify-between p-1.5 rounded-lg bg-white dark:bg-slate-900 border border-amber-200/70 dark:border-amber-800/40">
                  <div class="min-w-0">
                    <span class="text-xs font-bold text-slate-800 dark:text-slate-200">Kaffee</span>
                    <span class="text-[10px] text-slate-400 block sm:inline sm:ml-1">(~80 mg)</span>
                  </div>
                  <div class="flex items-center gap-1.5 shrink-0">
                    <button type="button" onclick="changeCoffee(-1)" class="w-6 h-6 rounded-md border border-slate-300 dark:border-slate-600 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-200 font-bold text-xs flex items-center justify-center transition" title="1 Tasse abziehen">-</button>
                    <span id="coffee-count-display" class="w-8 text-center text-xs font-black text-amber-800 dark:text-amber-300">0</span>
                    <button type="button" onclick="changeCoffee(1)" class="w-6 h-6 rounded-md bg-amber-600 hover:bg-amber-700 text-white font-bold text-xs flex items-center justify-center transition shadow-xs" title="1 Tasse hinzufügen">+</button>
                  </div>
                </div>

                <!-- Energy Drink Row -->
                <div class="flex items-center justify-between p-1.5 rounded-lg bg-white dark:bg-slate-900 border border-amber-200/70 dark:border-amber-800/40">
                  <div class="min-w-0">
                    <span class="text-xs font-bold text-slate-800 dark:text-slate-200">Energy Drink</span>
                    <span class="text-[10px] text-slate-400 block sm:inline sm:ml-1">(~150 mg)</span>
                  </div>
                  <div class="flex items-center gap-1.5 shrink-0">
                    <button type="button" onclick="changeEnergyDrink(-1)" class="w-6 h-6 rounded-md border border-slate-300 dark:border-slate-600 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-200 font-bold text-xs flex items-center justify-center transition" title="1 Dose abziehen">-</button>
                    <span id="energy-count-display" class="w-8 text-center text-xs font-black text-amber-800 dark:text-amber-300">0</span>
                    <button type="button" onclick="changeEnergyDrink(1)" class="w-6 h-6 rounded-md bg-amber-600 hover:bg-amber-700 text-white font-bold text-xs flex items-center justify-center transition shadow-xs" title="1 Dose hinzufügen">+</button>
                  </div>
                </div>
              </div>

              <!-- Summary Info Line -->
              <div id="caffeine-summary-text" class="text-[10px] text-slate-500 dark:text-slate-400 flex items-center justify-between pt-0.5">
                <span id="caffeine-mix-label">Mix: 0x Kaffee · 0x Energy</span>
                <button type="button" onclick="resetCaffeine()" class="text-[10px] text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 transition">Reset</button>
              </div>
            </div>
          </div>

          <!-- FEATURE CONTAINER: SLEEP -->
          <div id="feature-container-sleep" class="p-2.5 rounded-xl border border-indigo-100 dark:border-indigo-900/40 bg-indigo-50/30 dark:bg-indigo-950/15 space-y-2 pt-2 border-t border-slate-100 dark:border-slate-800">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-indigo-900 dark:text-indigo-300">
                Schlaf & Erholung:
              </span>
              <span id="sleep-badge" class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-indigo-100 dark:bg-indigo-950/70 text-indigo-700 dark:text-indigo-300">
                7.5 Std · Gut
              </span>
            </div>

            <!-- Times & Auto Calculator -->
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-1.5 sm:gap-2">
              <div class="min-w-0">
                <label class="block text-[9px] font-bold text-slate-500 mb-0.5">Zubettgehzeit:</label>
                <input type="time" id="input-sleep-bedtime" onchange="calculateSleepFromTimes()" class="shadcn-input text-xs font-semibold cursor-pointer py-1.5 block w-full">
              </div>
              <div class="min-w-0">
                <label class="block text-[9px] font-bold text-slate-500 mb-0.5">Aufwachzeit:</label>
                <input type="time" id="input-sleep-waketime" onchange="calculateSleepFromTimes()" class="shadcn-input text-xs font-semibold cursor-pointer py-1.5 block w-full">
              </div>
              <div class="col-span-2 sm:col-span-1 min-w-0">
                <label class="block text-[9px] font-bold text-slate-500 mb-0.5">Schlafdauer (Std):</label>
                <div class="flex items-center gap-1">
                  <input type="number" id="input-sleep-duration" step="0.25" min="0" max="24" value="7.5" oninput="updateSleepDurationDisplay()" class="shadcn-input text-xs font-bold py-1.5 flex-1 min-w-0 block">
                  <span class="text-xs font-bold text-slate-400 shrink-0">h</span>
                </div>
              </div>
            </div>

            <!-- Sleep Quality Rating (Single-Select Dropdown) -->
            <div class="space-y-1">
              <div class="flex items-center justify-between">
                <label for="select-sleep-quality" class="text-[11px] font-bold text-slate-700 dark:text-slate-300">Schlafqualität (Einzelauswahl):</label>
                <span id="sleep-quality-label" class="text-xs font-bold text-indigo-600 dark:text-indigo-400">4 / 5 · Gut</span>
              </div>
              <select id="select-sleep-quality" onchange="setSleepQuality(parseInt(this.value))" class="shadcn-input text-xs py-2 font-semibold">
                <option value="5">5 / 5 · Sehr erholsam & tief</option>
                <option value="4" selected>4 / 5 · Gut & ausreichend</option>
                <option value="3">3 / 5 · Mittelmäßig / unruhig</option>
                <option value="2">2 / 5 · Schlecht / oft aufgewacht</option>
                <option value="1">1 / 5 · Erschöpft & zerschlagen</option>
              </select>
            </div>

            <!-- Sleep Factors with (+) Button (Multi-Select) -->
            <div class="space-y-1 pt-0.5">
              <div class="flex items-center justify-between">
                <span class="text-[9px] font-bold uppercase tracking-wider text-slate-500">Schlaf-Faktoren: <span class="text-[9px] text-slate-400 font-normal normal-case">(Mehrfachauswahl)</span></span>
                <button type="button" onclick="openAddCustomModal('sleep_factors')" class="px-2.5 py-1 rounded-lg border border-dashed border-indigo-400 dark:border-indigo-700 text-indigo-600 dark:text-indigo-400 text-xs font-bold hover:bg-indigo-50 dark:hover:bg-indigo-950/40 transition inline-flex items-center gap-1" title="Eigenen Schlaffaktor dauerhaft hinzufügen">
                  <span>+ Neu</span>
                </button>
              </div>
              <div class="flex flex-wrap gap-1" id="sleep-factors-chips-container">
                <!-- Dynamically populated -->
              </div>
            </div>

          </div>

        </div>
      </section>

      <!-- ======================================================== -->
      <!-- CARD 4: 🧠 NEURO & BODY: ADHS, FOKUS & SCHRITTE          -->
      <!-- ======================================================== -->
      <section id="card-diary-adhs" class="checkin-card shadcn-card p-2.5 sm:p-3.5 space-y-2.5 transition-all duration-200 scroll-mt-28">
        
        <!-- Accordion Header -->
        <div onclick="toggleDiaryCard('adhs')" class="flex items-center justify-between cursor-pointer select-none">
          <div class="flex items-center gap-2">
            <h3 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-white">
              4. Neuro & Body: ADHS, Fokus & Schritte
            </h3>
          </div>
          <div class="flex items-center gap-1.5">
            <span id="badge-summary-adhs" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-pink-100 dark:bg-pink-950/70 text-pink-700 dark:text-pink-300">
              Fokus 7/10 · 0 Steps
            </span>
            <svg id="chevron-adhs" class="w-4 h-4 text-slate-400 transition-transform duration-200 transform rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </div>
        </div>

        <!-- Accordion Body -->
        <div id="body-diary-adhs" class="space-y-2.5 pt-1 border-t border-slate-100 dark:border-slate-800">
          
          <!-- FEATURE CONTAINER: ADHS, FOKUS & REIZE -->
          <div id="feature-container-adhs" class="space-y-2.5">
            <!-- 3 Sliders Grid: Focus, Restlessness, Brain Fog -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-1.5">
              <!-- Focus -->
              <div class="p-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-900/60 space-y-1">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-bold text-slate-900 dark:text-white">Fokus:</span>
                  <span id="adhs-focus-badge" class="text-xs font-extrabold text-emerald-600 dark:text-emerald-400">7 / 10</span>
                </div>
                <input type="range" id="input-adhs-focus" min="1" max="10" value="7" step="1" oninput="updateAdhsFocusScore(this.value)" class="w-full h-1.5 bg-slate-200 dark:bg-slate-700 rounded-lg appearance-none cursor-pointer">
                <div class="flex justify-between text-[9px] text-slate-400">
                  <span>Zerstreut</span>
                  <span>Im Flow</span>
                </div>
              </div>

              <!-- Restlessness -->
              <div class="p-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-900/60 space-y-1">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-bold text-slate-900 dark:text-white">Unruhe:</span>
                  <span id="adhs-restlessness-badge" class="text-xs font-extrabold text-amber-600 dark:text-amber-400">4 / 10</span>
                </div>
                <input type="range" id="input-adhs-restlessness" min="1" max="10" value="4" step="1" oninput="updateAdhsRestlessnessScore(this.value)" class="w-full h-1.5 bg-slate-200 dark:bg-slate-700 rounded-lg appearance-none cursor-pointer">
                <div class="flex justify-between text-[9px] text-slate-400">
                  <span>Ruhig</span>
                  <span>Getrieben</span>
                </div>
              </div>

              <!-- Brain Fog -->
              <div class="p-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-900/60 space-y-1">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-bold text-slate-900 dark:text-white">Brainfog:</span>
                  <span id="adhs-brainfog-badge" class="text-xs font-extrabold text-sky-600 dark:text-sky-400">2 / 10</span>
                </div>
                <input type="range" id="input-adhs-brainfog" min="1" max="10" value="2" step="1" oninput="updateAdhsBrainFogScore(this.value)" class="w-full h-1.5 bg-slate-200 dark:bg-slate-700 rounded-lg appearance-none cursor-pointer">
                <div class="flex justify-between text-[9px] text-slate-400">
                  <span>Klar</span>
                  <span>Nebel</span>
                </div>
              </div>
            </div>

            <!-- Executive Function & Sensory Overload (Single-Select Dropdowns) -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-0.5">
              <div class="space-y-1">
                <label for="select-adhs-executive" class="block text-[10px] font-bold text-slate-500 uppercase">Exekutive Funktion (Einzelauswahl):</label>
                <select id="select-adhs-executive" onchange="setExecutiveFunction(this.value)" class="shadcn-input text-xs py-2 font-semibold">
                  <option value="gut" selected>Flow & Fokussiert</option>
                  <option value="muehsam">Mühsam / Zerstreut</option>
                  <option value="paralysis">Paralysis / Blockade</option>
                  <option value="hyperfokus">Hyperfokus (stark vertieft)</option>
                </select>
              </div>

              <div class="space-y-1">
                <label for="select-adhs-sensory" class="block text-[10px] font-bold text-slate-500 uppercase">Reizoffenheit (Einzelauswahl):</label>
                <select id="select-adhs-sensory" onchange="setSensoryOverload(this.value)" class="shadcn-input text-xs py-2 font-semibold">
                  <option value="keine">Reizarm / Entspannt</option>
                  <option value="gering" selected>Leicht empfindlich</option>
                  <option value="mittel">Hohe Reizoffenheit</option>
                  <option value="stark">Sensorischer Overload / Reizflut</option>
                </select>
              </div>
            </div>

            <!-- ADHS Note / Win -->
            <div class="space-y-1 pt-0.5">
              <label class="block text-[11px] font-bold text-slate-700 dark:text-slate-300">
                ADHS-Erkenntnis, Dopamin-Hack oder Tagessieg:
              </label>
              <input type="text" id="input-adhs-notes" placeholder="z. B. 5-Minuten-Regel hat geholfen, Timer gestellt..." class="shadcn-input text-xs py-1.5">
            </div>
          </div>

          <!-- FEATURE CONTAINER: STEPS & AKTIVITÄTEN -->
          <div id="feature-container-steps" class="p-2.5 rounded-xl border border-blue-100 dark:border-blue-900/40 bg-blue-50/30 dark:bg-blue-950/15 space-y-2 pt-2 border-t border-slate-100 dark:border-slate-800">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-blue-900 dark:text-blue-300">
                Schritte & Bewegung:
              </span>
              <span id="steps-display-badge" class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-blue-100 dark:bg-blue-950/70 text-blue-700 dark:text-blue-300">
                0 Schritte
              </span>
            </div>

            <div class="w-full bg-slate-200 dark:bg-slate-700 h-2 rounded-full overflow-hidden">
              <div id="steps-progress-bar" class="h-full bg-gradient-to-r from-blue-500 to-indigo-500 transition-all duration-300 rounded-full" style="width: 0%"></div>
            </div>
            <div class="flex items-center justify-between text-[10px] text-slate-500">
              <span id="steps-progress-percent">0% erreicht (0 / 10.000)</span>
              <span>Tagesziel</span>
            </div>

            <div class="grid grid-cols-2 gap-2">
              <div class="min-w-0">
                <label class="block text-[9px] font-bold text-slate-500 mb-0.5">Schritte heute:</label>
                <input type="number" id="input-steps-count" min="0" step="100" value="0" oninput="updateStepsProgressDisplay()" class="shadcn-input text-xs font-extrabold text-blue-600 dark:text-blue-400 py-1.5 block w-full">
              </div>
              <div class="min-w-0">
                <label class="block text-[9px] font-bold text-slate-500 mb-0.5">Ziel:</label>
                <input type="number" id="input-steps-goal" min="1000" step="500" value="10000" oninput="updateStepsProgressDisplay()" class="shadcn-input text-xs font-semibold py-1.5 block w-full">
              </div>
            </div>

            <div class="flex flex-wrap items-center gap-1">
              <button type="button" onclick="addSteps(500)" class="text-[11px] font-bold px-2 py-0.5 rounded-lg bg-blue-50 dark:bg-blue-950/50 hover:bg-blue-100 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800 transition">+ 500</button>
              <button type="button" onclick="addSteps(1000)" class="text-[11px] font-bold px-2 py-0.5 rounded-lg bg-blue-50 dark:bg-blue-950/50 hover:bg-blue-100 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800 transition">+ 1k</button>
              <button type="button" onclick="addSteps(2500)" class="text-[11px] font-bold px-2 py-0.5 rounded-lg bg-blue-50 dark:bg-blue-950/50 hover:bg-blue-100 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800 transition">+ 2.5k</button>
              <button type="button" onclick="setSteps(10000)" class="text-[11px] font-bold px-2 py-0.5 rounded-lg bg-blue-600 text-white ml-auto transition shadow-xs">10k Ziel</button>
            </div>

            <!-- Sport & Aktivitäten Chips with (+) Button -->
            <div class="space-y-1 pt-1 border-t border-blue-200/40 dark:border-blue-900/30">
              <div class="flex items-center justify-between">
                <span class="text-[9px] font-bold uppercase tracking-wider text-slate-500">Aktivitäten & Sport: <span class="text-[9px] text-slate-400 font-normal normal-case">(Mehrfachauswahl)</span></span>
                <button type="button" onclick="openAddCustomModal('activities')" class="px-2.5 py-1 rounded-lg border border-dashed border-blue-400 dark:border-blue-700 text-blue-600 dark:text-blue-400 text-xs font-bold hover:bg-blue-50 dark:hover:bg-blue-950/40 transition inline-flex items-center gap-1" title="Eigene Aktivität dauerhaft hinzufügen">
                  <span>+ Neu</span>
                </button>
              </div>
              <div class="flex flex-wrap gap-1" id="activities-chips-container">
                <!-- Dynamically populated -->
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- ======================================================== -->
      <!-- CARD 5: 📖 JOURNAL, 3 POSITIVE DINGE & SPEICHERN         -->
      <!-- ======================================================== -->
      <section id="card-diary-mind" class="checkin-card shadcn-card p-2.5 sm:p-3.5 space-y-2.5 transition-all duration-200 scroll-mt-28">
        
        <!-- Accordion Header -->
        <div onclick="toggleDiaryCard('mind')" class="flex items-center justify-between cursor-pointer select-none">
          <div class="flex items-center gap-2">
            <h3 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-white">
              5. Journal, 3 Positive Dinge & Notizen
            </h3>
          </div>
          <div class="flex items-center gap-1.5">
            <span id="badge-summary-mind" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950/70 text-emerald-800 dark:text-emerald-300">
              0 / 3 Positiv
            </span>
            <svg id="chevron-mind" class="w-4 h-4 text-slate-400 transition-transform duration-200 transform rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </div>
        </div>

        <!-- Accordion Body -->
        <div id="body-diary-mind" class="space-y-2.5 pt-1 border-t border-slate-100 dark:border-slate-800">
          
          <!-- FEATURE CONTAINER: 3 POSITIVE DINGE -->
          <div id="feature-container-positive-things" class="space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-emerald-800 dark:text-emerald-400">
                3 Positive Dinge (Dopamin-Anker):
              </span>
              <span id="positive-things-counter" class="text-xs font-bold text-emerald-600 dark:text-emerald-400">
                0 / 3
              </span>
            </div>

            <div class="space-y-1.5" id="positive-things-inputs-container">
              <div class="flex items-center gap-2">
                <span class="w-6 h-6 rounded-lg bg-emerald-100 dark:bg-emerald-950/70 text-emerald-700 dark:text-emerald-300 font-bold text-xs flex items-center justify-center shrink-0">1</span>
                <input type="text" id="input-pos-1" oninput="updatePositiveThingsCounter()" placeholder="Ein schöner Moment heute..." class="flex-1 min-w-0 shadcn-input py-1.5 px-2.5 text-xs block">
              </div>
              <div class="flex items-center gap-2">
                <span class="w-6 h-6 rounded-lg bg-emerald-100 dark:bg-emerald-950/70 text-emerald-700 dark:text-emerald-300 font-bold text-xs flex items-center justify-center shrink-0">2</span>
                <input type="text" id="input-pos-2" oninput="updatePositiveThingsCounter()" placeholder="Ein Erfolg oder Lob..." class="flex-1 min-w-0 shadcn-input py-1.5 px-2.5 text-xs block">
              </div>
              <div class="flex items-center gap-2">
                <span class="w-6 h-6 rounded-lg bg-emerald-100 dark:bg-emerald-950/70 text-emerald-700 dark:text-emerald-300 font-bold text-xs flex items-center justify-center shrink-0">3</span>
                <input type="text" id="input-pos-3" oninput="updatePositiveThingsCounter()" placeholder="Zeit genommen für mich..." class="flex-1 min-w-0 shadcn-input py-1.5 px-2.5 text-xs block">
              </div>
            </div>

            <div class="pt-0.5">
              <button type="button" onclick="addAnotherPositiveThingInput()" class="text-[11px] text-emerald-700 dark:text-emerald-300 font-semibold hover:underline flex items-center gap-1">
                <span>+ Weiterer positiver Moment</span>
              </button>
            </div>
          </div>

          <!-- FEATURE CONTAINER: HIGHLIGHTS & MEMORIES -->
          <div id="feature-container-highlights" class="space-y-1 pt-1.5 border-t border-slate-100 dark:border-slate-800">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-amber-800 dark:text-amber-400">
                Highlights & Erlebnisse: <span class="text-[10px] text-slate-400 font-normal normal-case">(Mehrfachauswahl)</span>
              </span>
              <button type="button" onclick="openAddCustomModal('memory_tags')" class="px-2.5 py-1 rounded-lg border border-dashed border-amber-400 dark:border-amber-700 text-amber-600 dark:text-amber-400 text-xs font-bold hover:bg-amber-50 dark:hover:bg-amber-950/40 transition inline-flex items-center gap-1 shadow-xs" title="Eigenen Tag dauerhaft hinzufügen">
                <span>+ Neu</span>
              </button>
            </div>
            <textarea id="input-diary-highlights" rows="2" placeholder="Was waren heute die wichtigsten Momente deines Tages?..." class="shadcn-input text-xs py-1.5 leading-relaxed"></textarea>

            <div class="flex flex-wrap gap-1 pt-0.5" id="memory-tags-container">
              <!-- Dynamically populated -->
            </div>
          </div>

          <!-- FEATURE CONTAINER: BRAIN DUMP / NOTES -->
          <div id="feature-container-notes" class="space-y-1 pt-1.5 border-t border-slate-100 dark:border-slate-800">
            <span class="text-xs font-bold text-slate-800 dark:text-slate-200">
              Freie Gedanken & Brain Dump:
            </span>
            <textarea id="input-diary-notes" rows="3" placeholder="Schreibe ungefiltert auf, was dich heute beschäftigt hat..." class="shadcn-input text-xs py-1.5 leading-relaxed"></textarea>
          </div>

          <!-- ACTION FOOTER: SPEICHERN BUTTON -->
          <div class="pt-2 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between gap-2">
            <div class="text-[10px] text-slate-400 flex items-center gap-1">
              <span>100% lokal & privat</span>
            </div>
            <button type="button" onclick="saveCurrentDiaryEntry()" class="py-2.5 px-5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700 active:scale-[0.99] text-white font-bold text-xs sm:text-sm shadow-sm transition flex items-center justify-center gap-1.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"/></svg>
              <span>Tages-Eintrag speichern</span>
            </button>
          </div>

        </div>
      </section>

      <!-- Global Fallback Save Button (shown if Card 5 is hidden but at least one card is visible) -->
      <div id="diary-fallback-save-bar" class="hidden pt-2 flex items-center justify-between gap-2">
        <div class="text-[10px] text-slate-400 flex items-center gap-1">
          <span>100% lokal & privat</span>
        </div>
        <button type="button" onclick="saveCurrentDiaryEntry()" class="py-2.5 px-5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700 active:scale-[0.99] text-white font-bold text-xs sm:text-sm shadow-sm transition flex items-center justify-center gap-1.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"/></svg>
          <span id="label-fallback-save-btn">Tages-Eintrag speichern</span>
        </button>
      </div>

      <!-- ALL MODULES DISABLED NOTICE -->
      <div id="diary-all-disabled-notice" class="hidden p-6 rounded-2xl border-2 border-dashed border-slate-300 dark:border-slate-700 text-center space-y-3 bg-slate-50/50 dark:bg-slate-900/50 my-4">
        <div class="w-12 h-12 mx-auto rounded-full bg-slate-100 dark:bg-slate-800 flex items-center justify-center text-slate-400">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
        </div>
        <h3 class="text-sm sm:text-base font-bold text-slate-800 dark:text-slate-200" id="all-disabled-title">Alle Tracking-Module sind deaktiviert</h3>
        <p class="text-xs text-slate-500 max-w-sm mx-auto" id="all-disabled-desc">Du hast momentan alle Bereiche im Tagebuch ausgeblendet. Aktiviere Module in den Einstellungen, um loszulegen.</p>
        <button type="button" onclick="openSettingsModal()" class="px-4 py-2 rounded-xl bg-sky-600 hover:bg-sky-700 text-white font-bold text-xs shadow-xs transition inline-flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          <span id="all-disabled-btn">Module anpassen</span>
        </button>
      </div>

    </div>
'''
