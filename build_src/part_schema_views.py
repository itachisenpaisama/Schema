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
          <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-sky-100 dark:bg-sky-900/60 text-sky-800 dark:text-sky-300" data-i18n="schemaReflectBanner">
            Situation reflektieren
          </span>

          <div class="flex items-center gap-1.5 shrink-0">
            <button type="button" onclick="loadExampleMemo()" class="text-[11px] font-semibold px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 transition shadow-xs" data-i18n="btnExample">
              Beispiel
            </button>
            <button type="button" onclick="resetFormWithConfirm()" class="text-[11px] font-semibold px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700 text-rose-600 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/30 transition shadow-xs" data-i18n="quickReset">
              Leeren
            </button>
          </div>
        </div>

        <!-- Titel & Datum Inputs -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
          <div class="sm:col-span-2 min-w-0">
            <label class="block text-[11px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1">
              <span data-i18n="schemaLabelTitle">Titel des Memos</span> <span class="text-sky-500">*</span>
            </label>
            <input type="text" id="input-title" placeholder="z. B. Konflikt im Meeting, Absage, Einsamkeit..." data-i18n-placeholder="schemaPlaceholderTitle" class="shadcn-input font-medium block w-full">
          </div>
          <div class="min-w-0">
            <label class="block text-[11px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1" data-i18n="schemaLabelDate">
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
          <h3 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white" data-i18n="schemaStep1Title">
            Benennen des aktualisierten Gefühls
          </h3>
        </div>

        <div class="space-y-1.5">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            <span data-i18n="schemaStep1Prompt">Im Augenblick fühle ich</span> <span class="text-sky-600 dark:text-sky-400 font-bold" data-i18n="schemaStep1PromptBracket">(Emotion)</span>
          </label>

          <div class="flex flex-wrap gap-1.5 py-0.5" id="schema-step1-chips">
            <button type="button" onclick="appendTag('input-emotion', 'Traurig')" data-tag="Traurig" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Traurig</button>
            <button type="button" onclick="appendTag('input-emotion', 'Ängstlich')" data-tag="Ängstlich" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Ängstlich</button>
            <button type="button" onclick="appendTag('input-emotion', 'Wütend')" data-tag="Wütend" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Wütend</button>
            <button type="button" onclick="appendTag('input-emotion', 'Einsam')" data-tag="Einsam" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Einsam</button>
            <button type="button" onclick="appendTag('input-emotion', 'Überfordert')" data-tag="Überfordert" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Überfordert</button>
            <button type="button" onclick="appendTag('input-emotion', 'Hilflosigkeit')" data-tag="Hilflosigkeit" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Hilflosigkeit</button>
            <button type="button" onclick="appendTag('input-emotion', 'Kränkung')" data-tag="Kränkung" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-sky-100 dark:hover:bg-sky-900/40 text-slate-700 dark:text-slate-300 transition">Kränkung</button>
            <button type="button" onclick="openAddCustomModal('schema_emotions')" class="add-custom-btn text-xs px-2.5 py-1 rounded-full border border-dashed border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-300 font-semibold hover:border-slate-500 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 transition inline-flex items-center gap-1" title="Eigene Emotion hinzufügen" data-i18n-title="addCustomEmotionTooltip"><span class="font-bold text-sm leading-none">+</span><span class="add-btn-label">Neu</span></button>
          </div>

          <textarea id="input-emotion" rows="2" placeholder="z. B. tiefe Traurigkeit, Angst vor Ablehnung und Hilflosigkeit..." data-i18n-placeholder="schemaPlaceholderEmotion" class="shadcn-input leading-relaxed"></textarea>
        </div>

        <div class="space-y-1.5 pt-1">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            <span data-i18n="schemaStep1Because">Weil</span> <span class="text-sky-600 dark:text-sky-400 font-bold" data-i18n="schemaStep1BecauseBracket">(aktuelle Auslösesituation)</span>
          </label>
          <textarea id="input-situation" rows="2" placeholder="z. B. mein Partner mir heute morgen nur kurz angebunden geantwortet hat..." data-i18n-placeholder="schemaPlaceholderSituation" class="shadcn-input leading-relaxed"></textarea>
        </div>
      </section>

      <!-- STEP 2 CARD -->
      <section class="shadcn-card p-3 sm:p-5 space-y-3">
        <div class="flex items-center gap-2.5">
          <span class="w-7 h-7 rounded-full bg-indigo-100 dark:bg-indigo-900/60 text-indigo-700 dark:text-indigo-300 font-bold flex items-center justify-center text-xs">
            2
          </span>
          <h3 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white" data-i18n="schemaStep2Title">
            Erkennen der aktivierten Schemata/Modi und der Bewältigung
          </h3>
        </div>

        <div class="space-y-1.5">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            <span data-i18n="schemaStep2Prompt">Ich weiß, dass das wahrscheinlich mein</span> <span class="text-indigo-600 dark:text-indigo-400 font-bold" data-i18n="schemaStep2PromptBracket">(Schema/Modus)</span> <span data-i18n="schemaStep2PromptSuffix">... ist,</span>
          </label>

          <div class="flex flex-wrap gap-1.5 py-0.5">
            <button type="button" onclick="setFieldValue('input-schema', 'Verlassenheit / Instabilität (Verletztes Kind)')" data-tag="Verlassenheit / Verletztes Kind" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Verlassenheit / Verletztes Kind</button>
            <button type="button" onclick="setFieldValue('input-schema', 'Unzulänglichkeit / Scham (Strafender Modus)')" data-tag="Unzulänglichkeit / Scham" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Unzulänglichkeit / Scham</button>
            <button type="button" onclick="setFieldValue('input-schema', 'Überhöhte Standards (Fordernder Modus)')" data-tag="Überhöhte Standards" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Überhöhte Standards</button>
            <button type="button" onclick="setFieldValue('input-schema', 'Unterwerfung / Aufopferung')" data-tag="Unterwerfung" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Unterwerfung</button>
            <button type="button" onclick="setFieldValue('input-schema', 'Distanzierter Beschützer (Rückzug)')" data-tag="Distanzierter Beschützer" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Distanzierter Beschützer</button>
          </div>

          <textarea id="input-schema" rows="2" placeholder="z. B. Verlassenheits-Schema und der Modus des verletzten Kindes..." data-i18n-placeholder="schemaPlaceholderSchema" class="shadcn-input leading-relaxed"></textarea>
        </div>

        <div class="space-y-1.5 pt-1">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            <span data-i18n="schemaStep2Childhood">das/den ich durch</span> <span class="text-indigo-600 dark:text-indigo-400 font-bold" data-i18n="schemaStep2ChildhoodBracket">(Kindheitssituation)</span> <span data-i18n="schemaStep2ChildhoodSuffix">... erlernt habe.</span>
          </label>
          <textarea id="input-childhood" rows="2" placeholder="z. B. frühere Erfahrungen, in denen Eltern emotional distanziert waren..." data-i18n-placeholder="schemaPlaceholderChildhood" class="shadcn-input leading-relaxed"></textarea>
        </div>

        <div class="space-y-1.5 pt-1">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            <span data-i18n="schemaStep2Coping">Diese Aktivierung löst bei mir</span> <span class="text-indigo-600 dark:text-indigo-400 font-bold" data-i18n="schemaStep2CopingBracket">(altes Bewältigungsverhalten)</span> <span data-i18n="schemaStep2CopingSuffix">... aus.</span>
          </label>
          <div class="flex flex-wrap gap-1.5 py-0.5" id="schema-step2-coping-chips">
            <button type="button" onclick="appendTag('input-coping', 'Rückzug & Mauern')" data-tag="Rückzug & Mauern" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Rückzug & Mauern</button>
            <button type="button" onclick="appendTag('input-coping', 'Überanpassung')" data-tag="Überanpassung" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Überanpassung</button>
            <button type="button" onclick="appendTag('input-coping', 'Vorwürfe & Wutausbruch')" data-tag="Vorwürfe & Wut" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Vorwürfe & Wut</button>
            <button type="button" onclick="appendTag('input-coping', 'Gefühle betäuben / Ablenken')" data-tag="Ablenken" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-indigo-100 dark:hover:bg-indigo-900/40 text-slate-700 dark:text-slate-300 transition">Ablenken</button>
            <button type="button" onclick="openAddCustomModal('schema_coping')" class="add-custom-btn text-xs px-2.5 py-1 rounded-full border border-dashed border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-300 font-semibold hover:border-slate-500 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 transition inline-flex items-center gap-1" title="Eigenes Bewältigungsverhalten hinzufügen" data-i18n-title="addCustomCopingTooltip"><span class="font-bold text-sm leading-none">+</span><span class="add-btn-label">Neu</span></button>
          </div>
          <textarea id="input-coping" rows="2" placeholder="z. B. innerer Rückzug, gekränktes Schweigen..." data-i18n-placeholder="schemaPlaceholderCoping" class="shadcn-input leading-relaxed"></textarea>
        </div>
      </section>

      <!-- STEP 3 CARD -->
      <section class="shadcn-card p-3 sm:p-5 space-y-3">
        <div class="flex items-center gap-2.5">
          <span class="w-7 h-7 rounded-full bg-amber-100 dark:bg-amber-900/60 text-amber-700 dark:text-amber-300 font-bold flex items-center justify-center text-xs">
            3
          </span>
          <h3 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white" data-i18n="schemaStep3Title">
            Anerkennen der Dysfunktionalität / Realitätsprüfung
          </h3>
        </div>

        <div class="space-y-1.5">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            <span data-i18n="schemaStep3Thought">Obwohl ich glaube</span> <span class="text-amber-600 dark:text-amber-400 font-bold" data-i18n="schemaStep3ThoughtBracket">(negativer Gedanke/ Innere-Eltern-Stimme)</span>,
          </label>
          <textarea id="input-thought" rows="2" placeholder="z. B. dass ich nichts wert bin und niemand mich wirklich mag..." data-i18n-placeholder="schemaPlaceholderThought" class="shadcn-input leading-relaxed"></textarea>
        </div>

        <div class="space-y-1.5 pt-1">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            <span data-i18n="schemaStep3Reality">ist die Realität</span> <span class="text-amber-600 dark:text-amber-400 font-bold" data-i18n="schemaStep3RealityBracket">(Sicht des Gesunden Erwachsenen)</span>,
          </label>
          <textarea id="input-reality" rows="2" placeholder="z. B. eine kurze Nachricht nicht bedeutet, dass kein Interesse da ist..." data-i18n-placeholder="schemaPlaceholderReality" class="shadcn-input leading-relaxed"></textarea>
        </div>

        <div class="space-y-1.5 pt-1">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200" data-i18n="schemaStep3Evidence">
            Beweise für diese Realität sind:
          </label>
          <textarea id="input-evidence" rows="2" placeholder="z. B. gestern haben wir noch herzlich gelacht; die Person hat viel Stress..." data-i18n-placeholder="schemaPlaceholderEvidence" class="shadcn-input leading-relaxed"></textarea>
        </div>
      </section>

      <!-- STEP 4 CARD -->
      <section class="shadcn-card p-3 sm:p-5 space-y-3">
        <div class="flex items-center gap-2.5">
          <span class="w-7 h-7 rounded-full bg-emerald-100 dark:bg-emerald-900/60 text-emerald-700 dark:text-emerald-300 font-bold flex items-center justify-center text-xs">
            4
          </span>
          <h3 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white" data-i18n="schemaStep4Title">
            Trennen vom alten und Einbrennen des neuen Verhaltensimpulses
          </h3>
        </div>

        <div class="space-y-1.5">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            <span data-i18n="schemaStep4Old">Obwohl ich am liebsten</span> <span class="text-emerald-600 dark:text-emerald-400 font-bold" data-i18n="schemaStep4OldBracket">(altes dysfunktionales Verhalten)</span> <span data-i18n="schemaStep4OldSuffix">... würde,</span>
          </label>
          <textarea id="input-old-behavior" rows="2" placeholder="z. B. mich tagelang zurückgezogen habe..." data-i18n-placeholder="schemaPlaceholderOldBehavior" class="shadcn-input leading-relaxed"></textarea>
        </div>

        <div class="space-y-1.5 pt-1">
          <label class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-200">
            <span data-i18n="schemaStep4New">Könnte ich stattdessen</span> <span class="text-emerald-600 dark:text-emerald-400 font-bold" data-i18n="schemaStep4NewBracket">(alternative Lösungen)</span>
          </label>
          <div class="flex flex-wrap gap-1.5 py-0.5" id="schema-step4-action-chips">
            <button type="button" onclick="appendTag('input-new-action', 'Durchatmen')" data-tag="Durchatmen" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-emerald-100 dark:hover:bg-emerald-900/40 text-slate-700 dark:text-slate-300 transition">Durchatmen</button>
            <button type="button" onclick="appendTag('input-new-action', 'Bedürfnis ansprechen')" data-tag="Bedürfnis ansprechen" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-emerald-100 dark:hover:bg-emerald-900/40 text-slate-700 dark:text-slate-300 transition">Bedürfnis ansprechen</button>
            <button type="button" onclick="appendTag('input-new-action', 'Selbstfürsorge')" data-tag="Selbstfürsorge" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-emerald-100 dark:hover:bg-emerald-900/40 text-slate-700 dark:text-slate-300 transition">Selbstfürsorge</button>
            <button type="button" onclick="appendTag('input-new-action', 'Gesunder Erwachsener')" data-tag="Gesunder Erwachsener" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-emerald-100 dark:hover:bg-emerald-900/40 text-slate-700 dark:text-slate-300 transition">Gesunder Erwachsener</button>
            <button type="button" onclick="openAddCustomModal('schema_actions')" class="add-custom-btn text-xs px-2.5 py-1 rounded-full border border-dashed border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-300 font-semibold hover:border-slate-500 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 transition inline-flex items-center gap-1" title="Eigene Handlung hinzufügen" data-i18n-title="addCustomActionTooltip"><span class="font-bold text-sm leading-none">+</span><span class="add-btn-label">Neu</span></button>
          </div>
          <textarea id="input-new-action" rows="2" placeholder="z. B. tief durchatmen, mir sagen 'Ich bin sicher', und ruhig nachfragen..." data-i18n-placeholder="schemaPlaceholderNewAction" class="shadcn-input leading-relaxed"></textarea>
        </div>
      </section>

      <!-- Save & Preview Action Bar -->
      <div class="pt-2 flex flex-col sm:flex-row items-center gap-2">
        <button type="button" onclick="saveCurrentMemo()" class="w-full sm:flex-1 py-3 px-4 rounded-xl bg-gradient-to-r from-sky-600 to-indigo-600 hover:from-sky-700 hover:to-indigo-700 active:scale-[0.99] text-white font-bold text-sm shadow-md shadow-sky-500/20 transition flex items-center justify-center gap-2">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"/></svg>
          <span data-i18n="schemaBtnSaveSheet">Speichern & Blatt ansehen</span>
        </button>

        <button type="button" onclick="previewCurrentSheet()" class="w-full sm:w-auto py-3 px-5 rounded-xl border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 active:scale-[0.99] font-semibold text-sm transition flex items-center justify-center gap-1.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
          <span data-i18n="schemaBtnPreviewSheet">Blatt-Vorschau</span>
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
            <span data-i18n="sheetBtnEdit">Bearbeiten</span>
          </button>

          <button onclick="printSheet()" class="px-3 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-700 text-white text-xs font-bold transition flex items-center gap-1.5 shadow-sm">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
            <span data-i18n="sheetBtnPrint">Drucken / PDF</span>
          </button>
        </div>

        <div class="flex items-center gap-1.5">
          <select id="font-style-select" onchange="changeSheetFont(this.value)" class="bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-lg px-2.5 py-1 text-xs text-slate-700 dark:text-slate-200 font-medium focus:outline-none">
            <option value="kalam-blue" selected data-i18n="sheetFontKalamBlue">Handschrift Blau</option>
            <option value="caveat-black" data-i18n="sheetFontCaveatBlack">Handschrift Schwarz</option>
            <option value="clean-sans" data-i18n="sheetFontCleanSans">Druckschrift</option>
          </select>

          <button type="button" id="btn-toggle-blank" onclick="toggleBlankMode()" class="px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 text-xs font-medium hover:bg-slate-100 dark:hover:bg-slate-800 transition">
            <span data-i18n="sheetBtnBlank">Vorlage</span>
          </button>
        </div>
      </div>

      <!-- THE SHEET -->
      <div class="w-full">
        <div id="worksheet-paper" class="sheet-paper w-full rounded-2xl p-4 sm:p-10 md:p-12 text-slate-900 dark:text-slate-100 font-sheet transition-all">

          <!-- Header Metadata -->
          <div id="sheet-header-meta" class="mb-5 pb-2 border-b border-slate-200 dark:border-slate-800 flex flex-wrap items-center justify-between text-xs text-slate-500 dark:text-slate-400 gap-1">
            <div class="flex items-center gap-1.5 font-medium">
              <span class="font-bold text-slate-900 dark:text-white uppercase tracking-wider text-[11px]" data-i18n="navSchema">Schema-Memo</span>
              <span id="sheet-meta-title" class="text-slate-800 dark:text-slate-200 font-semibold"></span>
            </div>
            <div id="sheet-meta-date" class="text-slate-500 dark:text-slate-400"></div>
          </div>

          <!-- SECTION 1 -->
          <div class="mb-6">
            <h2 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white mb-2.5" data-i18n="sheetSec1Title">
              1. Benennen des aktualisierten Gefühls
            </h2>

            <div class="mb-3">
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1" data-i18n="sheetSec1L1">
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
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1" data-i18n="sheetSec1L2">
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
            <h2 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white mb-2.5" data-i18n="sheetSec2Title">
              2. Erkennen der aktivierten Schemata/Modi und der Bewältigung
            </h2>

            <div class="mb-3">
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1" data-i18n="sheetSec2L1">
                Ich weiß, dass das wahrscheinlich mein (Schema/Modus) ... ist,
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-schema"></span>
              </div>
            </div>

            <div class="mb-3">
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1" data-i18n="sheetSec2L2">
                das/den ich durch (Kindheitssituation) ... erlernt habe.
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-childhood"></span>
              </div>
            </div>

            <div>
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1" data-i18n="sheetSec2L3">
                Diese Aktivierung löst bei mir (altes Bewältigungsverhalten) ... aus.
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-coping"></span>
              </div>
            </div>
          </div>

          <!-- SECTION 3 -->
          <div class="mb-6">
            <h2 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white mb-2.5" data-i18n="sheetSec3Title">
              3. Anerkennen der Dysfunktionalität / Realitätsprüfung
            </h2>

            <div class="mb-3">
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1" data-i18n="sheetSec3L1">
                Obwohl ich glaube (negativer Gedanke/ Innere-Eltern-Stimme),
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-thought"></span>
              </div>
            </div>

            <div class="mb-3">
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1" data-i18n="sheetSec3L2">
                ist die Realität (Sicht des Gesunden Erwachsenen),
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-reality"></span>
              </div>
            </div>

            <div>
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1" data-i18n="sheetSec3L3">
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
            <h2 class="text-sm sm:text-base font-bold text-slate-900 dark:text-white mb-2.5" data-i18n="sheetSec4Title">
              4. Trennen vom alten und Einbrennen des neuen Verhaltensimpulses
            </h2>

            <div class="mb-3">
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1" data-i18n="sheetSec4L1">
                Obwohl ich am liebsten (altes dysfunktionales Verhalten) ... würde,
              </div>
              <div class="dotted-rule">
                <span class="sheet-user-content sheet-val-l1" id="sheet-val-old-behavior"></span>
              </div>
            </div>

            <div>
              <div class="font-bold text-slate-800 dark:text-slate-200 text-xs sm:text-[14px] mb-1" data-i18n="sheetSec4L2">
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
          <div class="mt-8 pt-3 border-t border-slate-200 dark:border-slate-800 text-center text-[10px] text-slate-500 dark:text-slate-400" data-i18n="sheetCopyright">
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
            <h2 class="text-base sm:text-xl font-bold tracking-tight text-slate-900 dark:text-white" data-i18n="archiveTitle">Gespeicherte Schema-Memos</h2>
            <p class="text-xs text-slate-500 dark:text-slate-400" data-i18n="archiveSubtitle">Verwalte deine reflektierten Memos und verfolge deinen Therapiefortschritt.</p>
          </div>

          <div class="flex items-center gap-1.5">
            <button onclick="exportJSON()" class="px-2.5 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-xs font-semibold hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1">
              <span data-i18n="btnExport">Export</span>
            </button>
            <label class="px-2.5 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-xs font-semibold hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1 cursor-pointer">
              <span data-i18n="btnImport">Import</span>
              <input type="file" id="import-file" accept=".json" onchange="importJSON(event)" class="hidden">
            </label>
          </div>
        </div>

        <div class="pt-1">
          <input type="text" id="archive-search-input" oninput="renderArchiveList()" placeholder="Memos nach Titel, Situation oder Schema durchsuchen..." data-i18n-placeholder="archiveSearchPlaceholder" class="shadcn-input text-xs">
        </div>
      </div>

      <div id="archive-list-container" class="space-y-3">
        <!-- Rendered via JavaScript -->
      </div>
    </div>

    <!-- VIEW A4: SCHEMA SPICKZETTEL / HILFE -->
    <div id="view-help" class="hidden space-y-4">
      <div class="shadcn-card p-3 sm:p-5 space-y-2.5">
        <h2 class="text-base sm:text-xl font-bold tracking-tight text-slate-900 dark:text-white" data-i18n="helpTitle">Schema-Therapie Spickzettel</h2>
        <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed" data-i18n="helpSubtitle">
          Kompaktes Nachschlagewerk über die 18 Schemata und Modi nach Jeffrey Young zur schnellen Orientierung während der Reflexion.
        </p>
      </div>

      <!-- Schemata Accordions/Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div class="shadcn-card p-3 sm:p-4 space-y-1.5">
          <span class="text-xs font-bold text-sky-600 dark:text-sky-400 uppercase tracking-wider" data-i18n="helpDomain1Badge">Bereich 1</span>
          <h3 class="text-sm font-bold text-slate-900 dark:text-white" data-i18n="helpDomain1Title">Abweisung & Trennung</h3>
          <p class="text-xs text-slate-500 leading-relaxed" data-i18n="helpDomain1Desc">
            Verlassenheit / Instabilität, Misstrauen / Missbrauch, Emotionale Vernachlässigung, Unzulänglichkeit / Scham, Soziale Isolation.
          </p>
        </div>

        <div class="shadcn-card p-3 sm:p-4 space-y-1.5">
          <span class="text-xs font-bold text-indigo-600 dark:text-indigo-400 uppercase tracking-wider" data-i18n="helpDomain2Badge">Bereich 2</span>
          <h3 class="text-sm font-bold text-slate-900 dark:text-white" data-i18n="helpDomain2Title">Autonomie & Leistung</h3>
          <p class="text-xs text-slate-500 leading-relaxed" data-i18n="helpDomain2Desc">
            Abhängigkeit / Inkompetenz, Anfälligkeit für Verletzungen oder Krankheiten, Verstrickung / Unterentwickeltes Selbst, Versagen.
          </p>
        </div>

        <div class="shadcn-card p-3 sm:p-4 space-y-1.5">
          <span class="text-xs font-bold text-amber-600 dark:text-amber-400 uppercase tracking-wider" data-i18n="helpDomain3Badge">Bereich 3</span>
          <h3 class="text-sm font-bold text-slate-900 dark:text-white" data-i18n="helpDomain3Title">Beeinträchtigte Grenzen</h3>
          <p class="text-xs text-slate-500 leading-relaxed" data-i18n="helpDomain3Desc">
            Anspruchshaltung / Grandiosität, Ungenügende Selbstkontrolle / Selbstdisziplin.
          </p>
        </div>

        <div class="shadcn-card p-3 sm:p-4 space-y-1.5">
          <span class="text-xs font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-wider" data-i18n="helpDomain4Badge">Bereich 4</span>
          <h3 class="text-sm font-bold text-slate-900 dark:text-white" data-i18n="helpDomain4Title">Fremdbezogenheit</h3>
          <p class="text-xs text-slate-500 leading-relaxed" data-i18n="helpDomain4Desc">
            Unterwerfung, Aufopferung, Streben nach Anerkennung & Bestätigung.
          </p>
        </div>
      </div>
    </div>
'''
