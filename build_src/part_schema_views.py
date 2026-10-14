# -*- coding: utf-8 -*-

def get_schema_views_html():
    return '''    <!-- ======================================================== -->
    <!-- MODULE A: SCHEMA-MEMO VIEWS                               -->
    <!-- ======================================================== -->

    <!-- VIEW A1: SCHEMA EINGABE (Formular) -->
    <div id="view-edit" class="space-y-4">

      <!-- Top Banner / Title & Date -->
      <div class="shadcn-card p-3 sm:p-5 space-y-2.5">
        <div class="flex items-center justify-between gap-2">
          <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-sky-100 dark:bg-sky-900/60 text-sky-800 dark:text-sky-300">
            Situation reflektieren
          </span>

          <div class="flex items-center gap-1.5 shrink-0">
            <button type="button" onclick="loadExampleMemo()" class="text-[11px] font-semibold px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 transition shadow-xs">
              Beispiel
            </button>
            <button type="button" onclick="resetFormWithConfirm()" class="text-[11px] font-semibold px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700 text-rose-600 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/30 transition shadow-xs">
              Leeren
            </button>
          </div>
        </div>

        <!-- Titel & Datum Inputs -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
          <div class="sm:col-span-2 min-w-0">
            <label class="block text-[11px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1">
              Titel des Memos <span class="text-sky-500">*</span>
            </label>
            <input type="text" id="input-title" placeholder="z. B. Konflikt im Meeting, Absage, Einsamkeit..." class="shadcn-input font-medium block w-full">
          </div>
          <div class="min-w-0">
            <label class="block text-[11px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1">
              Datum
            </label>
            <input type="date" id="input-date" class="shadcn-input font-medium cursor-pointer block w-full">
          </div>
        </div>
      </div>

      <!-- STEP 1 CARD -->
      <section class="shadcn-card p-3 sm:p-5 space-y-3">
        <div class="flex items-center gap-2.5">
          <span class="w-7 h-7 rounded-full bg-sky-100 dark:bg-sky-900/60 text-sky-700 dark:text-sky-300 font-bold flex items-center justify-center text-xs">
            1
          </span>
          <h3 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white">
            Benennen des aktualisierten Gefühls
          </h3>
        </div>

        <div class="space-y-1.5">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            Im Augenblick fühle ich <span class="text-sky-600 dark:text-sky-400 font-bold">(Emotion)</span>
          </label>

          <div class="flex flex-wrap gap-1.5 py-0.5" id="schema-step1-chips">
            <button type="button" onclick="appendTag('input-emotion', 'Traurig')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Traurig</button>
            <button type="button" onclick="appendTag('input-emotion', 'Ängstlich')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Ängstlich</button>
            <button type="button" onclick="appendTag('input-emotion', 'Wütend')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Wütend</button>
            <button type="button" onclick="appendTag('input-emotion', 'Einsam')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Einsam</button>
            <button type="button" onclick="appendTag('input-emotion', 'Überfordert')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Überfordert</button>
            <button type="button" onclick="appendTag('input-emotion', 'Hilflosigkeit')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Hilflosigkeit</button>
            <button type="button" onclick="appendTag('input-emotion', 'Kränkung')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Kränkung</button>
            <button type="button" onclick="openAddCustomModal('schema_emotions')" class="text-xs px-2.5 py-1 rounded-full border border-dashed border-sky-400 dark:border-sky-700 text-sky-600 dark:text-sky-400 font-bold hover:bg-sky-50 dark:hover:bg-sky-950/40 transition">+ Neu</button>
          </div>

          <textarea id="input-emotion" rows="2" placeholder="z. B. tiefe Traurigkeit, Angst vor Ablehnung und Hilflosigkeit..." class="shadcn-input leading-relaxed"></textarea>
        </div>

        <div class="space-y-1.5 pt-1">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            Weil <span class="text-sky-600 dark:text-sky-400 font-bold">(aktuelle Auslösesituation)</span>
          </label>
          <textarea id="input-situation" rows="2" placeholder="z. B. mein Partner mir heute morgen nur kurz angebunden geantwortet hat..." class="shadcn-input leading-relaxed"></textarea>
        </div>
      </section>

      <!-- STEP 2 CARD -->
      <section class="shadcn-card p-3 sm:p-5 space-y-3">
        <div class="flex items-center gap-2.5">
          <span class="w-7 h-7 rounded-full bg-indigo-100 dark:bg-indigo-900/60 text-indigo-700 dark:text-indigo-300 font-bold flex items-center justify-center text-xs">
            2
          </span>
          <h3 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white">
            Erkennen der aktivierten Schemata/Modi und der Bewältigung
          </h3>
        </div>

        <div class="space-y-1.5">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            Ich weiß, dass das wahrscheinlich mein <span class="text-indigo-600 dark:text-indigo-400 font-bold">(Schema/Modus)</span> ... ist,
          </label>

          <div class="flex flex-wrap gap-1.5 py-0.5">
            <button type="button" onclick="setFieldValue('input-schema', 'Verlassenheit / Instabilität (Verletztes Kind)')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Verlassenheit / Verletztes Kind</button>
            <button type="button" onclick="setFieldValue('input-schema', 'Unzulänglichkeit / Scham (Strafender Modus)')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Unzulänglichkeit / Scham</button>
            <button type="button" onclick="setFieldValue('input-schema', 'Überhöhte Standards (Fordernder Modus)')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Überhöhte Standards</button>
            <button type="button" onclick="setFieldValue('input-schema', 'Unterwerfung / Aufopferung')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Unterwerfung</button>
            <button type="button" onclick="setFieldValue('input-schema', 'Distanzierter Beschützer (Rückzug)')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Distanzierter Beschützer</button>
          </div>

          <textarea id="input-schema" rows="2" placeholder="z. B. Verlassenheits-Schema und der Modus des verletzten Kindes..." class="shadcn-input leading-relaxed"></textarea>
        </div>

        <div class="space-y-1.5 pt-1">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            das/den ich durch <span class="text-indigo-600 dark:text-indigo-400 font-bold">(Kindheitssituation)</span> ... erlernt habe.
          </label>
          <textarea id="input-childhood" rows="2" placeholder="z. B. frühere Erfahrungen, in denen Eltern emotional distanziert waren..." class="shadcn-input leading-relaxed"></textarea>
        </div>

        <div class="space-y-1.5 pt-1">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            Diese Aktivierung löst bei mir <span class="text-indigo-600 dark:text-indigo-400 font-bold">(altes Bewältigungsverhalten)</span> ... aus.
          </label>
          <div class="flex flex-wrap gap-1.5 py-0.5" id="schema-step2-coping-chips">
            <button type="button" onclick="appendTag('input-coping', 'Rückzug & Mauern')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Rückzug & Mauern</button>
            <button type="button" onclick="appendTag('input-coping', 'Überanpassung')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Überanpassung</button>
            <button type="button" onclick="appendTag('input-coping', 'Vorwürfe & Wutausbruch')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Vorwürfe & Wut</button>
            <button type="button" onclick="appendTag('input-coping', 'Gefühle betäuben / Ablenken')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Ablenken</button>
            <button type="button" onclick="openAddCustomModal('schema_coping')" class="text-xs px-2.5 py-1 rounded-full border border-dashed border-indigo-400 dark:border-indigo-700 text-indigo-600 dark:text-indigo-400 font-bold hover:bg-indigo-50 dark:hover:bg-indigo-950/40 transition">+ Neu</button>
          </div>
          <textarea id="input-coping" rows="2" placeholder="z. B. innerer Rückzug, gekränktes Schweigen..." class="shadcn-input leading-relaxed"></textarea>
        </div>
      </section>

      <!-- STEP 3 CARD -->
      <section class="shadcn-card p-3 sm:p-5 space-y-3">
        <div class="flex items-center gap-2.5">
          <span class="w-7 h-7 rounded-full bg-amber-100 dark:bg-amber-900/60 text-amber-700 dark:text-amber-300 font-bold flex items-center justify-center text-xs">
            3
          </span>
          <h3 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white">
            Anerkennen der Dysfunktionalität / Realitätsprüfung
          </h3>
        </div>

        <div class="space-y-1.5">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            Obwohl ich glaube <span class="text-amber-600 dark:text-amber-400 font-bold">(negativer Gedanke/ Innere-Eltern-Stimme)</span>,
          </label>
          <textarea id="input-thought" rows="2" placeholder="z. B. dass ich nichts wert bin und niemand mich wirklich mag..." class="shadcn-input leading-relaxed"></textarea>
        </div>

        <div class="space-y-1.5 pt-1">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            ist die Realität <span class="text-amber-600 dark:text-amber-400 font-bold">(Sicht des Gesunden Erwachsenen)</span>,
          </label>
          <textarea id="input-reality" rows="2" placeholder="z. B. eine kurze Nachricht nicht bedeutet, dass kein Interesse da ist..." class="shadcn-input leading-relaxed"></textarea>
        </div>

        <div class="space-y-1.5 pt-1">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            Beweise für diese Realität sind:
          </label>
          <textarea id="input-evidence" rows="2" placeholder="z. B. gestern haben wir noch herzlich gelacht; die Person hat viel Stress..." class="shadcn-input leading-relaxed"></textarea>
        </div>
      </section>

      <!-- STEP 4 CARD -->
      <section class="shadcn-card p-3 sm:p-5 space-y-3">
        <div class="flex items-center gap-2.5">
          <span class="w-7 h-7 rounded-full bg-emerald-100 dark:bg-emerald-900/60 text-emerald-700 dark:text-emerald-300 font-bold flex items-center justify-center text-xs">
            4
          </span>
          <h3 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white">
            Trennen vom alten und Einbrennen des neuen Verhaltensimpulses
          </h3>
        </div>

        <div class="space-y-1.5">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            Obwohl ich am liebsten <span class="text-emerald-600 dark:text-emerald-400 font-bold">(altes dysfunktionales Verhalten)</span> ... würde,
          </label>
          <textarea id="input-old-behavior" rows="2" placeholder="z. B. mich tagelang zurückgezogen habe..." class="shadcn-input leading-relaxed"></textarea>
        </div>

        <div class="space-y-1.5 pt-1">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            Könnte ich stattdessen <span class="text-emerald-600 dark:text-emerald-400 font-bold">(alternative Lösungen)</span>
          </label>
          <div class="flex flex-wrap gap-1.5 py-0.5" id="schema-step4-action-chips">
            <button type="button" onclick="appendTag('input-new-action', 'Einmal tief durchatmen und mich erden')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-emerald-100 dark:hover:bg-emerald-900/40 text-slate-700 dark:text-slate-300 transition">Durchatmen</button>
            <button type="button" onclick="appendTag('input-new-action', 'Freundlich nachfragen oder Bedürfnis ansprechen')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-emerald-100 dark:hover:bg-emerald-900/40 text-slate-700 dark:text-slate-300 transition">Bedürfnis ansprechen</button>
            <button type="button" onclick="appendTag('input-new-action', 'Selbstfürsorge (Tee, Spaziergang, Ruhe)')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-emerald-100 dark:hover:bg-emerald-900/40 text-slate-700 dark:text-slate-300 transition">Selbstfürsorge</button>
            <button type="button" onclick="appendTag('input-new-action', 'Gesunden Erwachsenen liebevoll stärken')" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-emerald-100 dark:hover:bg-emerald-900/40 text-slate-700 dark:text-slate-300 transition">Gesunder Erwachsener</button>
            <button type="button" onclick="openAddCustomModal('schema_actions')" class="text-xs px-2.5 py-1 rounded-full border border-dashed border-emerald-400 dark:border-emerald-700 text-emerald-600 dark:text-emerald-400 font-bold hover:bg-emerald-50 dark:hover:bg-emerald-950/40 transition">+ Neu</button>
          </div>
          <textarea id="input-new-action" rows="2" placeholder="z. B. tief durchatmen, mir sagen 'Ich bin sicher', und ruhig nachfragen..." class="shadcn-input leading-relaxed"></textarea>
        </div>
      </section>

      <!-- Save & Preview Action Bar -->
      <div class="pt-2 flex flex-col sm:flex-row items-center gap-2">
        <button type="button" onclick="saveCurrentMemo()" class="w-full sm:flex-1 py-3 px-4 rounded-xl bg-gradient-to-r from-sky-600 to-indigo-600 hover:from-sky-700 hover:to-indigo-700 active:scale-[0.99] text-white font-bold text-sm shadow-md shadow-sky-500/20 transition flex items-center justify-center gap-2">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"/></svg>
          <span>Speichern & Blatt ansehen</span>
        </button>

        <button type="button" onclick="previewCurrentSheet()" class="w-full sm:w-auto py-3 px-5 rounded-xl border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 active:scale-[0.99] font-semibold text-sm transition flex items-center justify-center gap-1.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
          <span>Blatt-Vorschau</span>
        </button>
      </div>

    </div>

    <!-- VIEW A2: SCHEMA BLATTANSICHT (Original-Vorlage) -->
    <div id="view-sheet" class="hidden space-y-4">

      <!-- Sheet Toolbar -->
      <div class="no-print shadcn-card p-3 flex flex-wrap items-center justify-between gap-2">
        <div class="flex items-center gap-1.5">
          <button onclick="switchView('edit')" class="px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 text-xs font-semibold transition flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
            <span>Bearbeiten</span>
          </button>

          <button onclick="printSheet()" class="px-3 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-700 text-white text-xs font-bold transition flex items-center gap-1.5 shadow-sm">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
            <span>Drucken / PDF</span>
          </button>
        </div>

        <div class="flex items-center gap-1.5">
          <select id="font-style-select" onchange="changeSheetFont(this.value)" class="bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-lg px-2.5 py-1 text-xs text-slate-700 dark:text-slate-200 font-medium focus:outline-none">
            <option value="kalam-blue" selected>Handschrift Blau</option>
            <option value="caveat-black">Handschrift Schwarz</option>
            <option value="clean-sans">Druckschrift</option>
          </select>

          <button type="button" id="btn-toggle-blank" onclick="toggleBlankMode()" class="px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 text-xs font-medium hover:bg-slate-100 dark:hover:bg-slate-800 transition">
            Vorlage
          </button>
        </div>
      </div>

      <!-- THE SHEET -->
      <div class="w-full">
        <div id="worksheet-paper" class="sheet-paper w-full rounded-2xl p-4 sm:p-10 md:p-12 text-slate-900 dark:text-slate-100 font-sheet transition-all">

          <!-- Header Metadata -->
          <div id="sheet-header-meta" class="mb-5 pb-2 border-b border-slate-200 dark:border-slate-800 flex flex-wrap items-center justify-between text-xs text-slate-500 dark:text-slate-400 gap-1">
            <div class="flex items-center gap-1.5 font-medium">
              <span class="font-bold text-slate-900 dark:text-white uppercase tracking-wider text-[11px]">Schema-Memo</span>
              <span id="sheet-meta-title" class="text-slate-800 dark:text-slate-200 font-semibold"></span>
            </div>
            <div id="sheet-meta-date" class="text-slate-500 dark:text-slate-400"></div>
          </div>

          <!-- SECTION 1 -->
          <div class="mb-6">
            <h2 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white mb-2.5">
              1. Benennen des aktualisierten Gefühls
            </h2>

            <div class="mb-3">
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1">
                Im Augenblick fühle ich (Emotion)
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-emotion"></span>
              </div>
              <div class="dotted-rule mt-1">
                <span class="sheet-user-content sheet-val-l2" id="sheet-val-emotion-extra"></span>
              </div>
            </div>

            <div>
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1">
                weil (aktuelle Auslösesituation)
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-situation"></span>
              </div>
              <div class="dotted-rule mt-1">
                <span class="sheet-user-content sheet-val-l2" id="sheet-val-situation-extra"></span>
              </div>
            </div>
          </div>

          <!-- SECTION 2 -->
          <div class="mb-6">
            <h2 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white mb-2.5">
              2. Erkennen der aktivierten Schemata/Modi und der Bewältigung
            </h2>

            <div class="mb-3">
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1">
                Ich weiß, dass das wahrscheinlich mein (Schema/Modus) ... ist,
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-schema"></span>
              </div>
            </div>

            <div class="mb-3">
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1">
                das/den ich durch (Kindheitssituation) ... erlernt habe.
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-childhood"></span>
              </div>
            </div>

            <div>
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1">
                Diese Aktivierung löst bei mir (altes Bewältigungsverhalten) ... aus.
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-coping"></span>
              </div>
            </div>
          </div>

          <!-- SECTION 3 -->
          <div class="mb-6">
            <h2 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white mb-2.5">
              3. Anerkennen der Dysfunktionalität / Realitätsprüfung
            </h2>

            <div class="mb-3">
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1">
                Obwohl ich glaube (negativer Gedanke/ Innere-Eltern-Stimme),
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-thought"></span>
              </div>
            </div>

            <div class="mb-3">
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1">
                ist die Realität (Sicht des Gesunden Erwachsenen),
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-reality"></span>
              </div>
            </div>

            <div>
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1">
                Beweise für diese Realität sind:
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-evidence"></span>
              </div>
              <div class="dotted-rule mt-1">
                <span class="sheet-user-content sheet-val-l2" id="sheet-val-evidence-extra"></span>
              </div>
            </div>
          </div>

          <!-- SECTION 4 -->
          <div class="mb-6">
            <h2 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white mb-2.5">
              4. Trennen vom alten und Einbrennen des neuen Verhaltensimpulses
            </h2>

            <div class="mb-3">
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1">
                Obwohl ich am liebsten (altes dysfunktionales Verhalten) ... würde,
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-old-behavior"></span>
              </div>
            </div>

            <div>
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1">
                Könnte ich stattdessen (alternative Lösungen)
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-new-action"></span>
              </div>
              <div class="dotted-rule mt-1">
                <span class="sheet-user-content sheet-val-l2" id="sheet-val-new-action-extra"></span>
              </div>
            </div>
          </div>

          <!-- FOOTER / COPYRIGHT (REQUIRED) -->
          <div class="mt-8 pt-3 border-t border-slate-200 dark:border-slate-800 text-center text-[10px] text-slate-500 dark:text-slate-400">
            Modifiziert nach J. Young 1996/2002. Das Original ist urheberrechtlich geschützt.
          </div>

        </div>
      </div>

    </div>

    <!-- VIEW A3: SCHEMA ARCHIV -->
    <div id="view-archive" class="hidden space-y-4">
      <div class="shadcn-card p-3 sm:p-5 space-y-2.5">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <h2 class="text-base sm:text-xl font-bold tracking-tight text-slate-900 dark:text-white">Gespeicherte Schema-Memos</h2>
            <p class="text-xs text-slate-500 dark:text-slate-400">Verwalte deine reflektierten Memos und verfolge deinen Therapiefortschritt.</p>
          </div>

          <div class="flex items-center gap-1.5">
            <button onclick="exportJSON()" class="px-2.5 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-xs font-semibold hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1">
              <span>Export</span>
            </button>
            <label class="px-2.5 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-xs font-semibold hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1 cursor-pointer">
              <span>Import</span>
              <input type="file" id="import-file" accept=".json" onchange="importJSON(event)" class="hidden">
            </label>
          </div>
        </div>

        <div class="pt-1">
          <input type="text" id="archive-search-input" oninput="renderArchiveList()" placeholder="Memos nach Titel, Situation oder Schema durchsuchen..." class="shadcn-input text-xs">
        </div>
      </div>

      <div id="archive-list-container" class="space-y-3">
        <!-- Rendered via JavaScript -->
      </div>
    </div>

    <!-- VIEW A4: SCHEMA SPICKZETTEL / HILFE -->
    <div id="view-help" class="hidden space-y-4">
      <div class="shadcn-card p-3 sm:p-5 space-y-2.5">
        <h2 class="text-base sm:text-xl font-bold tracking-tight text-slate-900 dark:text-white">Schema-Therapie Spickzettel</h2>
        <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
          Kompaktes Nachschlagewerk über die 18 Schemata und Modi nach Jeffrey Young zur schnellen Orientierung während der Reflexion.
        </p>
      </div>

      <!-- Schemata Accordions/Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div class="shadcn-card p-3 sm:p-4 space-y-1.5">
          <span class="text-xs font-bold text-sky-600 dark:text-sky-400 uppercase tracking-wider">Bereich 1</span>
          <h3 class="text-sm font-bold text-slate-900 dark:text-white">Abweisung & Trennung</h3>
          <p class="text-xs text-slate-500 leading-relaxed">
            Verlassenheit / Instabilität, Misstrauen / Missbrauch, Emotionale Vernachlässigung, Unzulänglichkeit / Scham, Soziale Isolation.
          </p>
        </div>

        <div class="shadcn-card p-3 sm:p-4 space-y-1.5">
          <span class="text-xs font-bold text-indigo-600 dark:text-indigo-400 uppercase tracking-wider">Bereich 2</span>
          <h3 class="text-sm font-bold text-slate-900 dark:text-white">Autonomie & Leistung</h3>
          <p class="text-xs text-slate-500 leading-relaxed">
            Abhängigkeit / Inkompetenz, Anfälligkeit für Verletzungen oder Krankheiten, Verstrickung / Unterentwickeltes Selbst, Versagen.
          </p>
        </div>

        <div class="shadcn-card p-3 sm:p-4 space-y-1.5">
          <span class="text-xs font-bold text-amber-600 dark:text-amber-400 uppercase tracking-wider">Bereich 3</span>
          <h3 class="text-sm font-bold text-slate-900 dark:text-white">Beeinträchtigte Grenzen</h3>
          <p class="text-xs text-slate-500 leading-relaxed">
            Anspruchshaltung / Grandiosität, Ungenügende Selbstkontrolle / Selbstdisziplin.
          </p>
        </div>

        <div class="shadcn-card p-3 sm:p-4 space-y-1.5">
          <span class="text-xs font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-wider">Bereich 4</span>
          <h3 class="text-sm font-bold text-slate-900 dark:text-white">Fremdbezogenheit</h3>
          <p class="text-xs text-slate-500 leading-relaxed">
            Unterwerfung, Aufopferung, Streben nach Anerkennung & Bestätigung.
          </p>
        </div>
      </div>
    </div>
'''
