# -*- coding: utf-8 -*-

def get_javascript_code():
    return r'''  <!-- Application Logic -->
  <script>
    // ==========================================
    // CONSTANTS & STATE MANAGEMENT
    // ==========================================
    const STORAGE_KEY_MEMOS = 'schema_therapy_memos_v1';
    const STORAGE_KEY_DIARY = 'schema_daily_diary_v1';
    const STORAGE_KEY_MODE = 'schema_app_active_mode';
    const STORAGE_KEY_SETTINGS = 'schema_settings_v1';

    // ==========================================
    // EMOJI PURGE & SANITIZATION ENGINE
    // Preserves ONLY mood/stimmung 1-10 faces: 😭 😞 😔 😕 😐 🙂 😊 😁 🥳 🌟
    // All other emojis are strictly purged across the entire app
    // ==========================================
    const MOOD_PERMITTED_EMOJIS = new Set(['😭', '😞', '😔', '😕', '😐', '🙂', '😊', '😁', '🥳', '🌟']);
    const NON_MOOD_EMOJI_REGEX = /[\u{1F000}-\u{1FAFF}\u{2300}-\u{23FF}\u{2600}-\u{27BF}\u{2B50}\u{FE00}-\u{FE0F}]/gu;

    function stripNonMoodEmojis(str) {
      if (!str || typeof str !== 'string') return str;
      return str.replace(NON_MOOD_EMOJI_REGEX, (m) => {
        return MOOD_PERMITTED_EMOJIS.has(m) ? m : '';
      }).replace(/\s+/g, ' ').trim();
    }

    function stripAllEmojis(str) {
      if (!str || typeof str !== 'string') return str;
      return str.replace(NON_MOOD_EMOJI_REGEX, '').replace(/\s+/g, ' ').trim();
    }

    const DEFAULT_SETTINGS = {
      language: 'de',      // 'de' | 'en'
      theme: 'auto',       // 'light' | 'dark' | 'auto'
      stepsGoal: 10000,
      waterGoal: 2500,
      compactMode: false,
      startView: 'schema', // 'schema' | 'diary'
      features: {
        'mood': true,
        'emotions': true,
        'meds-log': true,
        'meds-efficacy': true,
        'meals': true,
        'water': true,
        'caffeine': true,
        'sleep': true,
        'adhs': true,
        'steps': true,
        'positive-things': true,
        'highlights': true,
        'notes': true
      }
    };

    let appSettings = JSON.parse(JSON.stringify(DEFAULT_SETTINGS));

    const FEATURE_METADATA = [
      { id: 'mood', card: 'mood', icon: '', title_de: 'Gemüt & Energie', title_en: 'Mood & Energy', desc_de: '1-10 Skala für Stimmung & Energielevel', desc_en: '1-10 scale for mood & energy score' },
      { id: 'emotions', card: 'mood', icon: '', title_de: 'Gefühle & Reflexion', title_en: 'Emotions & Reflection', desc_de: 'Gefühls-Chips mit eigener Reflexions-Notiz', desc_en: 'Emotion chips with personal reflection notes' },
      { id: 'meds-log', card: 'meds', icon: '', title_de: 'Medikamente & Uhrzeit', title_en: 'Medications & Time', desc_de: '1-Klick Einnahme mit flexibler Zeiterfassung', desc_en: '1-click logging with flexible intake time' },
      { id: 'meds-efficacy', card: 'meds', icon: '', title_de: 'Wirkung & Rebound', title_en: 'Efficacy & Rebound', desc_de: 'Wirkungsbewertung (Flow, Optimal, ...) & Rebound', desc_en: 'Efficacy rating (Flow, Optimal, ...) & Rebound' },
      { id: 'meals', card: 'vital', icon: '', title_de: 'Mahlzeiten (4 Phasen)', title_en: 'Meals (4 Phases)', desc_de: 'Frühstück, Mittag, Abend, Snacks & Tags', desc_en: 'Breakfast, Lunch, Dinner, Snacks & Tags' },
      { id: 'water', card: 'vital', icon: '', title_de: 'Wasser & Hydration', title_en: 'Water & Hydration', desc_de: 'Fortschrittsbalken mit +250 / +500 ml Tasten', desc_en: 'Progress bar with +250 / +500 ml buttons' },
      { id: 'caffeine', card: 'vital', icon: '', title_de: 'Koffein & Wachmacher', title_en: 'Caffeine & Boosters', desc_de: 'Kaffee- & Energy-Zähler bzgl. Wechselwirkung', desc_en: 'Coffee & energy counter for interactions' },
      { id: 'sleep', card: 'vital', icon: '', title_de: 'Schlaf & Erholung', title_en: 'Sleep & Recovery', desc_de: 'Zeiten, Auto-Schlafdauer, Qualität & Faktoren', desc_en: 'Times, auto-duration, quality & factors' },
      { id: 'adhs', card: 'adhs', icon: '', title_de: 'ADHS, Fokus & Reize', title_en: 'ADHD, Focus & Sensory', desc_de: 'Fokus, Unruhe, Brainfog, Flow & Reizoffenheit', desc_en: 'Focus, restlessness, brain fog, flow & sensory load' },
      { id: 'steps', card: 'adhs', icon: '', title_de: 'Schritte & Sport', title_en: 'Steps & Activities', desc_de: 'Schrittzähler mit Zielbalken & Sport-Chips', desc_en: 'Step counter with goal bar & sport chips' },
      { id: 'positive-things', card: 'mind', icon: '', title_de: '3 Positive Dinge', title_en: '3 Positive Things', desc_de: 'Dankbarkeit & tägliche Dopamin-Anker', desc_en: 'Gratitude & daily dopamine anchors' },
      { id: 'highlights', card: 'mind', icon: '', title_de: 'Highlights & Erlebnisse', title_en: 'Highlights & Memories', desc_de: 'Schlüsselerlebnisse und Erinnerungs-Tags (#)', desc_en: 'Key moments and memory tags (#)' },
      { id: 'notes', card: 'mind', icon: '', title_de: 'Brain Dump / Notizen', title_en: 'Brain Dump / Notes', desc_de: 'Freies Textfeld für ungefilterte Gedanken', desc_en: 'Freeform text field for unfiltered thoughts' }
    ];

    const I18N = {
      de: {
        brandSubtitle: 'Nach J. Young · Schematherapie',
        diarySubtitle: 'All-in-One Life, Med & Neuro Tracker',
        navSchema: 'Schema-Memo',
        navDiary: 'Diary & Tracker',
        headerNewMemo: 'Memo',
        headerNewCheckin: 'Check-in',
        btnInstall: 'Installieren',
        tabEdit: 'Eingabe',
        tabSheet: 'Blatt',
        tabMemos: 'Memos',
        tabHelp: 'Hilfe',
        tabCheckin: 'Check-in',
        tabHistory: 'Chronik',
        tabTrends: 'Trends',
        quickYesterday: 'Vortag',
        quickReset: 'Leeren',
        quickCollapse: '⤓ Zuklappen',
        quickExpand: '⤢ Aufklappen',
        quickModules: 'Module',
        filterAll: 'Alles',
        filterMood: 'Mood',
        filterMeds: 'Medis',
        filterVital: 'Vitales',
        filterAdhs: 'ADHS & Steps',
        filterMind: 'Journal',
        saveEntry: 'Tages-Eintrag speichern',
        privacyNote: '100% lokal & privat auf diesem Gerät',
        allDisabledTitle: 'Alle Tracking-Module sind deaktiviert',
        allDisabledDesc: 'Du hast momentan alle Bereiche im Tagebuch ausgeblendet. Aktiviere Module in den Einstellungen, um loszulegen.',
        allDisabledBtn: 'Module anpassen',
        settingsHeading: 'Einstellungen & Module',
        settingsSubheading: 'Passe Module, Sprache und Darstellung an deine Bedürfnisse an.',
        tabLabelModules: 'Tracking-Module',
        tabLabelGeneral: 'Allgemein & Sprache',
        settingsPresetsTitle: 'Schnell-Vorlagen:',
        settingsPresetsDesc: 'Passe das Tagebuch so an, dass du dich nicht überfordert fühlst. Schalte nur die Bereiche ein, die du heute wirklich tracken möchtest.',
        presetAll: 'Alle an',
        presetMinimal: 'Nur Kern (Minimal)',
        presetMindfulness: 'Achtsamkeit',
        labelSettingLanguage: 'Sprache / Language:',
        labelSettingTheme: 'Erscheinungsbild:',
        themeLight: 'Hell',
        themeDark: 'Dunkel',
        themeAuto: 'System',
        labelSettingTargets: 'Tagesziele & Verhalten:',
        labelTargetSteps: 'Standard Schritte-Ziel:',
        labelTargetWater: 'Standard Wasser-Ziel (ml):',
        labelCompactMode: 'Karten beim Start standardmäßig zuklappen (Fokus-Modus)',
        labelStartView: 'Startansicht beim Öffnen:',
        labelSettingBackup: 'Gesamt-Backup & Datensicherung:',
        settingsBackupDesc: 'Erstelle ein Komplett-Backup aller Memos, Tagebuch-Tage und Einstellungen in einer einzigen sicheren Datei.',
        btnExportBackup: 'Gesamt-Backup laden',
        btnImportBackup: 'Backup einspielen',
        settingsDone: 'Fertig',
        toastSaved: 'Gespeichert',
        toastPresetApplied: 'Vorlage angewendet',
        toastBackupExported: 'Gesamt-Backup erfolgreich heruntergeladen!',
        toastBackupImported: 'Backup erfolgreich wiederhergestellt!',
        toastLanguageChanged: 'Sprache auf Deutsch gestellt',
        toastThemeChanged: 'Design angepasst'
      },
      en: {
        brandSubtitle: 'By J. Young · Schema Therapy',
        diarySubtitle: 'All-in-One Life, Med & Neuro Tracker',
        navSchema: 'Schema-Memo',
        navDiary: 'Diary & Tracker',
        headerNewMemo: 'Memo',
        headerNewCheckin: 'Check-in',
        btnInstall: 'Install',
        tabEdit: 'Form',
        tabSheet: 'Sheet',
        tabMemos: 'Memos',
        tabHelp: 'Help',
        tabCheckin: 'Check-in',
        tabHistory: 'History',
        tabTrends: 'Trends',
        quickYesterday: 'Yesterday',
        quickReset: 'Clear',
        quickCollapse: '⤓ Collapse',
        quickExpand: '⤢ Expand',
        quickModules: 'Modules',
        filterAll: 'All',
        filterMood: 'Mood',
        filterMeds: 'Meds',
        filterVital: 'Vitals',
        filterAdhs: 'ADHD & Steps',
        filterMind: 'Journal',
        saveEntry: 'Save Daily Entry',
        privacyNote: '100% local & private on this device',
        allDisabledTitle: 'All tracking modules are disabled',
        allDisabledDesc: 'You have currently hidden all diary sections. Enable modules in Settings to get started.',
        allDisabledBtn: 'Configure Modules',
        settingsHeading: 'Settings & Modules',
        settingsSubheading: 'Customize modules, language and appearance to your needs.',
        tabLabelModules: 'Tracking Modules',
        tabLabelGeneral: 'General & Language',
        settingsPresetsTitle: 'Quick Presets:',
        settingsPresetsDesc: 'Tailor your diary so you never feel overwhelmed. Toggle only the areas you really want to track today.',
        presetAll: 'All on',
        presetMinimal: 'Core Only (Minimal)',
        presetMindfulness: 'Mindfulness',
        labelSettingLanguage: 'Language / Sprache:',
        labelSettingTheme: 'Appearance:',
        themeLight: 'Light',
        themeDark: 'Dark',
        themeAuto: 'System',
        labelSettingTargets: 'Daily Goals & Behavior:',
        labelTargetSteps: 'Default Steps Goal:',
        labelTargetWater: 'Default Water Goal (ml):',
        labelCompactMode: 'Collapse cards by default at startup (Focus Mode)',
        labelStartView: 'Startup view on launch:',
        labelSettingBackup: 'Complete Backup & Safety:',
        settingsBackupDesc: 'Create a full backup of all memos, diary entries, and settings in a single safe file.',
        btnExportBackup: 'Export Full Backup',
        btnImportBackup: 'Restore Backup',
        settingsDone: 'Done',
        toastSaved: 'Saved',
        toastPresetApplied: 'Preset applied',
        toastBackupExported: 'Full backup exported successfully!',
        toastBackupImported: 'Backup restored successfully!',
        toastLanguageChanged: 'Language set to English',
        toastThemeChanged: 'Theme updated'
      }
    };

    let currentAppMode = 'schema'; // 'schema' | 'diary'
    let currentMemoId = null;
    let isBlankMode = false;
    let currentSheetFont = 'kalam-blue';

    // Diary State
    let currentDiaryEntryId = null;
    let activeStatsDays = 7;
    let activeDiaryFolder = 'all';
    let activeDiaryQuickFilter = 'all';

    let selectedDiaryEmotions = new Set();
    let diaryEmotionNotes = {};

    let currentDayMedications = [];
    let currentReboundLevel = 'none';

    let selectedMealTags = new Set();
    let currentWaterMl = 0;
    let currentWaterGoal = 2500;
    let currentCoffeeCups = 0;
    let currentEnergyCups = 0;
    let currentCaffeineCups = 0;

    let currentSleepQuality = 4;
    let selectedSleepTags = new Set();

    let selectedActivities = new Set();

    let currentExecutiveFunction = 'gut';
    let currentSensoryOverload = 'gering';

    let selectedMemoryTags = new Set();
    let currentMedEfficacyRating = '';

    // Accordion State for Diary Entry Cards
    let diaryCardsState = {
      mood: true,
      meds: true,
      vital: true,
      adhs: true,
      mind: true
    };
    let allCardsExpanded = true;

    // Custom Options Storage (Permanently saved user additions)
    const STORAGE_KEY_CUSTOM_OPTIONS = 'schema_custom_options_v1';
    let customOptions = {
      meds: [],          // [{ name: '...', dose: '...' }]
      emotions: [],      // ['...']
      sleep_factors: [], // ['...']
      activities: [],    // ['...']
      meal_tags: [],     // ['...']
      memory_tags: [],   // ['...']
      schema_emotions: [],
      schema_coping: [],
      schema_actions: []
    };

    const DEFAULT_MED_PRESETS = [
      { name: 'Elvanse Adult', dose: '30 mg' },
      { name: 'Elvanse Adult', dose: '50 mg' },
      { name: 'Elvanse Adult', dose: '70 mg' },
      { name: 'Medikinet adult', dose: '10 mg' },
      { name: 'Medikinet adult', dose: '20 mg' },
      { name: 'Ritalin adult', dose: '10 mg' },
      { name: 'Concerta', dose: '27 mg' },
      { name: 'Attentin', dose: '5 mg' },
      { name: 'Bupropion', dose: '150 mg' },
      { name: 'Magnesium', dose: '400 mg' },
      { name: 'Vitamin D3+K2', dose: '4000 IE' },
      { name: 'Omega 3', dose: '1000 mg' }
    ];

    const DEFAULT_SLEEP_FACTORS = [
      'Gedankenkreisen', 'Nachts wach', 'Melatonin', 'Zu spät ins Bett', 'Erholt', 'Träume'
    ];

    const DEFAULT_ACTIVITIES = [
      'Spaziergang', 'Gym', 'Laufen', 'Radfahren', 'Yoga', 'Ruhetag'
    ];

    const DEFAULT_MEAL_TAGS = [
      'Proteinreich', 'Ausgewogen', 'Leicht', 'Fast Food', 'Appetitmangel', 'Heißhunger'
    ];

    const DEFAULT_MEMORY_TAGS = [
      'Erfolg', 'Natur', 'Freunde', 'Familie', 'Kreativ', 'Dopamin-Win', 'Gelernt', 'Sport', 'Me-Time'
    ];


    // Mood Configurations (1 - 10)
    const MOOD_CONFIG = {
      1: { emoji: '😭', title: 'Krise / Akute Verzweiflung', desc: 'Extrem belastend, kaum aushaltbar. Bitte nimm dir Ruhe und suche Unterstützung.', bg: 'bg-rose-100 dark:bg-rose-950/80 text-rose-900 dark:text-rose-200 border border-rose-300 dark:border-rose-800' },
      2: { emoji: '😞', title: 'Sehr Niedergeschlagen / Erschöpft', desc: 'Schwere emotionale Last, Trauer oder massive Erschöpfung.', bg: 'bg-rose-50 dark:bg-rose-950/50 text-rose-800 dark:text-rose-300 border border-rose-200 dark:border-rose-900' },
      3: { emoji: '😔', title: 'Gedrückt & Kraftlos', desc: 'Vieles fiel schwer, geringe Motivation oder anhaltende Sorgen.', bg: 'bg-amber-100 dark:bg-amber-950/80 text-amber-900 dark:text-amber-200 border border-amber-300 dark:border-amber-800' },
      4: { emoji: '😕', title: 'Eher Unzufrieden / Angespannt', desc: 'Ein fordernder Tag mit Frustrationen oder innerer Unruhe.', bg: 'bg-amber-50 dark:bg-amber-950/50 text-amber-800 dark:text-amber-300 border border-amber-200 dark:border-amber-900' },
      5: { emoji: '😐', title: 'Durchschnittlich / Neutral', desc: 'Weder besonders gut noch schlecht. Ein solider, normaler Alltag.', bg: 'bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 border border-slate-300 dark:border-slate-700' },
      6: { emoji: '🙂', title: 'Ganz Okay / Leicht Positiv', desc: 'Mehrheitlich in Ordnung mit ein paar angenehmen Momenten.', bg: 'bg-sky-50 dark:bg-sky-950/50 text-sky-800 dark:text-sky-300 border border-sky-200 dark:border-sky-900' },
      7: { emoji: '😊', title: 'Gut & Ausgeglichen', desc: 'Stabiler Tag mit positiver Grundstimmung und guter Energie.', bg: 'bg-emerald-50 dark:bg-emerald-950/50 text-emerald-800 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-900' },
      8: { emoji: '😁', title: 'Sehr Zufrieden & Produktiv', desc: 'Erfüllend, stabil und mit vielen bereichernden Momenten.', bg: 'bg-emerald-100 dark:bg-emerald-950/80 text-emerald-900 dark:text-emerald-200 border border-emerald-300 dark:border-emerald-800' },
      9: { emoji: '🥳', title: 'Großartig & Voller Tatendrang', desc: 'Hervorragende Stimmung, starke Verbindung zu dir selbst oder anderen.', bg: 'bg-teal-100 dark:bg-teal-950/80 text-teal-900 dark:text-teal-200 border border-teal-300 dark:border-teal-800' },
      10: { emoji: '🌟', title: 'Herausragend / Flow-Erlebnis', desc: 'Ein absoluter Highlight-Tag voller Freude, Dankbarkeit und Klarheit.', bg: 'bg-amber-100 dark:bg-amber-900/40 text-amber-900 dark:text-amber-200 border border-amber-300 dark:border-amber-700' }
    };

    const PLEASANT_EMOTIONS = [
      'Freude', 'Dankbarkeit', 'Ruhe', 'Zufriedenheit', 'Energie', 
      'Stolz', 'Hoffnung', 'Erleichterung', 'Liebe', 'Gelassenheit', 
      'Verbundenheit', 'Zuversicht', 'Fokus'
    ];

    const CHALLENGING_EMOTIONS = [
      'Überforderung', 'Erschöpfung', 'Angst', 'Wut', 'Trauer', 
      'Frustration', 'Einsamkeit', 'Unruhe', 'Zweifel', 'Schuld', 
      'Scham', 'Stress', 'Reizüberflutung'
    ];

    // ==========================================
    // INITIALIZATION
    // ==========================================
    document.addEventListener('DOMContentLoaded', () => {
      loadAppSettings();
      initTheme();
      initDefaultDates();
      // Auto-migrate legacy data in client localStorage to strip obsolete emojis
      try {
        const rawD = localStorage.getItem(STORAGE_KEY_DIARY);
        if (rawD) {
          const pD = JSON.parse(rawD);
          if (Array.isArray(pD)) localStorage.setItem(STORAGE_KEY_DIARY, JSON.stringify(pD.map(sanitizeDiaryEntry)));
        }
        const rawM = localStorage.getItem(STORAGE_KEY_MEMOS);
        if (rawM) {
          const pM = JSON.parse(rawM);
          if (Array.isArray(pM)) localStorage.setItem(STORAGE_KEY_MEMOS, JSON.stringify(pM.map(sanitizeMemoEntry)));
        }
      } catch (e) {}

      ensureInitialMemos();
      ensureInitialDiary();
      loadCustomOptions();
      renderQuickMedsChips();
      renderEmotionChips();
      renderSleepTagChips();
      renderActivitiesChips();
      renderMealTagChips();
      renderMemoryTagChips();
      renderSchemaCustomChips();
      updateCardSummaryBadges();
      applyDiaryFeatureVisibility();
      
      const savedMode = localStorage.getItem(STORAGE_KEY_MODE) || (appSettings.startView || 'schema');
      switchAppMode(savedMode, false);

      if (appSettings.compactMode) {
        ['mood', 'meds', 'vital', 'adhs', 'mind'].forEach(k => {
          diaryCardsState[k] = false;
          applyDiaryCardVisibility(k);
        });
        allCardsExpanded = false;
        const lbl = document.getElementById('label-toggle-all-cards');
        const isDe = (appSettings.language || 'de') === 'de';
        if (lbl) lbl.textContent = isDe ? '⤢ Aufklappen' : '⤢ Expand';
      }

      renderArchiveList();
      renderDiaryEntriesList();
      registerServiceWorker();

      window.addEventListener('resize', () => {
        if (currentView === 'diary-stats') {
          renderStatsView();
        }
      });
    });

    // Theme Management
    function initTheme() {
      if (appSettings && appSettings.theme && appSettings.theme !== 'auto') {
        setAppThemeSetting(appSettings.theme);
        return;
      }
      if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
        document.getElementById('theme-icon-sun')?.classList.remove('hidden');
        document.getElementById('theme-icon-moon')?.classList.add('hidden');
      } else {
        document.documentElement.classList.remove('dark');
        document.getElementById('theme-icon-sun')?.classList.add('hidden');
        document.getElementById('theme-icon-moon')?.classList.remove('hidden');
      }
    }

    function toggleTheme() {
      if (document.documentElement.classList.contains('dark')) {
        setAppThemeSetting('light');
      } else {
        setAppThemeSetting('dark');
      }
    }

    function initDefaultDates() {
      const today = new Date().toISOString().split('T')[0];
      const dateEl = document.getElementById('input-date');
      if (dateEl && !dateEl.value) dateEl.value = today;

      const diaryDateEl = document.getElementById('input-diary-date');
      if (diaryDateEl && !diaryDateEl.value) {
        diaryDateEl.value = today;
        updateDiaryDateDisplay();
      }
    }

    // ==========================================
    // PRIMARY MODE SWITCHER
    // ==========================================
    function switchAppMode(mode, doScroll = true) {
      currentAppMode = mode;
      localStorage.setItem(STORAGE_KEY_MODE, mode);

      const btnSchema = document.getElementById('mode-btn-schema');
      const btnDiary = document.getElementById('mode-btn-diary');
      const titleEl = document.getElementById('app-main-title');
      const subTitleEl = document.getElementById('app-main-subtitle');
      const headerNewBtnText = document.getElementById('header-btn-new-text');
      const logoIcon = document.getElementById('brand-logo-icon');

      const isDe = (appSettings.language || 'de') === 'de';
      const t = I18N[appSettings.language || 'de'] || I18N.de;

      if (mode === 'schema') {
        btnSchema.className = 'flex-1 py-1.5 px-3 rounded-lg text-xs font-bold transition flex items-center justify-center gap-1.5 shadow-sm bg-white dark:bg-slate-900 text-sky-700 dark:text-sky-300';
        btnDiary.className = 'flex-1 py-1.5 px-3 rounded-lg text-xs font-semibold transition flex items-center justify-center gap-1.5 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white';
        titleEl.innerText = 'Schema-Memo';
        subTitleEl.innerText = t.brandSubtitle;
        headerNewBtnText.innerText = t.headerNewMemo;
        logoIcon.className = 'w-8 h-8 rounded-xl bg-gradient-to-tr from-sky-600 to-indigo-600 text-white flex items-center justify-center font-bold shadow-md shadow-sky-500/20';

        renderBottomNavForSchema();
        switchView('edit');
      } else {
        btnDiary.className = 'flex-1 py-1.5 px-3 rounded-lg text-xs font-bold transition flex items-center justify-center gap-1.5 shadow-sm bg-white dark:bg-slate-900 text-emerald-700 dark:text-emerald-300';
        btnSchema.className = 'flex-1 py-1.5 px-3 rounded-lg text-xs font-semibold transition flex items-center justify-center gap-1.5 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white';
        titleEl.innerText = 'Daily Diary & Neuro';
        subTitleEl.innerText = t.diarySubtitle;
        headerNewBtnText.innerText = t.headerNewCheckin;
        logoIcon.className = 'w-8 h-8 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-600 text-white flex items-center justify-center font-bold shadow-md shadow-emerald-500/20';

        renderBottomNavForDiary();
        switchView('diary-entry');
      }

      if (doScroll) window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function handleBrandClick() {
      if (currentAppMode === 'schema') switchView('edit');
      else switchView('diary-entry');
    }

    function handleHeaderNewClick() {
      if (currentAppMode === 'schema') createNewMemo();
      else createNewDiaryEntry();
    }

    // Dynamic Bottom Nav
    function renderBottomNavForSchema() {
      const nav = document.getElementById('app-bottom-nav');
      if (!nav) return;
      const memos = getStoredMemos();
      const t = I18N[appSettings.language || 'de'] || I18N.de;
      nav.innerHTML = `
        <button id="nav-btn-edit" type="button" onclick="switchView('edit')" class="bottom-nav-btn active flex-1 py-1.5 flex flex-col items-center justify-center text-slate-500 dark:text-slate-400 transition">
          <div class="nav-icon-wrapper w-9 h-7 rounded-full flex items-center justify-center transition mb-0.5">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
          </div>
          <span class="text-[11px] font-semibold tracking-tight">${t.tabEdit}</span>
        </button>

        <button id="nav-btn-sheet" type="button" onclick="switchView('sheet')" class="bottom-nav-btn flex-1 py-1.5 flex flex-col items-center justify-center text-slate-500 dark:text-slate-400 transition">
          <div class="nav-icon-wrapper w-9 h-7 rounded-full flex items-center justify-center transition mb-0.5">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
          </div>
          <span class="text-[11px] font-semibold tracking-tight">${t.tabSheet}</span>
        </button>

        <button id="nav-btn-archive" type="button" onclick="switchView('archive')" class="bottom-nav-btn flex-1 py-1.5 flex flex-col items-center justify-center text-slate-500 dark:text-slate-400 transition relative">
          <div class="nav-icon-wrapper w-9 h-7 rounded-full flex items-center justify-center transition mb-0.5 relative">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
            <span id="archive-count-badge" class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-sky-600 text-white text-[9px] font-bold flex items-center justify-center">${memos.length}</span>
          </div>
          <span class="text-[11px] font-semibold tracking-tight">${t.tabMemos}</span>
        </button>

        <button id="nav-btn-help" type="button" onclick="switchView('help')" class="bottom-nav-btn flex-1 py-1.5 flex flex-col items-center justify-center text-slate-500 dark:text-slate-400 transition">
          <div class="nav-icon-wrapper w-9 h-7 rounded-full flex items-center justify-center transition mb-0.5">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          </div>
          <span class="text-[11px] font-semibold tracking-tight">${t.tabHelp}</span>
        </button>
      `;
    }

    function renderBottomNavForDiary() {
      const nav = document.getElementById('app-bottom-nav');
      if (!nav) return;
      const diary = getStoredDiaryEntries();
      const t = I18N[appSettings.language || 'de'] || I18N.de;
      nav.innerHTML = `
        <button id="nav-btn-diary-entry" type="button" onclick="switchView('diary-entry')" class="bottom-nav-btn active flex-1 py-1.5 flex flex-col items-center justify-center text-slate-500 dark:text-slate-400 transition">
          <div class="nav-icon-wrapper w-9 h-7 rounded-full flex items-center justify-center transition mb-0.5">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          </div>
          <span class="text-[11px] font-semibold tracking-tight">${t.tabCheckin}</span>
        </button>

        <button id="nav-btn-diary-list" type="button" onclick="switchView('diary-list')" class="bottom-nav-btn flex-1 py-1.5 flex flex-col items-center justify-center text-slate-500 dark:text-slate-400 transition relative">
          <div class="nav-icon-wrapper w-9 h-7 rounded-full flex items-center justify-center transition mb-0.5 relative">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
            <span id="diary-count-badge" class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-emerald-600 text-white text-[9px] font-bold flex items-center justify-center">${diary.length}</span>
          </div>
          <span class="text-[11px] font-semibold tracking-tight">${t.tabHistory}</span>
        </button>

        <button id="nav-btn-diary-stats" type="button" onclick="switchView('diary-stats')" class="bottom-nav-btn flex-1 py-1.5 flex flex-col items-center justify-center text-slate-500 dark:text-slate-400 transition">
          <div class="nav-icon-wrapper w-9 h-7 rounded-full flex items-center justify-center transition mb-0.5">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
          </div>
          <span class="text-[11px] font-semibold tracking-tight">${t.tabTrends}</span>
        </button>
      `;
    }

    // ==========================================
    // APP SETTINGS & MODULAR FEATURE CONTROLLER
    // ==========================================
    function loadAppSettings() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY_SETTINGS);
        if (raw) {
          const parsed = JSON.parse(raw);
          appSettings = {
            ...DEFAULT_SETTINGS,
            ...parsed,
            features: {
              ...DEFAULT_SETTINGS.features,
              ...(parsed.features || {})
            }
          };
        }
      } catch (e) {
        console.error('Error loading settings:', e);
        appSettings = JSON.parse(JSON.stringify(DEFAULT_SETTINGS));
      }

      // Sync water and steps goals
      if (appSettings.waterGoal) {
        currentWaterGoal = appSettings.waterGoal;
        const waterDisp = document.getElementById('water-display');
        if (waterDisp) updateWaterDisplay();
      }
      if (appSettings.stepsGoal) {
        const inputGoal = document.getElementById('input-steps-goal');
        if (inputGoal) inputGoal.value = appSettings.stepsGoal;
        const setStepsGoal = document.getElementById('setting-steps-goal');
        if (setStepsGoal) setStepsGoal.value = appSettings.stepsGoal;
      }
      const setWaterGoal = document.getElementById('setting-water-goal');
      if (setWaterGoal) setWaterGoal.value = appSettings.waterGoal;

      const setCompact = document.getElementById('setting-compact-mode');
      if (setCompact) setCompact.checked = !!appSettings.compactMode;

      const setStart = document.getElementById('setting-start-view');
      if (setStart) setStart.value = appSettings.startView || 'schema';

      // Apply theme setting buttons
      updateThemeButtonsUI(appSettings.theme || 'auto');

      // Apply Language
      applyLanguageStrings();
    }

    function saveAppSettings() {
      try {
        localStorage.setItem(STORAGE_KEY_SETTINGS, JSON.stringify(appSettings));
      } catch (e) {
        console.error('Error saving settings:', e);
      }
    }

    function applyLanguageStrings() {
      const lang = appSettings.language || 'de';
      const t = I18N[lang] || I18N.de;

      const safeSetText = (id, text) => {
        const el = document.getElementById(id);
        if (el) el.textContent = text;
      };

      safeSetText('settings-modal-heading', t.settingsHeading);
      safeSetText('settings-modal-subheading', t.settingsSubheading);
      safeSetText('tab-label-modules', t.tabLabelModules);
      safeSetText('tab-label-general', t.tabLabelGeneral);
      safeSetText('settings-presets-title', t.settingsPresetsTitle);
      safeSetText('settings-presets-desc', t.settingsPresetsDesc);
      safeSetText('label-setting-language', t.labelSettingLanguage);
      safeSetText('label-setting-theme', t.labelSettingTheme);
      safeSetText('label-setting-targets', t.labelSettingTargets);
      safeSetText('label-target-steps', t.labelTargetSteps);
      safeSetText('label-target-water', t.labelTargetWater);
      safeSetText('label-compact-mode', t.labelCompactMode);
      safeSetText('label-start-view', t.labelStartView);
      safeSetText('label-setting-backup', t.labelSettingBackup);
      safeSetText('settings-backup-desc', t.settingsBackupDesc);
      safeSetText('btn-export-backup-text', t.btnExportBackup);
      safeSetText('btn-import-backup-text', t.btnImportBackup);
      safeSetText('settings-footer-privacy', t.privacyNote);
      safeSetText('settings-btn-done', t.settingsDone);
      safeSetText('label-quick-modules', t.quickModules);
      safeSetText('sec-nav-all', t.filterAll);
      safeSetText('sec-nav-mood', t.filterMood);
      safeSetText('sec-nav-meds', t.filterMeds);
      safeSetText('sec-nav-vital', t.filterVital);
      safeSetText('sec-nav-adhs', t.filterAdhs);
      safeSetText('sec-nav-mind', t.filterMind);
      safeSetText('all-disabled-title', t.allDisabledTitle);
      safeSetText('all-disabled-desc', t.allDisabledDesc);
      safeSetText('all-disabled-btn', t.allDisabledBtn);
      safeSetText('label-fallback-save-btn', t.saveEntry);

      // Accordion toggle label
      const toggleAllLbl = document.getElementById('label-toggle-all-cards');
      if (toggleAllLbl) toggleAllLbl.textContent = allCardsExpanded ? t.quickCollapse : t.quickExpand;

      // Update Language badge and button active states
      const langBadge = document.getElementById('current-lang-badge');
      if (langBadge) langBadge.textContent = lang === 'de' ? 'Deutsch' : 'English';

      const btnDe = document.getElementById('lang-btn-de');
      const btnEn = document.getElementById('lang-btn-en');
      if (btnDe && btnEn) {
        if (lang === 'de') {
          btnDe.className = 'py-2 px-3 rounded-xl border border-sky-500 bg-sky-50 dark:bg-sky-950/60 text-sky-800 dark:text-sky-300 font-bold text-xs flex items-center justify-center gap-1.5 transition shadow-xs';
          btnEn.className = 'py-2 px-3 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:text-slate-900 font-semibold text-xs flex items-center justify-center gap-1.5 transition';
        } else {
          btnEn.className = 'py-2 px-3 rounded-xl border border-sky-500 bg-sky-50 dark:bg-sky-950/60 text-sky-800 dark:text-sky-300 font-bold text-xs flex items-center justify-center gap-1.5 transition shadow-xs';
          btnDe.className = 'py-2 px-3 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:text-slate-900 font-semibold text-xs flex items-center justify-center gap-1.5 transition';
        }
      }

      // Re-render Bottom Nav & Settings Toggles with correct language
      if (currentAppMode === 'schema') renderBottomNavForSchema();
      else renderBottomNavForDiary();
      renderSettingsFeatureToggles();
    }

    function setAppLanguage(lang) {
      appSettings.language = lang;
      saveAppSettings();
      applyLanguageStrings();
      updateCardSummaryBadges();
      showToast(lang === 'de' ? 'Sprache auf Deutsch gestellt' : 'Language set to English');
    }

    function setAppThemeSetting(theme) {
      appSettings.theme = theme;
      saveAppSettings();
      updateThemeButtonsUI(theme);

      if (theme === 'light') {
        document.documentElement.classList.remove('dark');
        localStorage.theme = 'light';
        document.getElementById('theme-icon-sun')?.classList.add('hidden');
        document.getElementById('theme-icon-moon')?.classList.remove('hidden');
      } else if (theme === 'dark') {
        document.documentElement.classList.add('dark');
        localStorage.theme = 'dark';
        document.getElementById('theme-icon-sun')?.classList.remove('hidden');
        document.getElementById('theme-icon-moon')?.classList.add('hidden');
      } else { // auto
        delete localStorage.theme;
        if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
          document.documentElement.classList.add('dark');
          document.getElementById('theme-icon-sun')?.classList.remove('hidden');
          document.getElementById('theme-icon-moon')?.classList.add('hidden');
        } else {
          document.documentElement.classList.remove('dark');
          document.getElementById('theme-icon-sun')?.classList.add('hidden');
          document.getElementById('theme-icon-moon')?.classList.remove('hidden');
        }
      }
      showToast(appSettings.language === 'en' ? 'Theme updated' : 'Design angepasst');
    }

    function updateThemeButtonsUI(activeTheme) {
      const opts = ['light', 'dark', 'auto'];
      opts.forEach(opt => {
        const el = document.getElementById(`theme-opt-${opt}`);
        if (!el) return;
        if (opt === activeTheme) {
          el.className = 'theme-choice-btn active py-2 px-2 rounded-xl border border-sky-500 bg-sky-50 dark:bg-sky-950/60 text-xs font-bold text-sky-800 dark:text-sky-300 text-center transition flex flex-col items-center gap-0.5 shadow-xs';
        } else {
          el.className = 'theme-choice-btn py-2 px-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white text-center transition flex flex-col items-center gap-0.5';
        }
      });
    }

    function updateGoalSettings() {
      const stepsInput = document.getElementById('setting-steps-goal');
      const waterInput = document.getElementById('setting-water-goal');
      const compactInput = document.getElementById('setting-compact-mode');
      const startInput = document.getElementById('setting-start-view');

      if (stepsInput && stepsInput.value) {
        const val = parseInt(stepsInput.value, 10);
        if (val > 0) {
          appSettings.stepsGoal = val;
          const inputStepsGoal = document.getElementById('input-steps-goal');
          if (inputStepsGoal) inputStepsGoal.value = val;
          updateStepsProgressDisplay();
        }
      }

      if (waterInput && waterInput.value) {
        const val = parseInt(waterInput.value, 10);
        if (val > 0) {
          appSettings.waterGoal = val;
          currentWaterGoal = val;
          updateWaterDisplay();
        }
      }

      if (compactInput) {
        appSettings.compactMode = compactInput.checked;
      }

      if (startInput) {
        appSettings.startView = startInput.value;
      }

      saveAppSettings();
    }

    function applyDiaryFeatureVisibility() {
      let activeCount = 0;
      const cardCounts = {
        mood: 0,
        meds: 0,
        vital: 0,
        adhs: 0,
        mind: 0
      };

      FEATURE_METADATA.forEach(feat => {
        const isEnabled = appSettings.features[feat.id] !== false;
        if (isEnabled) {
          activeCount++;
          if (cardCounts[feat.card] !== undefined) cardCounts[feat.card]++;
        }
        const container = document.getElementById('feature-container-' + feat.id);
        if (container) {
          if (isEnabled) container.classList.remove('hidden');
          else container.classList.add('hidden');
        }
      });

      // Update badge in settings modal
      const badge = document.getElementById('settings-active-count-badge');
      if (badge) {
        const isDe = (appSettings.language || 'de') === 'de';
        badge.textContent = `${activeCount} ${isDe ? 'aktiv' : 'active'}`;
      }

      // Handle drinks row (water + caffeine)
      const drinksRow = document.getElementById('vital-drinks-row');
      const isWater = appSettings.features['water'] !== false;
      const isCaff = appSettings.features['caffeine'] !== false;
      if (drinksRow) {
        if (!isWater && !isCaff) {
          drinksRow.classList.add('hidden');
        } else {
          drinksRow.classList.remove('hidden');
        }
      }

      // Check card containers and their navigation pills
      let visibleCardsCount = 0;
      ['mood', 'meds', 'vital', 'adhs', 'mind'].forEach(cardKey => {
        const cardEl = document.getElementById('card-diary-' + cardKey);
        const navPill = document.getElementById('sec-nav-' + cardKey);
        const isCardVisible = cardCounts[cardKey] > 0;

        if (cardEl) {
          if (isCardVisible) {
            cardEl.classList.remove('hidden');
            visibleCardsCount++;
          } else {
            cardEl.classList.add('hidden');
          }
        }
        if (navPill) {
          if (isCardVisible) navPill.classList.remove('hidden');
          else navPill.classList.add('hidden');
        }
      });

      // Fallback save bar & All-disabled notice
      const notice = document.getElementById('diary-all-disabled-notice');
      const fallbackSave = document.getElementById('diary-fallback-save-bar');
      const secNavAll = document.getElementById('sec-nav-all');

      if (visibleCardsCount === 0) {
        if (notice) notice.classList.remove('hidden');
        if (fallbackSave) fallbackSave.classList.add('hidden');
        if (secNavAll) secNavAll.classList.add('hidden');
      } else {
        if (notice) notice.classList.add('hidden');
        if (secNavAll) secNavAll.classList.remove('hidden');

        // If Card 5 (mind) is hidden, show fallback save bar so user can still save
        const isMindVisible = cardCounts['mind'] > 0;
        if (!isMindVisible && fallbackSave) {
          fallbackSave.classList.remove('hidden');
        } else if (fallbackSave) {
          fallbackSave.classList.add('hidden');
        }
      }
    }

    function renderSettingsFeatureToggles() {
      const container = document.getElementById('settings-feature-toggles-container');
      if (!container) return;

      const lang = appSettings.language || 'de';
      const isDe = lang === 'de';

      const cardTitles = {
        mood: isDe ? 'Gemüt & Gefühle' : 'Mood & Emotions',
        meds: isDe ? 'Medikation & Wirkung' : 'Medications & Efficacy',
        vital: isDe ? 'Vital-Hub (Essen, Trinken, Schlaf)' : 'Vitals (Meals, Drinks, Sleep)',
        adhs: isDe ? 'Neuro & Body (ADHS, Schritte)' : 'Neuro & Body (ADHD, Steps)',
        mind: isDe ? 'Journal & Reflexion' : 'Journal & Reflection'
      };

      let html = '';
      const grouped = {};
      FEATURE_METADATA.forEach(feat => {
        if (!grouped[feat.card]) grouped[feat.card] = [];
        grouped[feat.card].push(feat);
      });

      Object.keys(grouped).forEach(cardKey => {
        html += `
          <div class="rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/40 p-2.5 space-y-2">
            <span class="text-[10px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 block pb-1 border-b border-slate-200/50 dark:border-slate-800">
              ${cardTitles[cardKey] || cardKey}
            </span>
            <div class="space-y-1.5">
        `;

        grouped[cardKey].forEach(feat => {
          const isChecked = appSettings.features[feat.id] !== false;
          const title = isDe ? feat.title_de : feat.title_en;
          const desc = isDe ? feat.desc_de : feat.desc_en;

          html += `
            <label class="flex items-center justify-between p-2 rounded-xl bg-white dark:bg-slate-800 border border-slate-200/70 dark:border-slate-700/80 hover:border-slate-300 dark:hover:border-slate-600 transition cursor-pointer gap-2">
              <div class="flex items-center gap-2 min-w-0">
                <div class="min-w-0">
                  <div class="text-xs font-bold text-slate-800 dark:text-slate-200 truncate leading-tight">${title}</div>
                  <div class="text-[10px] text-slate-400 truncate leading-tight">${desc}</div>
                </div>
              </div>
              
              <div class="relative inline-flex items-center shrink-0">
                <input type="checkbox" onchange="toggleFeatureSetting('${feat.id}', this.checked)" ${isChecked ? 'checked' : ''} class="sr-only peer">
                <div class="w-9 h-5 bg-slate-300 dark:bg-slate-700 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-emerald-600"></div>
              </div>
            </label>
          `;
        });

        html += `
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function toggleFeatureSetting(featId, isChecked) {
      if (!appSettings.features) appSettings.features = {};
      appSettings.features[featId] = isChecked;
      saveAppSettings();
      applyDiaryFeatureVisibility();
    }

    function setFeaturePreset(presetType) {
      if (!appSettings.features) appSettings.features = {};
      
      if (presetType === 'all') {
        FEATURE_METADATA.forEach(f => {
          appSettings.features[f.id] = true;
        });
      } else if (presetType === 'minimal') {
        const core = new Set(['mood', 'meds-log', 'meds-efficacy', 'water', 'sleep', 'adhs', 'positive-things']);
        FEATURE_METADATA.forEach(f => {
          appSettings.features[f.id] = core.has(f.id);
        });
      } else if (presetType === 'mindfulness') {
        const mindful = new Set(['mood', 'emotions', 'meals', 'water', 'sleep', 'steps', 'positive-things', 'highlights', 'notes']);
        FEATURE_METADATA.forEach(f => {
          appSettings.features[f.id] = mindful.has(f.id);
        });
      }

      saveAppSettings();
      renderSettingsFeatureToggles();
      applyDiaryFeatureVisibility();
      const isDe = (appSettings.language || 'de') === 'de';
      showToast(isDe ? 'Vorlage übernommen' : 'Preset applied');
    }

    function switchSettingsTab(tab) {
      const tabModules = document.getElementById('settings-tab-modules');
      const tabGeneral = document.getElementById('settings-tab-general');
      const btnModules = document.getElementById('tab-btn-modules');
      const btnGeneral = document.getElementById('tab-btn-general');

      if (!tabModules || !tabGeneral) return;

      if (tab === 'modules') {
        tabModules.classList.remove('hidden');
        tabGeneral.classList.add('hidden');
        btnModules.className = 'py-1.5 px-3 rounded-lg transition text-center shadow-xs bg-white dark:bg-slate-900 text-sky-700 dark:text-sky-300 font-bold';
        btnGeneral.className = 'py-1.5 px-3 rounded-lg transition text-center text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white font-medium';
      } else {
        tabModules.classList.add('hidden');
        tabGeneral.classList.remove('hidden');
        btnGeneral.className = 'py-1.5 px-3 rounded-lg transition text-center shadow-xs bg-white dark:bg-slate-900 text-sky-700 dark:text-sky-300 font-bold';
        btnModules.className = 'py-1.5 px-3 rounded-lg transition text-center text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white font-medium';

        updateSettingsDataStats();
      }
    }

    function openSettingsModal() {
      const modal = document.getElementById('settings-modal');
      if (!modal) return;
      renderSettingsFeatureToggles();
      updateSettingsDataStats();
      modal.classList.remove('hidden');
    }

    function closeSettingsModal() {
      const modal = document.getElementById('settings-modal');
      if (modal) modal.classList.add('hidden');
    }

    function updateSettingsDataStats() {
      const statsEl = document.getElementById('settings-data-stats');
      if (!statsEl) return;
      const memos = getStoredMemos();
      const diary = getStoredDiaryEntries();
      const isDe = (appSettings.language || 'de') === 'de';
      statsEl.textContent = isDe 
        ? `${memos.length} Memos · ${diary.length} Einträge`
        : `${memos.length} Memos · ${diary.length} Entries`;
    }

    function exportFullBackupJSON() {
      const backupData = {
        app: 'Schema-Memo & Daily Life Tracker',
        version: 1,
        exportedAt: new Date().toISOString(),
        memos: getStoredMemos(),
        diary: getStoredDiaryEntries(),
        customOptions: customOptions,
        settings: appSettings
      };

      const jsonStr = JSON.stringify(backupData, null, 2);
      const blob = new Blob([jsonStr], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      const dateStr = new Date().toISOString().split('T')[0];
      a.href = url;
      a.download = `schema-memo-full-backup-${dateStr}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);

      const isDe = (appSettings.language || 'de') === 'de';
      showToast(isDe ? 'Gesamt-Backup erfolgreich exportiert!' : 'Full backup exported successfully!');
    }

    function importFullBackupJSON(event) {
      const file = event.target.files && event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const data = JSON.parse(e.target.result);
          if (!data || typeof data !== 'object') {
            throw new Error('Ungültiges Datenformat');
          }

          if (Array.isArray(data.memos)) {
            localStorage.setItem(STORAGE_KEY_MEMOS, JSON.stringify(data.memos));
          }
          if (Array.isArray(data.diary)) {
            localStorage.setItem(STORAGE_KEY_DIARY, JSON.stringify(data.diary));
          }
          if (data.customOptions && typeof data.customOptions === 'object') {
            localStorage.setItem(STORAGE_KEY_CUSTOM_OPTIONS, JSON.stringify(data.customOptions));
            customOptions = data.customOptions;
          }
          if (data.settings && typeof data.settings === 'object') {
            localStorage.setItem(STORAGE_KEY_SETTINGS, JSON.stringify(data.settings));
            appSettings = { ...DEFAULT_SETTINGS, ...data.settings };
          }

          loadAppSettings();
          loadCustomOptions();
          renderQuickMedsChips();
          renderEmotionChips();
          renderSleepTagChips();
          renderActivitiesChips();
          renderMealTagChips();
          renderMemoryTagChips();
          renderSchemaCustomChips();
          applyDiaryFeatureVisibility();
          renderArchiveList();
          renderDiaryEntriesList();
          if (currentDiaryEntryId) loadDiaryEntryForDate(document.getElementById('input-diary-date')?.value || getTodayDateString());

          const isDe = (appSettings.language || 'de') === 'de';
          showToast(isDe ? 'Backup erfolgreich wiederhergestellt!' : 'Backup restored successfully!');
          updateSettingsDataStats();
          closeSettingsModal();
        } catch (err) {
          console.error('Import error:', err);
          alert('Fehler beim Einlesen der Backup-Datei: ' + err.message);
        }
      };
      reader.readAsText(file);
      event.target.value = '';
    }

    function switchView(viewName) {
      const allViews = ['edit', 'sheet', 'archive', 'help', 'diary-entry', 'diary-list', 'diary-stats'];
      allViews.forEach(v => {
        const el = document.getElementById('view-' + v);
        const btn = document.getElementById('nav-btn-' + v);
        if (el) el.classList.add('hidden');
        if (btn) btn.classList.remove('active');
      });

      const activeEl = document.getElementById('view-' + viewName);
      const activeBtn = document.getElementById('nav-btn-' + viewName);
      if (activeEl) activeEl.classList.remove('hidden');
      if (activeBtn) activeBtn.classList.add('active');

      if (viewName === 'sheet') {
        populateSheetView();
      } else if (viewName === 'archive') {
        renderArchiveList();
      } else if (viewName === 'diary-list') {
        renderDiaryEntriesList();
      } else if (viewName === 'diary-stats') {
        renderStatsView();
      }

      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // ==========================================
    // MODULE A: SCHEMA-MEMO LOGIC
    // ==========================================
    function sanitizeMemoEntry(m) {
      if (!m || typeof m !== 'object') return m;
      return {
        ...m,
        emotion: stripAllEmojis(m.emotion || ''),
        situation: stripAllEmojis(m.situation || ''),
        schema: stripAllEmojis(m.schema || ''),
        mode: stripAllEmojis(m.mode || ''),
        coping: stripAllEmojis(m.coping || ''),
        healthyBelief: stripAllEmojis(m.healthyBelief || ''),
        newAction: stripAllEmojis(m.newAction || '')
      };
    }

    function getStoredMemos() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY_MEMOS);
        if (!raw) return [];
        const parsed = JSON.parse(raw);
        if (!Array.isArray(parsed)) return [];
        return parsed.map(sanitizeMemoEntry);
      } catch (e) {
        console.error(e);
        return [];
      }
    }

    function saveStoredMemos(memos) {
      const cleaned = (memos || []).map(sanitizeMemoEntry);
      localStorage.setItem(STORAGE_KEY_MEMOS, JSON.stringify(cleaned));
      const badge = document.getElementById('archive-count-badge');
      if (badge) badge.innerText = cleaned.length;
    }

    function ensureInitialMemos() {
      const memos = getStoredMemos();
      if (memos.length === 0) {
        loadExampleMemo(false);
        saveCurrentMemo(false);
      }
    }

    function createNewMemo() {
      currentMemoId = null;
      document.getElementById('input-title').value = '';
      initDefaultDates();
      document.getElementById('input-emotion').value = '';
      document.getElementById('input-situation').value = '';
      document.getElementById('input-schema').value = '';
      document.getElementById('input-childhood').value = '';
      document.getElementById('input-coping').value = '';
      document.getElementById('input-thought').value = '';
      document.getElementById('input-reality').value = '';
      document.getElementById('input-evidence').value = '';
      document.getElementById('input-old-behavior').value = '';
      document.getElementById('input-new-action').value = '';
      switchView('edit');
      showToast('Neues Schema-Memo angelegt');
    }

    function getFormData() {
      return {
        id: currentMemoId || ('memo_' + Date.now()),
        title: document.getElementById('input-title').value.trim() || 'Unbenanntes Schema-Memo',
        date: document.getElementById('input-date').value || new Date().toISOString().split('T')[0],
        updatedAt: new Date().toISOString(),
        emotion: document.getElementById('input-emotion').value.trim(),
        situation: document.getElementById('input-situation').value.trim(),
        schema: document.getElementById('input-schema').value.trim(),
        childhood: document.getElementById('input-childhood').value.trim(),
        coping: document.getElementById('input-coping').value.trim(),
        thought: document.getElementById('input-thought').value.trim(),
        reality: document.getElementById('input-reality').value.trim(),
        evidence: document.getElementById('input-evidence').value.trim(),
        oldBehavior: document.getElementById('input-old-behavior').value.trim(),
        newAction: document.getElementById('input-new-action').value.trim()
      };
    }

    function setFormData(data) {
      currentMemoId = data.id || null;
      document.getElementById('input-title').value = data.title || '';
      document.getElementById('input-date').value = data.date || new Date().toISOString().split('T')[0];
      document.getElementById('input-emotion').value = data.emotion || '';
      document.getElementById('input-situation').value = data.situation || '';
      document.getElementById('input-schema').value = data.schema || '';
      document.getElementById('input-childhood').value = data.childhood || '';
      document.getElementById('input-coping').value = data.coping || '';
      document.getElementById('input-thought').value = data.thought || '';
      document.getElementById('input-reality').value = data.reality || '';
      document.getElementById('input-evidence').value = data.evidence || '';
      document.getElementById('input-old-behavior').value = data.oldBehavior || '';
      document.getElementById('input-new-action').value = data.newAction || '';
    }

    function saveCurrentMemo(notify = true) {
      const data = getFormData();
      const memos = getStoredMemos();

      const existingIndex = memos.findIndex(m => m.id === data.id);
      if (existingIndex >= 0) memos[existingIndex] = data;
      else memos.unshift(data);

      saveStoredMemos(memos);
      currentMemoId = data.id;

      if (notify) {
        showToast('Schema-Memo gespeichert!');
        switchView('sheet');
      }
    }

    function previewCurrentSheet() {
      populateSheetView();
      switchView('sheet');
    }

    function resetFormWithConfirm() {
      if (confirm('Möchtest du alle Eingabefelder dieses Memos leeren?')) {
        createNewMemo();
      }
    }

    function appendTag(fieldId, text) {
      const field = document.getElementById(fieldId);
      if (!field) return;
      if (field.value.trim().length > 0) field.value += ', ' + text;
      else field.value = text;
      field.focus();
    }

    function setFieldValue(fieldId, text) {
      const field = document.getElementById(fieldId);
      if (field) {
        field.value = text;
        field.focus();
      }
    }

    function loadExampleMemo(notify = true) {
      const sample = {
        id: 'memo_example_sample',
        title: 'Kurz angebundene Antwort im Meeting',
        date: new Date().toISOString().split('T')[0],
        emotion: 'Tiefe Verunsicherung, Angst vor Zurückweisung, Anspannung im Brustbereich',
        situation: 'Mein Kollege hat mir auf eine Nachfrage nur knapp mit "Keine Zeit" geantwortet und sich abgewandt.',
        schema: 'Verlassenheit / Instabilität & Modus des verletzten Kindes',
        childhood: 'Frühere Erfahrungen, in denen Bezugspersonen bei Stress unvorhersehbar abweisend oder emotional unerreichbar waren.',
        coping: 'Innerer Rückzug, gekränktes Schweigen, Grübeln und Suche nach Fehlern bei mir selbst.',
        thought: 'Ich habe etwas falsch gemacht, er schätzt mich nicht mehr und ich werde bald ausgeschlossen.',
        reality: 'Eine knappe Antwort unter Zeitdruck ist kein Urteil über meinen Wert oder die Beziehung.',
        evidence: 'Er hat eine dringende Deadline heute um 14 Uhr. Gestern haben wir noch konstruktiv und freundlich zusammengearbeitet.',
        oldBehavior: 'Mich den ganzen Tag zurückziehen, passiv-aggressiv reagieren oder klammern.',
        newAction: 'Einmal tief durchatmen, mir sagen "Ich bin in Sicherheit und wertvoll", und ihm nach seiner Deadline ruhig einen Kaffee anbieten.'
      };
      setFormData(sample);
      if (notify) showToast('Beispiel-Memo geladen');
    }

    function populateSheetView() {
      const data = getFormData();
      document.getElementById('sheet-meta-title').innerText = isBlankMode ? 'Arbeitsblatt (Vorlage)' : (data.title || 'Unbenannt');
      document.getElementById('sheet-meta-date').innerText = isBlankMode ? 'Datum: ____________' : formatDateDE(data.date);

      const splitToLines = (text) => {
        if (!text) return { l1: '', l2: '' };
        if (text.length <= 60) return { l1: text, l2: '' };
        const mid = text.lastIndexOf(' ', 60);
        const splitIdx = mid > 20 ? mid : 60;
        return {
          l1: text.substring(0, splitIdx).trim(),
          l2: text.substring(splitIdx).trim()
        };
      };

      const setRuleContent = (id1, id2, text) => {
        const el1 = document.getElementById(id1);
        const el2 = document.getElementById(id2);
        if (isBlankMode) {
          if (el1) el1.innerText = '';
          if (el2) el2.innerText = '';
          return;
        }
        const splitted = splitToLines(text);
        if (el1) el1.innerText = splitted.l1;
        if (el2) el2.innerText = splitted.l2;
      };

      setRuleContent('sheet-val-emotion', 'sheet-val-emotion-extra', data.emotion);
      setRuleContent('sheet-val-situation', 'sheet-val-situation-extra', data.situation);
      setRuleContent('sheet-val-schema', null, data.schema);
      setRuleContent('sheet-val-childhood', null, data.childhood);
      setRuleContent('sheet-val-coping', null, data.coping);
      setRuleContent('sheet-val-thought', null, data.thought);
      setRuleContent('sheet-val-reality', null, data.reality);
      setRuleContent('sheet-val-evidence', 'sheet-val-evidence-extra', data.evidence);
      setRuleContent('sheet-val-old-behavior', null, data.oldBehavior);
      setRuleContent('sheet-val-new-action', 'sheet-val-new-action-extra', data.newAction);
    }

    function changeSheetFont(fontClass) {
      currentSheetFont = fontClass;
      const paper = document.getElementById('worksheet-paper');
      const spans = paper.querySelectorAll('.sheet-user-content');

      spans.forEach(span => {
        span.className = 'sheet-user-content';
        if (fontClass === 'kalam-blue') {
          span.classList.add('font-handKalam', 'text-sky-800', 'dark:text-sky-300', 'text-base', 'sm:text-lg', 'font-bold');
        } else if (fontClass === 'caveat-black') {
          span.classList.add('font-handCaveat', 'text-slate-900', 'dark:text-slate-100', 'text-lg', 'sm:text-xl', 'font-bold');
        } else {
          span.classList.add('font-sans', 'text-slate-800', 'dark:text-slate-200', 'text-xs', 'sm:text-sm', 'font-semibold');
        }
      });
    }

    function toggleBlankMode() {
      isBlankMode = !isBlankMode;
      const btn = document.getElementById('btn-toggle-blank');
      if (isBlankMode) {
        btn.classList.add('bg-sky-600', 'text-white');
        btn.innerText = '✓ Leere Vorlage';
      } else {
        btn.classList.remove('bg-sky-600', 'text-white');
        btn.innerText = 'Vorlage';
      }
      populateSheetView();
    }

    function printSheet() {
      populateSheetView();
      window.print();
    }

    function renderArchiveList() {
      const container = document.getElementById('archive-list-container');
      if (!container) return;
      const memos = getStoredMemos();
      const term = (document.getElementById('archive-search-input')?.value || '').toLowerCase().trim();

      const filtered = memos.filter(m => {
        if (!term) return true;
        return (m.title && m.title.toLowerCase().includes(term)) ||
               (m.situation && m.situation.toLowerCase().includes(term)) ||
               (m.schema && m.schema.toLowerCase().includes(term)) ||
               (m.date && m.date.includes(term));
      });

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="shadcn-card p-8 text-center space-y-2">
            <p class="text-sm font-bold text-slate-800 dark:text-slate-200">Keine Memos gefunden</p>
            <p class="text-xs text-slate-500">Erstelle ein neues Schema-Memo oder passe die Suche an.</p>
          </div>
        `;
        return;
      }

      container.innerHTML = filtered.map(item => `
        <article class="shadcn-card p-4 sm:p-5 space-y-3">
          <div class="flex items-center justify-between pb-2 border-b border-slate-100 dark:border-slate-800">
            <div>
              <span class="text-[10px] font-bold text-sky-600 dark:text-sky-400 uppercase tracking-wider">${formatDateDE(item.date)}</span>
              <h3 class="text-sm sm:text-base font-extrabold text-slate-900 dark:text-white">${escapeHtml(item.title)}</h3>
            </div>
            <div class="flex items-center gap-1">
              <button onclick="editMemo('${item.id}')" class="p-1.5 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-600 dark:text-slate-300 text-xs transition" title="Bearbeiten">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
              </button>
              <button onclick="deleteMemo('${item.id}')" class="p-1.5 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-rose-50 text-rose-500 text-xs transition" title="Löschen">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
              </button>
            </div>
          </div>
          ${item.emotion ? `<p class="text-xs text-slate-600 dark:text-slate-300"><span class="font-bold text-slate-800 dark:text-slate-200">Gefühl:</span> ${escapeHtml(item.emotion)}</p>` : ''}
          ${item.schema ? `<p class="text-xs text-indigo-600 dark:text-indigo-400"><span class="font-bold">Schema/Modus:</span> ${escapeHtml(item.schema)}</p>` : ''}
        </article>
      `).join('');
    }

    function editMemo(id) {
      const memos = getStoredMemos();
      const item = memos.find(m => m.id === id);
      if (!item) return;
      setFormData(item);
      switchView('edit');
    }

    function deleteMemo(id) {
      if (confirm('Dieses Schema-Memo wirklich löschen?')) {
        const memos = getStoredMemos().filter(m => m.id !== id);
        saveStoredMemos(memos);
        renderArchiveList();
        showToast('Memo gelöscht');
      }
    }

    function exportJSON() {
      const data = getStoredMemos();
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `schema_memos_backup_${new Date().toISOString().split('T')[0]}.json`;
      a.click();
      URL.revokeObjectURL(url);
    }

    function importJSON(e) {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (evt) => {
        try {
          const parsed = JSON.parse(evt.target.result);
          if (Array.isArray(parsed)) {
            saveStoredMemos(parsed);
            renderArchiveList();
            showToast('Memos erfolgreich importiert!');
          }
        } catch (err) {
          alert('Ungültige JSON Datei');
        }
      };
      reader.readAsText(file);
    }

    // ==========================================
    // MODULE B: DAILY DIARY & LIFE TRACKER LOGIC
    // ==========================================
    function sanitizeDiaryEntry(entry) {
      if (!entry || typeof entry !== 'object') return entry;
      if (Array.isArray(entry.emotions)) {
        entry.emotions = entry.emotions.map(stripAllEmojis).filter(Boolean);
      }
      if (entry.emotionNotes && typeof entry.emotionNotes === 'object') {
        const cleaned = {};
        for (const [k, v] of Object.entries(entry.emotionNotes)) {
          cleaned[stripAllEmojis(k)] = stripNonMoodEmojis(v);
        }
        entry.emotionNotes = cleaned;
      }
      if (Array.isArray(entry.memoryTags)) {
        entry.memoryTags = entry.memoryTags.map(stripAllEmojis).filter(Boolean);
      }
      if (Array.isArray(entry.mealTags)) {
        entry.mealTags = entry.mealTags.map(stripAllEmojis).filter(Boolean);
      }
      if (entry.sleep && Array.isArray(entry.sleep.tags)) {
        entry.sleep.tags = entry.sleep.tags.map(stripAllEmojis).filter(Boolean);
      }
      if (Array.isArray(entry.activities)) {
        entry.activities = entry.activities.map(stripAllEmojis).filter(Boolean);
      }
      if (Array.isArray(entry.medications)) {
        entry.medications = entry.medications.map(m => ({
          ...m,
          name: stripAllEmojis(m.name || ''),
          dose: stripAllEmojis(m.dose || ''),
          note: stripAllEmojis(m.note || '')
        }));
      }
      if (Array.isArray(entry.positiveThings)) {
        entry.positiveThings = entry.positiveThings.map(stripNonMoodEmojis).filter(Boolean);
      }
      if (entry.highlights) entry.highlights = stripNonMoodEmojis(entry.highlights);
      if (entry.notes) entry.notes = stripNonMoodEmojis(entry.notes);
      return entry;
    }

    function getStoredDiaryEntries() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY_DIARY);
        if (!raw) return [];
        const parsed = JSON.parse(raw);
        if (!Array.isArray(parsed)) return [];
        return parsed.map(sanitizeDiaryEntry);
      } catch (e) {
        console.error(e);
        return [];
      }
    }

    function saveStoredDiaryEntries(entries) {
      const cleaned = (entries || []).map(sanitizeDiaryEntry);
      localStorage.setItem(STORAGE_KEY_DIARY, JSON.stringify(cleaned));
      const badge = document.getElementById('diary-count-badge');
      if (badge) badge.innerText = cleaned.length;
    }

    function updateDiaryDateDisplay() {
      const dateVal = document.getElementById('input-diary-date').value;
      if (!dateVal) return;
      try {
        const d = new Date(dateVal + 'T12:00:00');
        const dayStr = d.toLocaleDateString('de-DE', { weekday: 'long', day: '2-digit', month: '2-digit', year: 'numeric' });
        const label = document.getElementById('diary-current-day-label');
        if (label) label.innerText = dayStr;
      } catch (e) {}
    }

    // Mood Score Update
    function updateMoodScore(score) {
      score = parseInt(score);
      const conf = MOOD_CONFIG[score] || MOOD_CONFIG[8];
      document.getElementById('diary-mood-slider').value = score;
      document.getElementById('diary-mood-badge').innerText = `${score} / 10 · ${conf.title.split('/')[0].trim()}`;
      document.getElementById('diary-mood-emoji').innerText = conf.emoji;
      document.getElementById('diary-mood-title').innerText = conf.title;
      document.getElementById('diary-mood-desc').innerText = conf.desc;
      document.getElementById('diary-mood-number').innerText = score;

      const banner = document.getElementById('diary-mood-banner');
      if (banner) {
        banner.className = `rounded-2xl p-3.5 flex items-center justify-between transition-colors duration-200 gap-3 ${conf.bg}`;
      }
    }

    function updateEnergyScore(score) {
      score = parseInt(score);
      document.getElementById('diary-energy-slider').value = score;
      const badge = document.getElementById('diary-energy-badge');
      let text = 'Aktiv & Ausgeglichen';
      if (score <= 3) text = 'Erschöpft / Niedrig';
      else if (score >= 8) text = 'Hochenergetisch / Tatendrang';
      badge.innerText = `${score} / 10 · ${text}`;
    }

    // Emotion Chips
    function initEmotionChips() {
      renderEmotionChips();
    }

    function renderEmotionChips() {
      const pleasantContainer = document.getElementById('pleasant-emotions-chips');
      const challengingContainer = document.getElementById('challenging-emotions-chips');

      const customs = customOptions.emotions || [];
      const pleasantCustoms = [];
      const challengingCustoms = [];

      customs.forEach(c => {
        if (typeof c === 'string') {
          pleasantCustoms.push(c);
        } else if (c && typeof c === 'object') {
          if (c.category === 'challenging') {
            challengingCustoms.push(c.name);
          } else {
            pleasantCustoms.push(c.name);
          }
        }
      });

      if (pleasantContainer) {
        const defHtml = PLEASANT_EMOTIONS.map(emo => `
          <button type="button" onclick="toggleDiaryEmotion('${escapeHtml(emo)}')" class="emotion-chip pleasant-emo text-xs px-2.5 py-1 rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium transition" data-emotion="${escapeHtml(emo)}" data-type="pleasant">
            ${escapeHtml(emo)}
          </button>
        `).join('');

        const custHtml = pleasantCustoms.map(emo => `
          <span class="emotion-chip-custom pleasant-custom inline-flex items-center text-xs rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium transition" data-emotion="${escapeHtml(emo)}" data-type="pleasant">
            <button type="button" onclick="toggleDiaryEmotion('${escapeHtml(emo)}')" class="py-1 pl-2.5 pr-1 focus:outline-none">
              ${escapeHtml(emo)}
            </button>
            <button type="button" onclick="event.stopPropagation(); deleteCustomOptionByName('emotions', '${escapeHtml(emo)}')" class="pr-2 pl-0.5 py-1 text-slate-400 hover:text-rose-500 font-bold text-sm leading-none transition" title="Löschen">×</button>
          </span>
        `).join('');

        pleasantContainer.innerHTML = defHtml + custHtml;
      }

      if (challengingContainer) {
        const defHtml = CHALLENGING_EMOTIONS.map(emo => `
          <button type="button" onclick="toggleDiaryEmotion('${escapeHtml(emo)}')" class="emotion-chip challenging-emo text-xs px-2.5 py-1 rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium transition" data-emotion="${escapeHtml(emo)}" data-type="challenging">
            ${escapeHtml(emo)}
          </button>
        `).join('');

        const custHtml = challengingCustoms.map(emo => `
          <span class="emotion-chip-custom challenging-custom inline-flex items-center text-xs rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium transition" data-emotion="${escapeHtml(emo)}" data-type="challenging">
            <button type="button" onclick="toggleDiaryEmotion('${escapeHtml(emo)}')" class="py-1 pl-2.5 pr-1 focus:outline-none">
              ${escapeHtml(emo)}
            </button>
            <button type="button" onclick="event.stopPropagation(); deleteCustomOptionByName('emotions', '${escapeHtml(emo)}')" class="pr-2 pl-0.5 py-1 text-slate-400 hover:text-rose-500 font-bold text-sm leading-none transition" title="Löschen">×</button>
          </span>
        `).join('');

        challengingContainer.innerHTML = defHtml + custHtml;
      }

      updateEmotionChipStyles();
    }

    function toggleDiaryEmotion(emo) {
      if (selectedDiaryEmotions.has(emo)) {
        selectedDiaryEmotions.delete(emo);
        delete diaryEmotionNotes[emo];
      } else {
        selectedDiaryEmotions.add(emo);
        if (!diaryEmotionNotes[emo]) diaryEmotionNotes[emo] = '';
      }
      updateEmotionChipStyles();
      renderEmotionNoteSegments();
    }

    function updateEmotionChipStyles() {
      document.querySelectorAll('.emotion-chip, .emotion-chip-custom').forEach(chip => {
        const emo = chip.getAttribute('data-emotion');
        const isChallenging = chip.getAttribute('data-type') === 'challenging';
        const isCustom = chip.classList.contains('emotion-chip-custom');
        const isSelected = selectedDiaryEmotions.has(emo);

        if (isCustom) {
          if (isSelected) {
            chip.className = `emotion-chip-custom ${isChallenging ? 'challenging-custom' : 'pleasant-custom'} inline-flex items-center text-xs rounded-full border font-bold transition shadow-xs ${isChallenging ? 'border-rose-500 bg-rose-100 dark:bg-rose-950/80 text-rose-900 dark:text-rose-200' : 'border-emerald-500 bg-emerald-100 dark:bg-emerald-950/80 text-emerald-900 dark:text-emerald-200'}`;
          } else {
            chip.className = `emotion-chip-custom ${isChallenging ? 'challenging-custom' : 'pleasant-custom'} inline-flex items-center text-xs rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium transition`;
          }
        } else {
          if (isSelected) {
            if (isChallenging) {
              chip.className = 'emotion-chip challenging-emo text-xs px-2.5 py-1 rounded-full border border-rose-500 bg-rose-100 dark:bg-rose-950/80 text-rose-900 dark:text-rose-200 font-bold transition shadow-xs';
            } else {
              chip.className = 'emotion-chip pleasant-emo text-xs px-2.5 py-1 rounded-full border border-emerald-500 bg-emerald-100 dark:bg-emerald-950/80 text-emerald-900 dark:text-emerald-200 font-bold transition shadow-xs';
            }
          } else {
            chip.className = `emotion-chip ${isChallenging ? 'challenging-emo' : 'pleasant-emo'} text-xs px-2.5 py-1 rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium transition`;
          }
        }
      });
    }

    function renderEmotionNoteSegments() {
      const wrapper = document.getElementById('diary-emotion-notes-wrapper');
      const container = document.getElementById('diary-emotion-notes-container');
      const badge = document.getElementById('emotion-notes-count-badge');
      if (!container || !wrapper) return;

      const emos = Array.from(selectedDiaryEmotions);
      badge.innerText = `${emos.length} ausgewählt`;

      if (emos.length === 0) {
        wrapper.classList.add('hidden');
        container.innerHTML = '';
        return;
      }

      wrapper.classList.remove('hidden');
      container.innerHTML = emos.map(emo => `
        <div class="p-3 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50/50 dark:bg-slate-900/50 space-y-1.5">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-slate-800 dark:text-slate-200">Gefühl: <span class="text-emerald-600 dark:text-emerald-400 font-extrabold">${escapeHtml(emo)}</span></span>
            <button type="button" onclick="toggleDiaryEmotion('${escapeHtml(emo)}')" class="text-[10px] text-rose-500 hover:text-rose-700 font-semibold">Entfernen</button>
          </div>
          <textarea rows="2" oninput="diaryEmotionNotes['${escapeHtml(emo)}'] = this.value" placeholder="Was hat ${escapeHtml(emo)} ausgelöst und wie bist du damit umgegangen?" class="shadcn-input text-xs block w-full resize-none min-h-[50px] leading-relaxed">${escapeHtml(diaryEmotionNotes[emo] || '')}</textarea>
        </div>
      `).join('');
    }

    // ==========================================
    // CUSTOM OPTIONS SYSTEM & MODAL (+)
    // ==========================================
    function sanitizeCustomOptions(opts) {
      if (!opts || typeof opts !== 'object') return opts;
      for (const key of Object.keys(opts)) {
        if (Array.isArray(opts[key])) {
          if (key === 'meds') {
            opts[key] = opts[key].map(m => {
              if (typeof m === 'string') return { name: stripAllEmojis(m), dose: '1 Dosis' };
              return {
                name: stripAllEmojis(m.name || ''),
                dose: stripAllEmojis(m.dose || '')
              };
            }).filter(m => m.name);
          } else if (key === 'emotions') {
            opts[key] = opts[key].map(e => {
              if (typeof e === 'string') return { name: stripAllEmojis(e), category: 'pleasant' };
              return {
                name: stripAllEmojis(e.name || ''),
                category: e.category || 'pleasant'
              };
            }).filter(e => e.name);
          } else {
            opts[key] = opts[key]
              .map(val => (typeof val === 'string' ? stripAllEmojis(val) : val))
              .filter(Boolean);
          }
        }
      }
      return opts;
    }

    function loadCustomOptions() {
      try {
        const saved = localStorage.getItem(STORAGE_KEY_CUSTOM_OPTIONS);
        if (saved) {
          const parsed = JSON.parse(saved);
          const cleaned = sanitizeCustomOptions(parsed);
          customOptions = Object.assign(customOptions, cleaned);
          localStorage.setItem(STORAGE_KEY_CUSTOM_OPTIONS, JSON.stringify(customOptions));
        }
      } catch (e) {
        console.error('Error loading custom options', e);
      }
    }

    function saveCustomOptionsToStorage() {
      try {
        sanitizeCustomOptions(customOptions);
        localStorage.setItem(STORAGE_KEY_CUSTOM_OPTIONS, JSON.stringify(customOptions));
      } catch (e) {
        console.error('Error saving custom options', e);
      }
    }

    let activeCustomModalCategory = null;

    function openAddCustomModal(category) {
      activeCustomModalCategory = category;
      const modal = document.getElementById('custom-option-modal');
      const icon = document.getElementById('custom-modal-icon');
      const title = document.getElementById('custom-modal-title');
      const fields = document.getElementById('custom-modal-fields');

      if (!modal) return;

      const configs = {
        'meds': { title: 'Eigenes Medikament hinzufügen', icon: '+' },
        'emotions': { title: 'Eigene Emotion hinzufügen', icon: '+' },
        'sleep_factors': { title: 'Eigenen Schlaffaktor hinzufügen', icon: '+' },
        'activities': { title: 'Eigene Aktivität / Sport hinzufügen', icon: '+' },
        'meal_tags': { title: 'Eigenen Mahlzeiten-Tag hinzufügen', icon: '+' },
        'memory_tags': { title: 'Eigenen Erlebnis-Tag (#) hinzufügen', icon: '+' },
        'schema_emotions': { title: 'Eigene Schema-Emotion hinzufügen', icon: '+' },
        'schema_coping': { title: 'Eigenes Bewältigungsverhalten hinzufügen', icon: '+' },
        'schema_actions': { title: 'Eigene Handlung hinzufügen', icon: '+' }
      };

      const cfg = configs[category] || { title: 'Eigene Option hinzufügen', icon: '+' };
      if (icon) icon.textContent = cfg.icon;
      if (title) title.textContent = cfg.title;

      if (category === 'meds') {
        fields.innerHTML = `
          <div>
            <label class="block text-[10px] font-bold uppercase text-slate-500 mb-0.5">Name des Medikaments / Supplements:</label>
            <input type="text" id="input-custom-modal-name" placeholder="z. B. Attentin, Magnesium, Elvanse..." class="shadcn-input text-xs block w-full">
          </div>
          <div>
            <label class="block text-[10px] font-bold uppercase text-slate-500 mb-0.5">Standard-Dosis:</label>
            <input type="text" id="input-custom-modal-dose" placeholder="z. B. 10 mg, 400 mg, 1 Kapsel..." class="shadcn-input text-xs block w-full" onkeydown="if(event.key==='Enter'){event.preventDefault();saveCustomOptionFromModal();}">
          </div>
        `;
      } else if (category === 'emotions') {
        fields.innerHTML = `
          <div>
            <label class="block text-[10px] font-bold uppercase text-slate-500 mb-1">Kategorie des Gefühls:</label>
            <div class="grid grid-cols-2 gap-2 mb-2.5">
              <label class="flex items-center gap-1.5 p-2 rounded-xl border border-emerald-300 dark:border-emerald-800 bg-emerald-50/60 dark:bg-emerald-950/40 cursor-pointer">
                <input type="radio" name="custom-emotion-cat" value="pleasant" checked class="text-emerald-600 focus:ring-emerald-500">
                <span class="text-xs font-bold text-emerald-800 dark:text-emerald-200">Angenehm / Positiv</span>
              </label>
              <label class="flex items-center gap-1.5 p-2 rounded-xl border border-rose-300 dark:border-rose-800 bg-rose-50/60 dark:bg-rose-950/40 cursor-pointer">
                <input type="radio" name="custom-emotion-cat" value="challenging" class="text-rose-600 focus:ring-rose-500">
                <span class="text-xs font-bold text-rose-800 dark:text-rose-200">Fordernd / Negativ</span>
              </label>
            </div>
            <label class="block text-[10px] font-bold uppercase text-slate-500 mb-0.5">Name des Gefühls:</label>
            <input type="text" id="input-custom-modal-val" placeholder="z. B. Inspiriert, Überreizt, Erleichtert..." class="shadcn-input text-xs block w-full" onkeydown="if(event.key==='Enter'){event.preventDefault();saveCustomOptionFromModal();}">
          </div>
        `;
      } else {
        fields.innerHTML = `
          <div>
            <label class="block text-[10px] font-bold uppercase text-slate-500 mb-0.5">Bezeichnung:</label>
            <input type="text" id="input-custom-modal-val" placeholder="z. B. Neue Bezeichnung..." class="shadcn-input text-xs block w-full" onkeydown="if(event.key==='Enter'){event.preventDefault();saveCustomOptionFromModal();}">
          </div>
        `;
      }

      renderCustomModalExistingList();
      modal.classList.remove('hidden');

      setTimeout(() => {
        const inp = category === 'meds' ? document.getElementById('input-custom-modal-name') : document.getElementById('input-custom-modal-val');
        if (inp) inp.focus();
      }, 50);
    }

    function renderCustomModalExistingList() {
      const existingWrapper = document.getElementById('custom-modal-existing-wrapper');
      const existingList = document.getElementById('custom-modal-existing-list');
      if (!existingWrapper || !existingList || !activeCustomModalCategory) return;

      const items = customOptions[activeCustomModalCategory] || [];
      if (items.length === 0) {
        existingWrapper.classList.add('hidden');
        existingList.innerHTML = '';
        return;
      }

      existingWrapper.classList.remove('hidden');
      existingList.innerHTML = items.map((item, idx) => {
        let label = '';
        if (typeof item === 'object') {
          if (activeCustomModalCategory === 'meds') {
            label = `${item.name} (${item.dose})`;
          } else if (activeCustomModalCategory === 'emotions') {
            const catBadge = item.category === 'challenging' ? '[Negativ]' : '[Positiv]';
            label = `${catBadge} ${item.name}`;
          } else {
            label = item.name || JSON.stringify(item);
          }
        } else {
          label = item;
        }
        return `
          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-lg text-[11px] bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 border border-slate-200 dark:border-slate-700">
            <span>${escapeHtml(label)}</span>
            <button type="button" onclick="deleteCustomOptionItem('${activeCustomModalCategory}', ${idx})" class="text-rose-500 hover:text-rose-700 font-bold ml-1 text-xs" title="Löschen">×</button>
          </span>
        `;
      }).join('');
    }

    function closeCustomOptionModal() {
      const modal = document.getElementById('custom-option-modal');
      if (modal) modal.classList.add('hidden');
      activeCustomModalCategory = null;
    }

    function saveCustomOptionFromModal() {
      if (!activeCustomModalCategory) return;

      if (activeCustomModalCategory === 'meds') {
        const name = stripAllEmojis((document.getElementById('input-custom-modal-name')?.value || '').trim());
        const dose = stripAllEmojis((document.getElementById('input-custom-modal-dose')?.value || '').trim()) || '1 Dosis';
        if (!name) {
          alert('Bitte gib mindestens den Namen des Medikaments ein.');
          return;
        }
        customOptions.meds = customOptions.meds || [];
        customOptions.meds.push({ name, dose });
        saveCustomOptionsToStorage();
        renderQuickMedsChips();
        quickAddMedication(name, dose);
        showToast(`${name} gespeichert & eingetragen!`);
      } else if (activeCustomModalCategory === 'emotions') {
        const val = stripAllEmojis((document.getElementById('input-custom-modal-val')?.value || '').trim());
        if (!val) {
          alert('Bitte gib eine Bezeichnung ein.');
          return;
        }
        const catRadio = document.querySelector('input[name="custom-emotion-cat"]:checked');
        const emotionCat = catRadio ? catRadio.value : 'pleasant';

        customOptions.emotions = customOptions.emotions || [];
        customOptions.emotions.push({ name: val, category: emotionCat });
        saveCustomOptionsToStorage();

        renderEmotionChips();
        toggleDiaryEmotion(val);
        showToast(`Emotion "${val}" gespeichert!`);
      } else {
        const val = stripAllEmojis((document.getElementById('input-custom-modal-val')?.value || '').trim());
        if (!val) {
          alert('Bitte gib eine Bezeichnung ein.');
          return;
        }
        customOptions[activeCustomModalCategory] = customOptions[activeCustomModalCategory] || [];
        customOptions[activeCustomModalCategory].push(val);
        saveCustomOptionsToStorage();

        if (activeCustomModalCategory === 'sleep_factors') {
          renderSleepTagChips();
          toggleSleepTag(val);
        } else if (activeCustomModalCategory === 'activities') {
          renderActivitiesChips();
          toggleActivityTag(val);
        } else if (activeCustomModalCategory === 'meal_tags') {
          renderMealTagChips();
          toggleMealTag(val);
        } else if (activeCustomModalCategory === 'memory_tags') {
          renderMemoryTagChips();
          toggleMemoryTag(val);
        } else if (activeCustomModalCategory === 'schema_emotions') {
          renderSchemaCustomChips();
          appendTag('input-emotion', val);
        } else if (activeCustomModalCategory === 'schema_coping') {
          renderSchemaCustomChips();
          appendTag('input-coping', val);
        } else if (activeCustomModalCategory === 'schema_actions') {
          renderSchemaCustomChips();
          appendTag('input-new-action', val);
        }
        showToast(`"${val}" dauerhaft gespeichert!`);
      }

      closeCustomOptionModal();
    }

    function deleteCustomOptionItem(category, index) {
      if (!customOptions[category]) return;
      const item = customOptions[category][index];
      const name = (item && typeof item === 'object') ? item.name : item;

      customOptions[category].splice(index, 1);
      saveCustomOptionsToStorage();
      renderCustomModalExistingList();

      if (category === 'meds') renderQuickMedsChips();
      else if (category === 'emotions') {
        if (name) {
          selectedDiaryEmotions.delete(name);
          delete diaryEmotionNotes[name];
          renderEmotionNoteSegments();
        }
        renderEmotionChips();
      } else if (category === 'sleep_factors') {
        if (name) selectedSleepTags.delete(name);
        renderSleepTagChips();
      } else if (category === 'activities') {
        if (name) selectedActivities.delete(name);
        renderActivitiesChips();
      } else if (category === 'meal_tags') {
        if (name) selectedMealTags.delete(name);
        renderMealTagChips();
      } else if (category === 'memory_tags') {
        if (name) selectedMemoryTags.delete(name);
        renderMemoryTagChips();
      } else if (category.startsWith('schema_')) renderSchemaCustomChips();

      showToast('Eintrag gelöscht');
    }

    function deleteCustomOptionByName(category, name) {
      if (!customOptions[category]) return;
      const idx = customOptions[category].findIndex(item => {
        if (typeof item === 'object') return item.name === name;
        return item === name;
      });
      if (idx !== -1) {
        customOptions[category].splice(idx, 1);
        saveCustomOptionsToStorage();

        if (category === 'meds') {
          renderQuickMedsChips();
        } else if (category === 'emotions') {
          selectedDiaryEmotions.delete(name);
          delete diaryEmotionNotes[name];
          renderEmotionChips();
          renderEmotionNoteSegments();
        } else if (category === 'sleep_factors') {
          selectedSleepTags.delete(name);
          renderSleepTagChips();
        } else if (category === 'activities') {
          selectedActivities.delete(name);
          renderActivitiesChips();
        } else if (category === 'meal_tags') {
          selectedMealTags.delete(name);
          renderMealTagChips();
        } else if (category === 'memory_tags') {
          selectedMemoryTags.delete(name);
          renderMemoryTagChips();
        } else if (category.startsWith('schema_')) {
          renderSchemaCustomChips();
        }
        showToast(`"${name}" gelöscht`);
      }
    }

    // ==========================================
    // ACCORDION & CARDS CONTROLLER
    // ==========================================
    function toggleDiaryCard(key) {
      diaryCardsState[key] = !diaryCardsState[key];
      applyDiaryCardVisibility(key);
    }

    function applyDiaryCardVisibility(key) {
      const body = document.getElementById(`body-diary-${key}`);
      const chevron = document.getElementById(`chevron-${key}`);
      if (!body) return;
      if (diaryCardsState[key]) {
        body.classList.remove('hidden');
        if (chevron) chevron.classList.add('rotate-180');
      } else {
        body.classList.add('hidden');
        if (chevron) chevron.classList.remove('rotate-180');
      }
    }

    function toggleAllCardsState() {
      allCardsExpanded = !allCardsExpanded;
      ['mood', 'meds', 'vital', 'adhs', 'mind'].forEach(k => {
        diaryCardsState[k] = allCardsExpanded;
        applyDiaryCardVisibility(k);
      });
      const lbl = document.getElementById('label-toggle-all-cards');
      if (lbl) lbl.textContent = allCardsExpanded ? '⤓ Zuklappen' : '⤢ Aufklappen';
    }

    function filterCheckinSections(tab) {
      document.querySelectorAll('.sec-nav-btn').forEach(btn => {
        btn.classList.remove('active', 'bg-slate-900', 'text-white', 'dark:bg-white', 'dark:text-slate-900');
        btn.classList.add('bg-slate-100', 'dark:bg-slate-800', 'text-slate-600', 'dark:text-slate-400');
      });
      const activeBtn = document.getElementById(`sec-nav-${tab}`);
      if (activeBtn) {
        activeBtn.classList.remove('bg-slate-100', 'dark:bg-slate-800', 'text-slate-600', 'dark:text-slate-400');
        activeBtn.classList.add('active', 'bg-slate-900', 'text-white', 'dark:bg-white', 'dark:text-slate-900');
      }

      const keys = ['mood', 'meds', 'vital', 'adhs', 'mind'];
      if (tab === 'all') {
        keys.forEach(k => {
          diaryCardsState[k] = true;
          applyDiaryCardVisibility(k);
        });
      } else {
        keys.forEach(k => {
          diaryCardsState[k] = (k === tab);
          applyDiaryCardVisibility(k);
        });
        const targetCard = document.getElementById(`card-diary-${tab}`);
        if (targetCard) targetCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    function updateCardSummaryBadges() {
      const isDe = (appSettings.language || 'de') === 'de';

      const moodBadge = document.getElementById('badge-summary-mood');
      const moodVal = document.getElementById('diary-mood-slider')?.value || 8;
      const emoCount = selectedDiaryEmotions.size;
      if (moodBadge) {
        const emoWord = isDe ? (emoCount === 1 ? 'Gefühl' : 'Gefühle') : (emoCount === 1 ? 'Emotion' : 'Emotions');
        moodBadge.textContent = `${moodVal}/10 · ${emoCount} ${emoWord}`;
      }

      const medsBadge = document.getElementById('badge-summary-meds');
      const medCount = currentDayMedications.length;
      const eff = currentMedEfficacyRating ? ` · ${currentMedEfficacyRating.toUpperCase()}` : '';
      if (medsBadge) {
        const medWord = isDe ? (medCount === 1 ? 'Medi' : 'Medis') : (medCount === 1 ? 'Med' : 'Meds');
        medsBadge.textContent = `${medCount} ${medWord}${eff}`;
      }

      const vitalBadge = document.getElementById('badge-summary-vital');
      const duration = document.getElementById('input-sleep-duration')?.value || '7.5';
      if (vitalBadge) {
        vitalBadge.textContent = `${currentWaterMl} ml · ${duration}h ${isDe ? 'Schlaf' : 'Sleep'}`;
      }

      const adhsBadge = document.getElementById('badge-summary-adhs');
      const focusVal = document.getElementById('input-adhs-focus')?.value || 7;
      const stepsVal = document.getElementById('input-steps-count')?.value || 0;
      if (adhsBadge) {
        adhsBadge.textContent = `${isDe ? 'Fokus' : 'Focus'} ${focusVal}/10 · ${parseInt(stepsVal).toLocaleString(isDe ? 'de-DE' : 'en-US')} Steps`;
      }

      const mindBadge = document.getElementById('badge-summary-mind');
      const posInputs = document.querySelectorAll('#positive-things-inputs-container input');
      let posFilled = 0;
      posInputs.forEach(i => { if (i.value.trim()) posFilled++; });
      if (mindBadge) {
        mindBadge.textContent = `${posFilled}/3 ${isDe ? 'Positiv' : 'Positive'}`;
      }
    }

    function renderQuickMedsChips() {
      const container = document.getElementById('quick-meds-chips-container');
      if (!container) return;

      const defaults = DEFAULT_MED_PRESETS;
      const customs = customOptions.meds || [];

      let html = defaults.map(m => `
        <button type="button" onclick="quickAddMedication('${escapeHtml(m.name)}', '${escapeHtml(m.dose)}')" class="text-xs px-2.5 py-1 rounded-lg bg-violet-50 dark:bg-violet-950/50 hover:bg-violet-100 text-violet-700 dark:text-violet-300 border border-violet-200/60 dark:border-violet-800/40 transition font-medium inline-flex items-center gap-1">
          <span>${escapeHtml(m.name)}</span> <span class="opacity-75 font-normal text-[10px]">${escapeHtml(m.dose)}</span>
        </button>
      `).join('');

      if (customs.length > 0) {
        html += customs.map(m => `
          <span class="inline-flex items-center text-xs rounded-lg bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-800 transition font-medium">
            <button type="button" onclick="quickAddMedication('${escapeHtml(m.name)}', '${escapeHtml(m.dose)}')" class="py-1 pl-2.5 pr-1 hover:bg-emerald-100/60 transition inline-flex items-center gap-1 rounded-l-lg">
              <span>${escapeHtml(m.name)}</span> <span class="opacity-75 font-normal text-[10px]">${escapeHtml(m.dose)}</span>
            </button>
            <button type="button" onclick="event.stopPropagation(); deleteCustomOptionByName('meds', '${escapeHtml(m.name)}')" class="pr-2 pl-0.5 py-1 text-slate-400 hover:text-rose-500 font-bold text-sm leading-none transition" title="Löschen">×</button>
          </span>
        `).join('');
      }

      container.innerHTML = html;
    }

    function renderSchemaCustomChips() {
      const s1 = document.getElementById('schema-step1-chips');
      if (s1 && customOptions.schema_emotions) {
        s1.querySelectorAll('.custom-schema-chip').forEach(b => b.remove());
        const plusBtn = s1.querySelector('button[onclick*="openAddCustomModal"]');
        customOptions.schema_emotions.forEach(emo => {
          const span = document.createElement('span');
          span.className = 'custom-schema-chip inline-flex items-center text-xs rounded-full bg-sky-50 dark:bg-sky-950/60 text-sky-800 dark:text-sky-300 font-medium border border-sky-300 dark:border-sky-800 transition';
          span.innerHTML = `
            <button type="button" class="py-1 pl-2.5 pr-1 hover:bg-sky-100 dark:hover:bg-sky-900/50 rounded-l-full transition">${escapeHtml(emo)}</button>
            <button type="button" class="pr-2 pl-0.5 py-1 text-slate-400 hover:text-rose-500 font-bold text-sm leading-none transition" title="Löschen">×</button>
          `;
          span.firstElementChild.onclick = () => appendTag('input-emotion', emo);
          span.lastElementChild.onclick = (e) => { e.stopPropagation(); deleteCustomOptionByName('schema_emotions', emo); };
          if (plusBtn) s1.insertBefore(span, plusBtn);
          else s1.appendChild(span);
        });
      }

      const s2 = document.getElementById('schema-step2-coping-chips');
      if (s2 && customOptions.schema_coping) {
        s2.querySelectorAll('.custom-schema-chip').forEach(b => b.remove());
        const plusBtn = s2.querySelector('button[onclick*="openAddCustomModal"]');
        customOptions.schema_coping.forEach(c => {
          const span = document.createElement('span');
          span.className = 'custom-schema-chip inline-flex items-center text-xs rounded-full bg-indigo-50 dark:bg-indigo-950/60 text-indigo-800 dark:text-indigo-300 font-medium border border-indigo-300 dark:border-indigo-800 transition';
          span.innerHTML = `
            <button type="button" class="py-1 pl-2.5 pr-1 hover:bg-indigo-100 dark:hover:bg-indigo-900/50 rounded-l-full transition">${escapeHtml(c)}</button>
            <button type="button" class="pr-2 pl-0.5 py-1 text-slate-400 hover:text-rose-500 font-bold text-sm leading-none transition" title="Löschen">×</button>
          `;
          span.firstElementChild.onclick = () => appendTag('input-coping', c);
          span.lastElementChild.onclick = (e) => { e.stopPropagation(); deleteCustomOptionByName('schema_coping', c); };
          if (plusBtn) s2.insertBefore(span, plusBtn);
          else s2.appendChild(span);
        });
      }

      const s4 = document.getElementById('schema-step4-action-chips');
      if (s4 && customOptions.schema_actions) {
        s4.querySelectorAll('.custom-schema-chip').forEach(b => b.remove());
        const plusBtn = s4.querySelector('button[onclick*="openAddCustomModal"]');
        customOptions.schema_actions.forEach(a => {
          const span = document.createElement('span');
          span.className = 'custom-schema-chip inline-flex items-center text-xs rounded-full bg-emerald-50 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300 font-medium border border-emerald-300 dark:border-emerald-800 transition';
          span.innerHTML = `
            <button type="button" class="py-1 pl-2.5 pr-1 hover:bg-emerald-100 dark:hover:bg-emerald-900/50 rounded-l-full transition">${escapeHtml(a)}</button>
            <button type="button" class="pr-2 pl-0.5 py-1 text-slate-400 hover:text-rose-500 font-bold text-sm leading-none transition" title="Löschen">×</button>
          `;
          span.firstElementChild.onclick = () => appendTag('input-new-action', a);
          span.lastElementChild.onclick = (e) => { e.stopPropagation(); deleteCustomOptionByName('schema_actions', a); };
          if (plusBtn) s4.insertBefore(span, plusBtn);
          else s4.appendChild(span);
        });
      }
    }

    // ==========================================
    // MEDICATION TRACKER LOGIC
    // ==========================================
    function getCurrentTimeFormatted() {
      const now = new Date();
      return `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}`;
    }

    function quickAddMedication(name, dose) {
      const med = {
        id: 'med_' + Date.now() + '_' + Math.random().toString(36).substr(2, 4),
        name: name,
        dose: dose,
        time: getCurrentTimeFormatted(),
        note: '',
        taken: true
      };
      currentDayMedications.push(med);
      renderMedicationsList();
      showToast(`${name} (${dose}) um ${med.time} erfasst!`);
    }

    function updateMedTime(id, newTime) {
      const med = currentDayMedications.find(m => m.id === id);
      if (med) {
        med.time = newTime;
        showToast(`Uhrzeit für ${med.name} auf ${newTime} gesetzt`);
      }
    }

    function setMedEfficacyRating(rating) {
      currentMedEfficacyRating = rating || '';
      const sel = document.getElementById('select-med-efficacy');
      if (sel && sel.value !== currentMedEfficacyRating) {
        sel.value = currentMedEfficacyRating || 'none';
      }
      const labels = {
        'optimal': 'Optimal / Flow',
        'gut': 'Gut & Stabil',
        'schwach': 'Kaum Wirkung',
        'zu_stark': 'Zu intensiv',
        'nebenwirkung': 'Nebenwirkungen'
      };
      const badge = document.getElementById('med-efficacy-badge');
      if (badge) {
        if (rating && rating !== 'none') {
          badge.textContent = labels[rating] || rating;
          if (rating === 'optimal' || rating === 'gut') {
            badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-600 text-white';
          } else if (rating === 'zu_stark' || rating === 'nebenwirkung') {
            badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-rose-600 text-white';
          } else {
            badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-600 text-white';
          }
        } else {
          badge.textContent = 'Noch offen';
          badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-500 dark:text-slate-400';
        }
      }
      document.querySelectorAll('.med-eff-btn').forEach(btn => {
        if (btn.getAttribute('data-rating') === rating) {
          btn.className = 'med-eff-btn active text-xs px-2.5 py-1 rounded-lg border border-violet-500 bg-violet-100 dark:bg-violet-950/80 text-violet-900 dark:text-violet-200 font-bold shadow-xs';
        } else {
          btn.className = 'med-eff-btn text-xs px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 font-semibold transition';
        }
      });
      updateCardSummaryBadges();
    }

    function toggleMedTaken(id) {
      const med = currentDayMedications.find(m => m.id === id);
      if (med) {
        med.taken = !med.taken;
        renderMedicationsList();
      }
    }

    function removeMedication(id) {
      currentDayMedications = currentDayMedications.filter(m => m.id !== id);
      renderMedicationsList();
    }

    function renderMedicationsList() {
      const container = document.getElementById('today-meds-list');
      const badge = document.getElementById('meds-count-badge');
      if (badge) badge.innerText = `${currentDayMedications.length} Medis`;

      if (!container) return;

      if (currentDayMedications.length === 0) {
        container.innerHTML = `
          <div class="text-xs text-slate-400 italic py-1.5">
            Noch keine Medikamente für heute eingetragen. Tippe oben auf einen Schnell-Button oder (+).
          </div>
        `;
        updateCardSummaryBadges();
        return;
      }

      container.innerHTML = currentDayMedications.map(med => `
        <div class="flex items-center justify-between p-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs gap-2 shadow-2xs">
          <div class="flex items-center gap-2 min-w-0 flex-1">
            <input type="checkbox" ${med.taken ? 'checked' : ''} onchange="toggleMedTaken('${med.id}')" class="w-4 h-4 rounded text-violet-600 focus:ring-violet-500 cursor-pointer shrink-0">
            <div class="min-w-0 flex-1">
              <span class="font-bold text-slate-900 dark:text-white ${med.taken ? '' : 'line-through text-slate-400'}">${escapeHtml(med.name)}</span>
              <span class="ml-1 px-1.5 py-0.5 rounded text-[10px] font-bold bg-violet-100 dark:bg-violet-950/60 text-violet-700 dark:text-violet-300">${escapeHtml(med.dose)}</span>
            </div>
          </div>
          <!-- Editable time directly on each med pill -->
          <div class="flex items-center gap-1.5 shrink-0">
            <div class="flex items-center gap-1 bg-slate-100 dark:bg-slate-700/80 px-2 py-0.5 rounded-lg border border-slate-200 dark:border-slate-600 shrink-0">
              <svg class="w-3.5 h-3.5 text-slate-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" stroke-width="2"/><path stroke-linecap="round" stroke-width="2" d="M12 7v5l3 2"/></svg>
              <input type="time" value="${escapeHtml(med.time || getCurrentTimeFormatted())}" onchange="updateMedTime('${med.id}', this.value)" class="bg-transparent border-0 p-0 text-xs font-bold text-slate-800 dark:text-slate-200 focus:outline-none w-20 sm:w-24 cursor-pointer" title="Einnahme-Uhrzeit anpassen">
            </div>
            <button type="button" onclick="removeMedication('${med.id}')" class="p-1 text-slate-400 hover:text-rose-500 transition shrink-0" title="Löschen">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
          </div>
        </div>
      `).join('');

      updateCardSummaryBadges();
    }

    function setReboundLevel(level) {
      currentReboundLevel = level || 'none';
      const sel = document.getElementById('select-med-rebound');
      if (sel && sel.value !== currentReboundLevel) {
        sel.value = currentReboundLevel;
      }
      const badge = document.getElementById('rebound-badge');
      if (badge) {
        if (level === 'none') {
          badge.innerText = 'Kein Rebound';
          badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950/70 text-emerald-800 dark:text-emerald-200';
        } else if (level === 'leicht') {
          badge.innerText = 'Leichter Rebound';
          badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-100 dark:bg-amber-950/70 text-amber-800 dark:text-amber-200';
        } else {
          badge.innerText = (level === 'stark' ? 'Starker Rebound' : 'Spürbarer Rebound');
          badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-rose-600 text-white shadow-xs';
        }
      }
      document.querySelectorAll('.rebound-btn').forEach(btn => {
        if (btn.getAttribute('data-level') === level) {
          btn.className = 'rebound-btn text-xs px-2.5 py-1 rounded-lg border border-violet-500 bg-violet-100 dark:bg-violet-950/70 text-violet-800 dark:text-violet-200 font-bold';
        } else {
          btn.className = 'rebound-btn text-xs px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700 hover:border-violet-300 font-semibold';
        }
      });
    }

    // ==========================================
    // MEALS, WATER & CAFFEINE LOGIC
    // ==========================================
    function appendMealTag(mealType, tag) {
      const input = document.getElementById('input-meal-' + mealType);
      if (input) {
        if (input.value.trim().length > 0) input.value += ', ' + tag;
        else input.value = tag;
        input.focus();
      }
    }

    function toggleMealTag(tag) {
      if (selectedMealTags.has(tag)) selectedMealTags.delete(tag);
      else selectedMealTags.add(tag);
      renderMealTagChips();
    }

    function renderMealTagChips() {
      document.querySelectorAll('.meal-tag-btn').forEach(btn => {
        const tag = btn.getAttribute('data-tag');
        if (selectedMealTags.has(tag)) {
          btn.className = 'meal-tag-btn text-xs px-2.5 py-1 rounded-full border border-amber-500 bg-amber-100 dark:bg-amber-950/70 text-amber-900 dark:text-amber-200 font-bold transition';
        } else {
          btn.className = 'meal-tag-btn text-xs px-2.5 py-1 rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 font-medium transition';
        }
      });
    }

    function addWater(amount) {
      currentWaterMl = Math.max(0, currentWaterMl + amount);
      updateWaterDisplay();
    }

    function resetWater() {
      currentWaterMl = 0;
      updateWaterDisplay();
    }

    function updateWaterDisplay() {
      const disp = document.getElementById('water-display');
      const bar = document.getElementById('water-progress-bar');
      if (!disp || !bar) return;
      const pct = Math.min(100, Math.round((currentWaterMl / currentWaterGoal) * 100));
      disp.innerText = `${currentWaterMl} ml / ${currentWaterGoal} ml (${pct}%)`;
      bar.style.width = pct + '%';
    }

    function changeCoffee(delta) {
      currentCoffeeCups = Math.max(0, currentCoffeeCups + delta);
      currentCaffeineCups = currentCoffeeCups + currentEnergyCups;
      updateCaffeineDisplay();
      if (delta > 0) showToast('+1 Kaffee erfasst');
    }

    function changeEnergyDrink(delta) {
      currentEnergyCups = Math.max(0, currentEnergyCups + delta);
      currentCaffeineCups = currentCoffeeCups + currentEnergyCups;
      updateCaffeineDisplay();
      if (delta > 0) showToast('+1 Energy Drink erfasst');
    }

    function resetCaffeine() {
      currentCoffeeCups = 0;
      currentEnergyCups = 0;
      currentCaffeineCups = 0;
      updateCaffeineDisplay();
      showToast('Koffein zurückgesetzt');
    }

    function updateCaffeineDisplay() {
      const coffeeEl = document.getElementById('coffee-count-display');
      const energyEl = document.getElementById('energy-count-display');
      const badgeEl = document.getElementById('caffeine-total-badge');
      const dispEl = document.getElementById('caffeine-display');
      const mixEl = document.getElementById('caffeine-mix-label');

      if (coffeeEl) coffeeEl.textContent = String(currentCoffeeCups);
      if (energyEl) energyEl.textContent = String(currentEnergyCups);

      const totalMg = (currentCoffeeCups * 80) + (currentEnergyCups * 150);

      if (badgeEl) {
        badgeEl.innerHTML = `<span id="caffeine-display">${totalMg} mg</span>`;
      } else if (dispEl) {
        dispEl.textContent = `${totalMg} mg`;
      }
      if (mixEl) {
        mixEl.textContent = `Mix: ${currentCoffeeCups}x Kaffee · ${currentEnergyCups}x Energy (~${totalMg} mg)`;
      }
      updateCardSummaryBadges();
    }

    function addCaffeine(amount, type) {
      if (type && type.toLowerCase().includes('energy')) {
        changeEnergyDrink(amount);
      } else {
        changeCoffee(amount);
      }
    }

    // ==========================================
    // SLEEP & RECOVERY LOGIC
    // ==========================================
    function calculateSleepFromTimes() {
      const bed = document.getElementById('input-sleep-bedtime').value;
      const wake = document.getElementById('input-sleep-waketime').value;
      if (!bed || !wake) return;

      const [bH, bM] = bed.split(':').map(Number);
      const [wH, wM] = wake.split(':').map(Number);

      let bMinutes = bH * 60 + bM;
      let wMinutes = wH * 60 + wM;
      if (wMinutes < bMinutes) wMinutes += 24 * 60; // Next day wrap

      const diffHours = ((wMinutes - bMinutes) / 60).toFixed(2);
      document.getElementById('input-sleep-duration').value = diffHours;
      updateSleepDurationDisplay();
    }

    function updateSleepDurationDisplay() {
      const dur = parseFloat(document.getElementById('input-sleep-duration').value) || 0;
      const badge = document.getElementById('sleep-badge');
      const qualLabels = ['', 'Sehr schlecht', 'Unruhig', 'Geht so', 'Erholsam', 'Perfekt'];
      if (badge) {
        badge.innerText = `${dur} Std · ${qualLabels[currentSleepQuality] || 'Erholsam'}`;
      }
    }

    function setSleepQuality(qual) {
      currentSleepQuality = parseInt(qual) || 4;
      const sel = document.getElementById('select-sleep-quality');
      if (sel && parseInt(sel.value) !== currentSleepQuality) {
        sel.value = String(currentSleepQuality);
      }
      const labels = {
        1: '1 / 5 · Sehr schlecht',
        2: '2 / 5 · Schlecht',
        3: '3 / 5 · Mittelmäßig',
        4: '4 / 5 · Gut & ausreichend',
        5: '5 / 5 · Sehr erholsam & tief'
      };
      const lbl = document.getElementById('sleep-quality-label');
      if (lbl) lbl.textContent = labels[currentSleepQuality] || (currentSleepQuality + ' / 5');

      document.querySelectorAll('.sleep-qual-btn').forEach(btn => {
        if (parseInt(btn.getAttribute('data-qual')) === currentSleepQuality) {
          btn.className = 'sleep-qual-btn active py-2 rounded-lg border border-indigo-500 bg-indigo-50 dark:bg-indigo-950/60 text-center transition font-bold shadow-xs flex flex-col items-center justify-center';
        } else {
          btn.className = 'sleep-qual-btn py-2 rounded-lg border border-slate-200 dark:border-slate-700 text-center transition flex flex-col items-center justify-center hover:bg-slate-50 dark:hover:bg-slate-800/60';
        }
      });
      updateSleepDurationDisplay();
    }

    function toggleSleepTag(tag) {
      if (selectedSleepTags.has(tag)) selectedSleepTags.delete(tag);
      else selectedSleepTags.add(tag);
      renderSleepTagChips();
    }

    function formatTagDisplay(tag) {
      if (!tag) return '';
      const trimmed = tag.trim();
      if (trimmed.startsWith('#')) return trimmed;
      return '#' + trimmed;
    }

    function renderGenericChipGroup({ containerId, categoryKey, defaults, customs = [], activeSet, toggleFnName, activeClass, inactiveClass, isHashtag = false }) {
      const container = document.getElementById(containerId);
      if (!container) return;

      const defaultsHtml = defaults.map(item => {
        const isSelected = activeSet.has(item);
        const displayLabel = isHashtag ? formatTagDisplay(item) : item;
        return `
          <button type="button" onclick="${toggleFnName}('${escapeHtml(item)}')" class="text-xs px-2.5 py-1 rounded-full border transition ${isSelected ? activeClass : inactiveClass}" data-tag="${escapeHtml(item)}">
            ${escapeHtml(displayLabel)}
          </button>
        `;
      }).join('');

      const customsHtml = customs.map(item => {
        const isSelected = activeSet.has(item);
        const displayLabel = isHashtag ? formatTagDisplay(item) : item;
        return `
          <span class="inline-flex items-center text-xs rounded-full border transition ${isSelected ? activeClass : inactiveClass}">
            <button type="button" onclick="${toggleFnName}('${escapeHtml(item)}')" class="py-1 pl-2.5 pr-1 focus:outline-none">
              ${escapeHtml(displayLabel)}
            </button>
            <button type="button" onclick="event.stopPropagation(); deleteCustomOptionByName('${categoryKey}', '${escapeHtml(item)}')" class="pr-2 pl-0.5 py-1 text-slate-400 hover:text-rose-500 font-bold text-sm leading-none transition" title="Löschen">×</button>
          </span>
        `;
      }).join('');

      container.innerHTML = defaultsHtml + customsHtml;
    }

    function renderSleepTagChips() {
      renderGenericChipGroup({
        containerId: 'sleep-factors-chips-container',
        categoryKey: 'sleep_factors',
        defaults: DEFAULT_SLEEP_FACTORS,
        customs: customOptions.sleep_factors || [],
        activeSet: selectedSleepTags,
        toggleFnName: 'toggleSleepTag',
        activeClass: 'border-indigo-500 bg-indigo-100 dark:bg-indigo-950/70 text-indigo-900 dark:text-indigo-200 font-bold shadow-xs',
        inactiveClass: 'border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium'
      });
    }

    // ==========================================
    // STEPS & MOVEMENT LOGIC
    // ==========================================
    function addSteps(amount) {
      const input = document.getElementById('input-steps-count');
      const cur = parseInt(input.value) || 0;
      input.value = cur + amount;
      updateStepsProgressDisplay();
    }

    function setSteps(val) {
      const input = document.getElementById('input-steps-count');
      input.value = val;
      updateStepsProgressDisplay();
    }

    function updateStepsProgressDisplay() {
      const steps = parseInt(document.getElementById('input-steps-count').value) || 0;
      const goal = parseInt(document.getElementById('input-steps-goal').value) || 10000;
      const pct = Math.min(100, Math.round((steps / goal) * 100));

      const bar = document.getElementById('steps-progress-bar');
      const text = document.getElementById('steps-progress-percent');
      const badge = document.getElementById('steps-display-badge');

      if (bar) bar.style.width = pct + '%';
      if (text) text.innerText = `${pct}% erreicht (${steps.toLocaleString('de-DE')} / ${goal.toLocaleString('de-DE')})`;
      if (badge) badge.innerText = `${steps.toLocaleString('de-DE')} Schritte`;
    }

    function toggleActivityTag(tag) {
      if (selectedActivities.has(tag)) selectedActivities.delete(tag);
      else selectedActivities.add(tag);
      renderActivitiesChips();
    }

    function renderActivitiesChips() {
      renderGenericChipGroup({
        containerId: 'activities-chips-container',
        categoryKey: 'activities',
        defaults: DEFAULT_ACTIVITIES,
        customs: customOptions.activities || [],
        activeSet: selectedActivities,
        toggleFnName: 'toggleActivityTag',
        activeClass: 'border-blue-500 bg-blue-100 dark:bg-blue-950/70 text-blue-900 dark:text-blue-200 font-bold shadow-xs',
        inactiveClass: 'border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium'
      });
    }

    function renderMealTagChips() {
      renderGenericChipGroup({
        containerId: 'meal-tags-container',
        categoryKey: 'meal_tags',
        defaults: DEFAULT_MEAL_TAGS,
        customs: customOptions.meal_tags || [],
        activeSet: selectedMealTags,
        toggleFnName: 'toggleMealTag',
        activeClass: 'border-amber-500 bg-amber-100 dark:bg-amber-950/70 text-amber-900 dark:text-amber-200 font-bold shadow-xs',
        inactiveClass: 'border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium'
      });
    }

    function renderMemoryTagChips() {
      renderGenericChipGroup({
        containerId: 'memory-tags-container',
        categoryKey: 'memory_tags',
        defaults: DEFAULT_MEMORY_TAGS,
        customs: customOptions.memory_tags || [],
        activeSet: selectedMemoryTags,
        toggleFnName: 'toggleMemoryTag',
        activeClass: 'border-amber-500 bg-amber-100 dark:bg-amber-950/70 text-amber-900 dark:text-amber-200 font-bold shadow-xs',
        inactiveClass: 'border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium',
        isHashtag: true
      });
    }

    // ==========================================
    // ADHD & NEURO-FOKUS LOGIC
    // ==========================================
    function updateAdhsFocusScore(val) {
      val = parseInt(val);
      document.getElementById('input-adhs-focus').value = val;
      const badge = document.getElementById('adhs-focus-badge');
      if (badge) badge.innerText = `${val} / 10`;
    }

    function updateAdhsRestlessnessScore(val) {
      val = parseInt(val);
      document.getElementById('input-adhs-restlessness').value = val;
      const badge = document.getElementById('adhs-restlessness-badge');
      if (badge) badge.innerText = `${val} / 10`;
    }

    function updateAdhsBrainFogScore(val) {
      val = parseInt(val);
      document.getElementById('input-adhs-brainfog').value = val;
      const badge = document.getElementById('adhs-brainfog-badge');
      if (badge) badge.innerText = `${val} / 10`;
    }

    function setExecutiveFunction(val) {
      currentExecutiveFunction = val || 'gut';
      const sel = document.getElementById('select-adhs-executive');
      if (sel && sel.value !== currentExecutiveFunction) {
        sel.value = currentExecutiveFunction;
      }
      document.querySelectorAll('.exec-btn').forEach(btn => {
        if (btn.getAttribute('data-val') === val) {
          btn.className = 'exec-btn active text-xs px-2.5 py-1 rounded-lg border border-indigo-500 bg-indigo-50 dark:bg-indigo-950/60 text-indigo-700 dark:text-indigo-300 font-bold';
        } else {
          btn.className = 'exec-btn text-xs px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700';
        }
      });
    }

    function setSensoryOverload(val) {
      currentSensoryOverload = val || 'gering';
      const sel = document.getElementById('select-adhs-sensory');
      if (sel && sel.value !== currentSensoryOverload) {
        sel.value = currentSensoryOverload;
      }
      document.querySelectorAll('.sensory-btn').forEach(btn => {
        if (btn.getAttribute('data-val') === val) {
          btn.className = 'sensory-btn active text-xs px-2.5 py-1 rounded-lg border border-emerald-500 bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 font-bold';
        } else {
          btn.className = 'sensory-btn text-xs px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700';
        }
      });
    }

    // ==========================================
    // MEMORIES, POSITIVES & NOTES LOGIC
    // ==========================================
    function toggleMemoryTag(tag) {
      if (selectedMemoryTags.has(tag)) selectedMemoryTags.delete(tag);
      else selectedMemoryTags.add(tag);
      renderMemoryTagChips();
    }

    function updatePositiveThingsCounter() {
      const inputs = document.querySelectorAll('#positive-things-inputs-container input');
      let filled = 0;
      inputs.forEach(inp => {
        if (inp.value.trim().length > 0) filled++;
      });
      const counterEl = document.getElementById('positive-things-counter');
      if (counterEl) {
        counterEl.innerText = `${filled} / 3 notiert ${filled >= 3 ? '✓' : ''}`;
        counterEl.className = filled >= 3 
          ? 'text-xs font-extrabold text-emerald-600 dark:text-emerald-400' 
          : 'text-xs font-semibold text-slate-500';
      }
    }

    function addAnotherPositiveThingInput() {
      const container = document.getElementById('positive-things-inputs-container');
      const count = container.querySelectorAll('input').length + 1;
      const row = document.createElement('div');
      row.className = 'flex items-center gap-2';
      row.innerHTML = `
        <span class="w-6 h-6 rounded-lg bg-emerald-100 dark:bg-emerald-950/70 text-emerald-700 dark:text-emerald-300 font-bold text-xs flex items-center justify-center shrink-0">${count}</span>
        <input type="text" oninput="updatePositiveThingsCounter()" placeholder="Ein weiterer positiver Moment..." class="flex-1 min-w-0 shadcn-input py-1.5 px-2.5 text-xs block">
      `;
      container.appendChild(row);
      row.querySelector('input').focus();
    }

    // Copy routine from previous day
    function copyRoutineFromPreviousDay() {
      const entries = getStoredDiaryEntries();
      const currentDate = document.getElementById('input-diary-date').value;
      const prev = entries
        .filter(e => e.date < currentDate)
        .sort((a, b) => b.date.localeCompare(a.date))[0];

      if (!prev) {
        showToast('Kein vorheriger Eintrag gefunden zum Kopieren.', false);
        return;
      }

      if (Array.isArray(prev.medications) && prev.medications.length > 0) {
        currentDayMedications = prev.medications.map(m => ({
          ...m,
          id: 'med_' + Date.now() + '_' + Math.random().toString(36).substr(2, 4),
          taken: true
        }));
        renderMedicationsList();
      }

      if (prev.stepGoal) document.getElementById('input-steps-goal').value = prev.stepGoal;
      if (prev.waterGoal) currentWaterGoal = prev.waterGoal;
      updateStepsProgressDisplay();
      updateWaterDisplay();

      showToast(`Routine vom ${formatDateDE(prev.date)} übernommen!`);
    }

    // Collect & Save Diary Form Data
    function getDiaryFormData() {
      const moodVal = parseInt(document.getElementById('diary-mood-slider').value) || 8;
      const energyVal = parseInt(document.getElementById('diary-energy-slider').value) || 7;
      const dateVal = document.getElementById('input-diary-date').value || new Date().toISOString().split('T')[0];

      // Positives
      const posInputs = document.querySelectorAll('#positive-things-inputs-container input');
      const positiveThings = [];
      posInputs.forEach(inp => {
        if (inp.value.trim()) positiveThings.push(inp.value.trim());
      });

      // Meals
      const meals = {
        breakfast: (document.getElementById('input-meal-breakfast')?.value || '').trim(),
        lunch: (document.getElementById('input-meal-lunch')?.value || '').trim(),
        dinner: (document.getElementById('input-meal-dinner')?.value || '').trim(),
        snacks: (document.getElementById('input-meal-snacks')?.value || '').trim()
      };

      // Sleep
      const sleepDuration = parseFloat(document.getElementById('input-sleep-duration')?.value) || 0;
      const sleepBed = (document.getElementById('input-sleep-bedtime')?.value || '').trim();
      const sleepWake = (document.getElementById('input-sleep-waketime')?.value || '').trim();

      // Steps
      const steps = parseInt(document.getElementById('input-steps-count')?.value) || 0;
      const stepGoal = parseInt(document.getElementById('input-steps-goal')?.value) || 10000;

      // ADHD
      const adhs = {
        focus: parseInt(document.getElementById('input-adhs-focus')?.value) || 7,
        restlessness: parseInt(document.getElementById('input-adhs-restlessness')?.value) || 4,
        brainFog: parseInt(document.getElementById('input-adhs-brainfog')?.value) || 2,
        executiveFunction: currentExecutiveFunction || 'gut',
        sensoryOverload: currentSensoryOverload || 'gering',
        notes: (document.getElementById('input-adhs-notes')?.value || '').trim()
      };

      return {
        id: currentDiaryEntryId || ('diary_' + Date.now()),
        date: dateVal,
        mood: moodVal,
        energy: energyVal,
        emotions: Array.from(selectedDiaryEmotions),
        emotionNotes: { ...diaryEmotionNotes },
        highlights: document.getElementById('input-diary-highlights').value.trim(),
        memoryTags: Array.from(selectedMemoryTags),
        positiveThings: positiveThings,
        notes: document.getElementById('input-diary-notes').value.trim(),
        // New Tracking Dimensions
        medications: [...currentDayMedications],
        medEfficacy: (document.getElementById('input-med-efficacy')?.value || '').trim(),
        medEfficacyRating: currentMedEfficacyRating || '',
        rebound: {
          level: currentReboundLevel || 'none',
          time: (document.getElementById('input-med-rebound-time')?.value || '').trim(),
          notes: (document.getElementById('input-med-rebound-notes')?.value || '').trim()
        },
        meals: meals,
        mealTags: Array.from(selectedMealTags),
        waterMl: currentWaterMl || 0,
        waterGoal: currentWaterGoal || 2500,
        coffeeCups: currentCoffeeCups || 0,
        energyCups: currentEnergyCups || 0,
        caffeineCups: (currentCoffeeCups + currentEnergyCups) || 0,
        caffeineMg: (currentCoffeeCups * 80 + currentEnergyCups * 150),
        sleep: {
          durationHours: sleepDuration,
          bedTime: sleepBed,
          wakeTime: sleepWake,
          quality: currentSleepQuality || 4,
          tags: Array.from(selectedSleepTags)
        },
        steps: steps,
        stepGoal: stepGoal,
        activities: Array.from(selectedActivities),
        adhs: adhs,
        updatedAt: new Date().toISOString()
      };
    }

    function setDiaryFormData(data) {
      currentDiaryEntryId = data.id || null;
      document.getElementById('input-diary-date').value = data.date || new Date().toISOString().split('T')[0];
      updateDiaryDateDisplay();
      updateMoodScore(data.mood || 8);
      updateEnergyScore(data.energy || 7);

      selectedDiaryEmotions = new Set(data.emotions || []);
      diaryEmotionNotes = { ...(data.emotionNotes || {}) };
      updateEmotionChipStyles();
      renderEmotionNoteSegments();

      document.getElementById('input-diary-highlights').value = data.highlights || '';
      document.getElementById('input-diary-notes').value = data.notes || '';

      // Positives
      const container = document.getElementById('positive-things-inputs-container');
      const pts = data.positiveThings || [];
      container.innerHTML = `
        <div class="flex items-center gap-2.5">
          <span class="w-8 h-8 rounded-xl bg-emerald-100 dark:bg-emerald-950/70 text-emerald-700 dark:text-emerald-300 font-bold text-xs flex items-center justify-center flex-shrink-0 text-center shadow-xs">1</span>
          <input type="text" id="input-pos-1" value="${escapeHtml(pts[0] || '')}" oninput="updatePositiveThingsCounter()" placeholder="z. B. Ein ruhiger, wärmender Morgenkaffee..." class="notebook-input-area py-2.5">
        </div>
        <div class="flex items-center gap-2.5">
          <span class="w-8 h-8 rounded-xl bg-emerald-100 dark:bg-emerald-950/70 text-emerald-700 dark:text-emerald-300 font-bold text-xs flex items-center justify-center flex-shrink-0 text-center shadow-xs">2</span>
          <input type="text" id="input-pos-2" value="${escapeHtml(pts[1] || '')}" oninput="updatePositiveThingsCounter()" placeholder="z. B. Ein unerwartetes Lächeln oder schönes Feedback..." class="notebook-input-area py-2.5">
        </div>
        <div class="flex items-center gap-2.5">
          <span class="w-8 h-8 rounded-xl bg-emerald-100 dark:bg-emerald-950/70 text-emerald-700 dark:text-emerald-300 font-bold text-xs flex items-center justify-center flex-shrink-0 text-center shadow-xs">3</span>
          <input type="text" id="input-pos-3" value="${escapeHtml(pts[2] || '')}" oninput="updatePositiveThingsCounter()" placeholder="z. B. Zeit genommen für mich und durchgeatmet..." class="notebook-input-area py-2.5">
        </div>
      `;

      if (pts.length > 3) {
        for (let i = 3; i < pts.length; i++) {
          const row = document.createElement('div');
          row.className = 'flex items-center gap-2.5';
          row.innerHTML = `
            <span class="w-8 h-8 rounded-xl bg-emerald-100 dark:bg-emerald-950/70 text-emerald-700 dark:text-emerald-300 font-bold text-xs flex items-center justify-center flex-shrink-0 text-center shadow-xs">${i+1}</span>
            <input type="text" value="${escapeHtml(pts[i])}" oninput="updatePositiveThingsCounter()" class="notebook-input-area py-2.5">
          `;
          container.appendChild(row);
        }
      }
      updatePositiveThingsCounter();

      // Memory Tags
      selectedMemoryTags = new Set(data.memoryTags || []);
      renderMemoryTagChips();

      // Medications
      currentDayMedications = Array.isArray(data.medications) ? JSON.parse(JSON.stringify(data.medications)) : [];
      renderMedicationsList();

      // Med Efficacy
      setMedEfficacyRating(data.medEfficacyRating || '');
      if (document.getElementById('input-med-efficacy')) {
        document.getElementById('input-med-efficacy').value = data.medEfficacy || '';
      }

      // Rebound
      const reb = data.rebound || {};
      setReboundLevel(reb.level || 'none');
      if (document.getElementById('input-med-rebound-time')) document.getElementById('input-med-rebound-time').value = reb.time || '';
      if (document.getElementById('input-med-rebound-notes')) document.getElementById('input-med-rebound-notes').value = reb.notes || '';

      // Meals
      const mls = data.meals || {};
      if (document.getElementById('input-meal-breakfast')) document.getElementById('input-meal-breakfast').value = mls.breakfast || '';
      if (document.getElementById('input-meal-lunch')) document.getElementById('input-meal-lunch').value = mls.lunch || '';
      if (document.getElementById('input-meal-dinner')) document.getElementById('input-meal-dinner').value = mls.dinner || '';
      if (document.getElementById('input-meal-snacks')) document.getElementById('input-meal-snacks').value = mls.snacks || '';
      selectedMealTags = new Set(data.mealTags || []);
      renderMealTagChips();

      // Water & Caffeine
      currentWaterMl = typeof data.waterMl === 'number' ? data.waterMl : 0;
      currentWaterGoal = data.waterGoal || 2500;
      updateWaterDisplay();
      currentCoffeeCups = typeof data.coffeeCups === 'number' ? data.coffeeCups : (typeof data.caffeineCups === 'number' ? data.caffeineCups : 0);
      currentEnergyCups = typeof data.energyCups === 'number' ? data.energyCups : 0;
      currentCaffeineCups = currentCoffeeCups + currentEnergyCups;
      updateCaffeineDisplay();

      // Sleep
      const slp = data.sleep || {};
      if (document.getElementById('input-sleep-duration')) document.getElementById('input-sleep-duration').value = slp.durationHours || 7.5;
      if (document.getElementById('input-sleep-bedtime')) document.getElementById('input-sleep-bedtime').value = slp.bedTime || '';
      if (document.getElementById('input-sleep-waketime')) document.getElementById('input-sleep-waketime').value = slp.wakeTime || '';
      setSleepQuality(slp.quality || 4);
      selectedSleepTags = new Set(slp.tags || []);
      renderSleepTagChips();
      updateSleepDurationDisplay();

      // Steps
      const stp = typeof data.steps === 'number' ? data.steps : 0;
      const stpGoal = data.stepGoal || 10000;
      if (document.getElementById('input-steps-count')) document.getElementById('input-steps-count').value = stp;
      if (document.getElementById('input-steps-goal')) document.getElementById('input-steps-goal').value = stpGoal;
      selectedActivities = new Set(data.activities || []);
      renderActivitiesChips();
      updateStepsProgressDisplay();

      // ADHD
      const ad = data.adhs || {};
      updateAdhsFocusScore(ad.focus || 7);
      updateAdhsRestlessnessScore(ad.restlessness || 4);
      updateAdhsBrainFogScore(ad.brainFog || 2);
      setExecutiveFunction(ad.executiveFunction || 'gut');
      setSensoryOverload(ad.sensoryOverload || 'gering');
      if (document.getElementById('input-adhs-notes')) document.getElementById('input-adhs-notes').value = ad.notes || '';

      updateCardSummaryBadges();
    }

    function saveCurrentDiaryEntry() {
      const data = getDiaryFormData();
      const entries = getStoredDiaryEntries();

      const existingIndex = entries.findIndex(e => e.id === data.id);
      if (existingIndex >= 0) entries[existingIndex] = data;
      else entries.unshift(data);

      saveStoredDiaryEntries(entries);
      currentDiaryEntryId = data.id;
      showToast('Tagebucheintrag gespeichert!');
      switchView('diary-list');
    }

    function createNewDiaryEntry() {
      currentDiaryEntryId = null;
      initDefaultDates();
      updateMoodScore(8);
      updateEnergyScore(7);
      selectedDiaryEmotions.clear();
      diaryEmotionNotes = {};
      updateEmotionChipStyles();
      renderEmotionNoteSegments();
      document.getElementById('input-diary-highlights').value = '';
      document.getElementById('input-diary-notes').value = '';

      // Reset Positives
      const container = document.getElementById('positive-things-inputs-container');
      container.innerHTML = `
        <div class="flex items-center gap-2.5">
          <span class="w-8 h-8 rounded-xl bg-emerald-100 dark:bg-emerald-950/70 text-emerald-700 dark:text-emerald-300 font-bold text-xs flex items-center justify-center flex-shrink-0 text-center shadow-xs">1</span>
          <input type="text" id="input-pos-1" oninput="updatePositiveThingsCounter()" placeholder="z. B. Ein ruhiger, wärmender Morgenkaffee..." class="notebook-input-area py-2.5">
        </div>
        <div class="flex items-center gap-2.5">
          <span class="w-8 h-8 rounded-xl bg-emerald-100 dark:bg-emerald-950/70 text-emerald-700 dark:text-emerald-300 font-bold text-xs flex items-center justify-center flex-shrink-0 text-center shadow-xs">2</span>
          <input type="text" id="input-pos-2" oninput="updatePositiveThingsCounter()" placeholder="z. B. Ein unerwartetes Lächeln oder schönes Feedback..." class="notebook-input-area py-2.5">
        </div>
        <div class="flex items-center gap-2.5">
          <span class="w-8 h-8 rounded-xl bg-emerald-100 dark:bg-emerald-950/70 text-emerald-700 dark:text-emerald-300 font-bold text-xs flex items-center justify-center flex-shrink-0 text-center shadow-xs">3</span>
          <input type="text" id="input-pos-3" oninput="updatePositiveThingsCounter()" placeholder="z. B. Zeit genommen für mich und durchgeatmet..." class="notebook-input-area py-2.5">
        </div>
      `;
      updatePositiveThingsCounter();

      // Reset Meds & Meals
      currentDayMedications = [];
      renderMedicationsList();
      setMedEfficacyRating('');
      if (document.getElementById('input-med-efficacy')) document.getElementById('input-med-efficacy').value = '';
      setReboundLevel('none');
      if (document.getElementById('input-med-rebound-time')) document.getElementById('input-med-rebound-time').value = '';
      if (document.getElementById('input-med-rebound-notes')) document.getElementById('input-med-rebound-notes').value = '';

      if (document.getElementById('input-meal-breakfast')) document.getElementById('input-meal-breakfast').value = '';
      if (document.getElementById('input-meal-lunch')) document.getElementById('input-meal-lunch').value = '';
      if (document.getElementById('input-meal-dinner')) document.getElementById('input-meal-dinner').value = '';
      if (document.getElementById('input-meal-snacks')) document.getElementById('input-meal-snacks').value = '';
      selectedMealTags.clear();
      renderMealTagChips();

      // Reset Water, Sleep, Steps, ADHD
      currentWaterMl = 0;
      updateWaterDisplay();
      currentCoffeeCups = 0;
      currentEnergyCups = 0;
      currentCaffeineCups = 0;
      updateCaffeineDisplay();

      if (document.getElementById('input-sleep-duration')) document.getElementById('input-sleep-duration').value = 7.5;
      if (document.getElementById('input-sleep-bedtime')) document.getElementById('input-sleep-bedtime').value = '';
      if (document.getElementById('input-sleep-waketime')) document.getElementById('input-sleep-waketime').value = '';
      setSleepQuality(4);
      selectedSleepTags.clear();
      renderSleepTagChips();
      updateSleepDurationDisplay();

      if (document.getElementById('input-steps-count')) document.getElementById('input-steps-count').value = 0;
      selectedActivities.clear();
      renderActivitiesChips();
      updateStepsProgressDisplay();

      updateAdhsFocusScore(7);
      updateAdhsRestlessnessScore(4);
      updateAdhsBrainFogScore(2);
      setExecutiveFunction('gut');
      setSensoryOverload('gering');
      if (document.getElementById('input-adhs-notes')) document.getElementById('input-adhs-notes').value = '';

      selectedMemoryTags.clear();
      renderMemoryTagChips();
      updateCardSummaryBadges();

      switchView('diary-entry');
      showToast('Neuer Check-in geöffnet');
    }

    function resetDiaryFormWithConfirm() {
      if (confirm('Möchtest du das heutige Check-in Formular komplett zurücksetzen?')) {
        createNewDiaryEntry();
      }
    }

    // ==========================================
    // CHRONIK & JOURNAL RENDERING
    // ==========================================
    function setDiaryFolder(folderKey) {
      activeDiaryFolder = folderKey;
      renderDiaryFolders();
      renderDiaryEntriesList();
    }

    function setDiaryQuickFilter(qfKey) {
      activeDiaryQuickFilter = qfKey;
      document.querySelectorAll('.qf-btn').forEach(btn => {
        btn.className = 'qf-btn text-xs px-2.5 py-1 rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium transition';
      });
      const activeBtn = document.getElementById('qf-' + qfKey);
      if (activeBtn) {
        activeBtn.className = 'qf-btn active text-xs px-2.5 py-1 rounded-full border border-emerald-500 bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 font-bold transition';
      }
      renderDiaryEntriesList();
    }

    function renderDiaryFolders() {
      const entries = getStoredDiaryEntries();
      const container = document.getElementById('diary-folders-container');
      if (!container) return;

      const folders = {};
      entries.forEach(e => {
        if (!e.date) return;
        const key = e.date.substring(0, 7); // YYYY-MM
        folders[key] = (folders[key] || 0) + 1;
      });

      const sorted = Object.keys(folders).sort().reverse();
      let html = `
        <button type="button" onclick="setDiaryFolder('all')" class="px-2.5 py-1 rounded-lg text-xs font-semibold whitespace-nowrap transition ${activeDiaryFolder === 'all' ? 'bg-emerald-600 text-white shadow-xs' : 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300'}">
          Alle (${entries.length})
        </button>
      `;

      sorted.forEach(key => {
        const [y, m] = key.split('-');
        const dObj = new Date(parseInt(y), parseInt(m) - 1, 1);
        const label = dObj.toLocaleDateString('de-DE', { month: 'short', year: 'numeric' });
        html += `
          <button type="button" onclick="setDiaryFolder('${key}')" class="px-2.5 py-1 rounded-lg text-xs font-semibold whitespace-nowrap transition ${activeDiaryFolder === key ? 'bg-emerald-600 text-white shadow-xs' : 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300'}">
            ${label} (${folders[key]})
          </button>
        `;
      });

      container.innerHTML = html;
    }

    function renderDiaryEntriesList() {
      renderDiaryFolders();
      const entries = getStoredDiaryEntries();
      const container = document.getElementById('diary-entries-container');
      if (!container) return;

      const searchTerm = (document.getElementById('diary-search-input')?.value || '').toLowerCase().trim();

      const filtered = entries.filter(e => {
        // Folder filter
        if (activeDiaryFolder !== 'all' && (!e.date || !e.date.startsWith(activeDiaryFolder))) {
          return false;
        }

        // Quick tag filter
        if (activeDiaryQuickFilter === 'meds' && (!e.medications || e.medications.length === 0)) return false;
        if (activeDiaryQuickFilter === 'food' && (!e.meals || (!e.meals.breakfast && !e.meals.lunch && !e.meals.dinner))) return false;
        if (activeDiaryQuickFilter === 'steps' && ((e.steps || 0) < 8000)) return false;

        // Search term
        if (!searchTerm) return true;
        const matchesDate = e.date && e.date.toLowerCase().includes(searchTerm);
        const matchesHighlights = e.highlights && e.highlights.toLowerCase().includes(searchTerm);
        const matchesNotes = e.notes && e.notes.toLowerCase().includes(searchTerm);
        const matchesEmotions = (e.emotions || []).some(emo => emo.toLowerCase().includes(searchTerm));
        const matchesPos = (e.positiveThings || []).some(p => p.toLowerCase().includes(searchTerm));
        const matchesMeds = (e.medications || []).some(m => m.name.toLowerCase().includes(searchTerm) || (m.dose && m.dose.toLowerCase().includes(searchTerm)));
        const matchesMeals = e.meals && Object.values(e.meals).some(m => m && m.toLowerCase().includes(searchTerm));
        const matchesTags = (e.memoryTags || []).some(t => t.toLowerCase().includes(searchTerm));

        return matchesDate || matchesHighlights || matchesNotes || matchesEmotions || matchesPos || matchesMeds || matchesMeals || matchesTags;
      });

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="shadcn-card p-8 text-center space-y-3">
            <div class="w-12 h-12 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-400 mx-auto flex items-center justify-center text-xl">
              <svg class="w-6 h-6 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
            </div>
            <p class="text-sm font-bold text-slate-800 dark:text-slate-200">Keine Tagebucheinträge im ausgewählten Filter</p>
            <p class="text-xs text-slate-500 max-w-sm mx-auto">Notiere deinen täglichen Check-in mit Medis, Essen, Schlaf, Steps und Stimmung.</p>
            <button onclick="createNewDiaryEntry()" class="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold transition shadow-xs">
              + Neuen Check-in verfassen
            </button>
          </div>
        `;
        return;
      }

      container.innerHTML = filtered.map(item => {
        const moodConf = MOOD_CONFIG[item.mood || 5] || MOOD_CONFIG[5];
        const dateObj = new Date(item.date);
        const formattedFullDate = dateObj.toLocaleDateString('de-DE', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });

        const slp = item.sleep || {};
        const steps = item.steps || 0;
        const meds = Array.isArray(item.medications) ? item.medications : [];
        const mls = item.meals || {};
        const water = item.waterMl || 0;
        const caffeine = item.caffeineCups || 0;
        const adhs = item.adhs || {};

        return `
          <article class="diary-page-card p-3 sm:p-5 space-y-3 break-words overflow-hidden">
            
            <!-- Card Header: Date & Mood Badge & Action Buttons -->
            <div class="flex flex-wrap items-center justify-between pb-2.5 border-b border-slate-100 dark:border-slate-800 gap-2">
              <div class="min-w-0">
                <span class="text-[10px] font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Daily Life & Neuro Entry</span>
                <h3 class="text-sm sm:text-base font-extrabold text-slate-900 dark:text-white capitalize">${formattedFullDate}</h3>
              </div>

              <div class="flex items-center gap-1.5">
                <div class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-bold ${moodConf.bg} shadow-xs">
                  <span>${moodConf.emoji}</span>
                  <span>${item.mood}/10 · ${moodConf.title.split('/')[0].trim()}</span>
                </div>

                <div class="flex items-center gap-1">
                  <button onclick="editDiaryEntry('${item.id}')" class="p-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 text-xs transition" title="Bearbeiten">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
                  </button>
                  <button onclick="deleteDiaryEntry('${item.id}')" class="p-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-rose-500 hover:bg-rose-50 dark:hover:bg-rose-950/40 text-xs transition" title="Löschen">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                  </button>
                </div>
              </div>
            </div>

            <!-- Quick Metrics Overview Bar -->
            <div class="flex flex-wrap items-center gap-1 pt-0.5">
              ${slp.durationHours ? `
                <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-xs font-bold bg-indigo-50 dark:bg-indigo-950/50 text-indigo-700 dark:text-indigo-300 border border-indigo-200/50 dark:border-indigo-800/40">
                  <span>Schlaf:</span> ${slp.durationHours}h (${slp.quality || 4}/5)
                </span>
              ` : ''}

              ${steps > 0 ? `
                <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-xs font-bold bg-blue-50 dark:bg-blue-950/50 text-blue-700 dark:text-blue-300 border border-blue-200/50 dark:border-blue-800/40">
                  <span>Schritte:</span> ${steps.toLocaleString('de-DE')}
                </span>
              ` : ''}

              ${meds.length > 0 ? `
                <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-xs font-bold bg-violet-50 dark:bg-violet-950/50 text-violet-700 dark:text-violet-300 border border-violet-200/50 dark:border-violet-800/40">
                  <span>Medis:</span> ${meds.length}
                </span>
              ` : ''}

              ${water > 0 ? `
                <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-xs font-bold bg-sky-50 dark:bg-sky-950/50 text-sky-700 dark:text-sky-300 border border-sky-200/50 dark:border-sky-800/40">
                  <span>Wasser:</span> ${water} ml
                </span>
              ` : ''}

              ${(item.coffeeCups || item.energyCups || caffeine > 0) ? `
                <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-xs font-bold bg-amber-50 dark:bg-amber-950/50 text-amber-700 dark:text-amber-300 border border-amber-200/50 dark:border-amber-800/40">
                  ${item.coffeeCups !== undefined ? `${item.coffeeCups || 0}x Kaffee · ${item.energyCups || 0}x Energy` : `Koffein: ${caffeine}x`}
                </span>
              ` : ''}

              ${adhs.focus ? `
                <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-xs font-bold bg-violet-50 dark:bg-violet-950/50 text-violet-700 dark:text-violet-300 border border-violet-200/50 dark:border-violet-800/40">
                  <span>Fokus:</span> ${adhs.focus}/10
                </span>
              ` : ''}
            </div>

            <!-- Key Highlights Box -->
            ${item.highlights ? `
              <div class="bg-amber-50/70 dark:bg-amber-950/30 border-l-4 border-amber-500 p-2.5 sm:p-3 rounded-r-xl space-y-1">
                <div class="text-[11px] font-bold uppercase tracking-wider text-amber-800 dark:text-amber-400 flex items-center justify-between">
                  <span>Key Highlights & Erlebnisse</span>
                </div>
                <p class="text-xs sm:text-sm text-slate-800 dark:text-slate-200 leading-relaxed font-medium">
                  ${escapeHtml(item.highlights)}
                </p>
                ${(item.memoryTags && item.memoryTags.length > 0) ? `
                  <div class="flex flex-wrap gap-1 pt-0.5">
                    ${item.memoryTags.map(t => `<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-100 dark:bg-amber-900/60 text-amber-800 dark:text-amber-300">#${escapeHtml(t)}</span>`).join('')}
                  </div>
                ` : ''}
              </div>
            ` : ''}

            <!-- Medications Details Box -->
            ${(meds.length > 0 || (item.rebound && item.rebound.level !== 'none')) ? `
              <div class="p-2.5 sm:p-3 rounded-xl border border-violet-100 dark:border-violet-900/40 bg-violet-50/40 dark:bg-violet-950/20 space-y-1.5">
                <div class="text-[11px] font-bold uppercase tracking-wider text-violet-800 dark:text-violet-400 flex items-center justify-between">
                  <span>Eingenommene Medikation & Supplements:</span>
                </div>
                <div class="flex flex-wrap gap-1">
                  ${meds.map(m => `
                    <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-lg bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200 text-xs border border-violet-200/60 dark:border-violet-800/50">
                      <span class="text-emerald-500 font-bold">✓</span>
                      <span class="font-bold">${escapeHtml(m.name)}</span>
                      <span class="text-violet-600 dark:text-violet-400 font-semibold">${escapeHtml(m.dose)}</span>
                      ${m.time ? `<span class="text-violet-600 dark:text-violet-400 text-[10px] font-bold">${escapeHtml(m.time)} Uhr</span>` : ''}
                    </span>
                  `).join('')}
                </div>
                ${(item.medEfficacyRating || item.medEfficacy) ? `
                  <div class="p-2 rounded-lg border border-violet-200/80 dark:border-violet-900/40 bg-violet-100/40 dark:bg-violet-950/30 space-y-0.5 text-xs">
                    <div class="text-[10px] font-bold uppercase tracking-wider text-violet-800 dark:text-violet-300 flex items-center gap-1">
                      <span>Wirkung der Medikation:</span>
                      ${item.medEfficacyRating ? `<span class="px-1.5 py-0.2 rounded bg-violet-600 text-white font-bold ml-1 text-[9px] uppercase">${escapeHtml(item.medEfficacyRating)}</span>` : ''}
                    </div>
                    ${item.medEfficacy ? `<p class="text-slate-700 dark:text-slate-300 italic leading-relaxed text-[11px]">${escapeHtml(item.medEfficacy)}</p>` : ''}
                  </div>
                ` : ''}
                ${(item.rebound && item.rebound.level && item.rebound.level !== 'none') ? `
                  <div class="text-[11px] text-violet-700 dark:text-violet-300 pt-0.5 font-medium flex items-center gap-1.5">
                    <strong>Rebound:</strong> ${escapeHtml(item.rebound.level)} ${item.rebound.time ? `(${escapeHtml(item.rebound.time)} Uhr)` : ''} ${item.rebound.notes ? `– ${escapeHtml(item.rebound.notes)}` : ''}
                  </div>
                ` : ''}
              </div>
            ` : ''}

            <!-- Meals Box -->
            ${(mls.breakfast || mls.lunch || mls.dinner || mls.snacks) ? `
              <div class="p-2.5 sm:p-3 rounded-xl border border-amber-100 dark:border-amber-900/40 bg-amber-50/30 dark:bg-amber-950/15 space-y-1.5">
                <div class="text-[11px] font-bold uppercase tracking-wider text-amber-800 dark:text-amber-400">
                  Mahlzeiten & Ernährung:
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-1.5 text-xs text-slate-700 dark:text-slate-300">
                  ${mls.breakfast ? `<div><strong class="text-slate-900 dark:text-white">Frühstück:</strong> ${escapeHtml(mls.breakfast)}</div>` : ''}
                  ${mls.lunch ? `<div><strong class="text-slate-900 dark:text-white">Mittag:</strong> ${escapeHtml(mls.lunch)}</div>` : ''}
                  ${mls.dinner ? `<div><strong class="text-slate-900 dark:text-white">Abend:</strong> ${escapeHtml(mls.dinner)}</div>` : ''}
                  ${mls.snacks ? `<div><strong class="text-slate-900 dark:text-white">Snacks:</strong> ${escapeHtml(mls.snacks)}</div>` : ''}
                </div>
              </div>
            ` : ''}

            <!-- ADHD & Body Details -->
            ${(adhs.notes || (item.activities && item.activities.length > 0) || (slp.tags && slp.tags.length > 0)) ? `
              <div class="p-2.5 sm:p-3 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/50 space-y-1.5 text-xs">
                ${(item.activities && item.activities.length > 0) ? `
                  <div class="flex items-center gap-1 flex-wrap">
                    <span class="text-slate-400 font-semibold">Sport:</span>
                    ${item.activities.map(a => `<span class="px-2 py-0.5 rounded-full bg-blue-100 dark:bg-blue-950/60 text-blue-800 dark:text-blue-300 text-[10px] font-bold">${escapeHtml(a)}</span>`).join('')}
                  </div>
                ` : ''}
                ${(slp.tags && slp.tags.length > 0) ? `
                  <div class="flex items-center gap-1 flex-wrap">
                    <span class="text-slate-400 font-semibold">Schlaf:</span>
                    ${slp.tags.map(t => `<span class="px-2 py-0.5 rounded-full bg-indigo-100 dark:bg-indigo-950/60 text-indigo-800 dark:text-indigo-300 text-[10px] font-bold">${escapeHtml(t)}</span>`).join('')}
                  </div>
                ` : ''}
                ${adhs.notes ? `
                  <div class="pt-0.5 text-slate-800 dark:text-slate-200">
                    <strong class="text-violet-600 dark:text-violet-400">ADHS-Erkenntnis:</strong> ${escapeHtml(adhs.notes)}
                  </div>
                ` : ''}
              </div>
            ` : ''}

            <!-- 3 Positive Things List -->
            ${(item.positiveThings && item.positiveThings.length > 0) ? `
              <div class="bg-emerald-50/60 dark:bg-emerald-950/20 border border-emerald-100 dark:border-emerald-900/40 rounded-xl p-2.5 sm:p-3 space-y-1.5">
                <div class="text-[11px] font-bold uppercase tracking-wider text-emerald-800 dark:text-emerald-400">
                  Das war heute positiv:
                </div>
                <div class="space-y-1">
                  ${item.positiveThings.map(pt => `
                    <div class="flex items-start gap-1.5 text-xs sm:text-sm text-slate-700 dark:text-slate-300">
                      <span class="text-emerald-500 font-bold mt-0.5">✓</span>
                      <span>${escapeHtml(pt)}</span>
                    </div>
                  `).join('')}
                </div>
              </div>
            ` : ''}

            <!-- Free Diary Notes -->
            ${item.notes ? `
              <div class="space-y-1 pt-1 border-t border-slate-100 dark:border-slate-800">
                <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Tagebuch-Notizen:</span>
                <p class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 whitespace-pre-line leading-relaxed font-sans">
                  ${escapeHtml(item.notes)}
                </p>
              </div>
            ` : ''}

          </article>
        `;
      }).join('');
    }

    function editDiaryEntry(id) {
      const entries = getStoredDiaryEntries();
      const item = entries.find(e => e.id === id);
      if (!item) return;
      setDiaryFormData(item);
      switchView('diary-entry');
    }

    function deleteDiaryEntry(id) {
      if (confirm('Diesen Tagebucheintrag wirklich unwiderruflich löschen?')) {
        const entries = getStoredDiaryEntries().filter(e => e.id !== id);
        saveStoredDiaryEntries(entries);
        renderDiaryEntriesList();
        showToast('Eintrag gelöscht');
      }
    }

    function printDiaryJournal() {
      window.print();
    }

    function exportDiaryJSON() {
      const data = getStoredDiaryEntries();
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `diary_journal_backup_${new Date().toISOString().split('T')[0]}.json`;
      a.click();
      URL.revokeObjectURL(url);
    }

    function importDiaryJSON(e) {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (evt) => {
        try {
          const parsed = JSON.parse(evt.target.result);
          if (Array.isArray(parsed)) {
            saveStoredDiaryEntries(parsed);
            renderDiaryEntriesList();
            showToast('Tagebuch erfolgreich importiert!');
          }
        } catch (err) {
          alert('Ungültige JSON Datei');
        }
      };
      reader.readAsText(file);
    }

    function ensureInitialDiary() {
      const entries = getStoredDiaryEntries();
      if (entries.length === 0) {
        const today = new Date().toISOString().split('T')[0];
        const sample = {
          id: 'diary_sample_1',
          date: today,
          mood: 8,
          energy: 7,
          emotions: ['Freude', 'Dankbarkeit', 'Fokus'],
          emotionNotes: {
            'Freude': 'Schöner Spaziergang in der Mittagssonne und leckeres Essen.',
            'Dankbarkeit': 'Mein Kollege hat mir bei einer kniffligen Aufgabe unkompliziert geholfen.',
            'Fokus': 'Konnte morgens im Hyperfokus 2 Stunden hochkonzentriert programmieren.'
          },
          highlights: 'Wichtiges Feature erfolgreich gelauncht und am Abend Zeit zum Durchatmen genommen.',
          memoryTags: ['Erfolg', 'Natur', 'DopaminWin'],
          positiveThings: [
            'Den Morgen ohne Hektik mit Rührei und Kaffee begonnen',
            'Ein freundliches Lächeln und Lob von einem Kollegen',
            '35 Minuten draußen an der frischen Luft spaziert'
          ],
          notes: 'Ein rundum guter Tag. Die Medikation hat gut gegriffen, proteinreiches Frühstück hat das Nachmittagstief spürbar abgefedert.',
          medications: [
            { id: 'm1', name: 'Elvanse Adult', dose: '30 mg', time: '08:15', note: 'zum Frühstück', taken: true },
            { id: 'm2', name: 'Magnesium Bisglycinat', dose: '400 mg', time: '21:30', note: 'vor dem Schlafen', taken: true }
          ],
          medEfficacy: 'Fokus setzte sanft nach ca. 40 Minuten ein, stabiler Flow über 6 Stunden ohne Herzrasen.',
          medEfficacyRating: 'optimal',
          rebound: { level: 'leicht', time: '17:00', notes: 'Leichte Müdigkeit und Verlangen nach Pause' },
          meals: {
            breakfast: '3 Rühreier mit Vollkornbrot und Tomaten',
            lunch: 'Hähnchen-Reis-Bowl mit Brokkoli',
            dinner: 'Gemüsesuppe mit Avocado',
            snacks: 'Handvoll Mandeln und 1 Apfel'
          },
          mealTags: ['Proteinreich', 'Ausgewogen'],
          waterMl: 2500,
          waterGoal: 2500,
          caffeineCups: 2,
          sleep: {
            durationHours: 7.75,
            bedTime: '23:15',
            wakeTime: '07:00',
            quality: 4,
            tags: ['Erholt aufgewacht']
          },
          steps: 8640,
          stepGoal: 10000,
          activities: ['Spaziergang'],
          adhs: {
            focus: 8,
            restlessness: 3,
            brainFog: 2,
            executiveFunction: 'gut',
            sensoryOverload: 'gering',
            notes: 'Pomodoro-Technik mit Lo-Fi Musik hat hervorragend funktioniert!'
          },
          updatedAt: new Date().toISOString()
        };
        saveStoredDiaryEntries([sample]);
      }
    }

    // ==========================================
    // MODULE B: STATISTIKEN & NEURO-TRENDS LOGIC
    // ==========================================
    function setStatsTimeframe(days) {
      activeStatsDays = days;
      document.querySelectorAll('.stats-time-btn').forEach(btn => {
        const d = btn.getAttribute('data-days');
        if (d == days) {
          btn.className = 'stats-time-btn flex-1 sm:flex-initial px-3 py-1.5 rounded-lg text-xs font-bold transition active bg-white dark:bg-slate-900 text-sky-700 dark:text-sky-300 shadow-xs';
        } else {
          btn.className = 'stats-time-btn flex-1 sm:flex-initial px-3 py-1.5 rounded-lg text-xs font-medium text-slate-600 dark:text-slate-400 transition';
        }
      });
      renderStatsView();
    }

    function renderStatsView() {
      const entries = getStoredDiaryEntries();
      const now = new Date();

      const filtered = entries.filter(e => {
        if (!e.date) return false;
        const eDate = new Date(e.date);
        if (activeStatsDays === 'all') return true;
        if (activeStatsDays === 'month') {
          return eDate.getFullYear() === now.getFullYear() && eDate.getMonth() === now.getMonth();
        }
        const diffDays = (now - eDate) / (1000 * 60 * 60 * 24);
        return diffDays <= parseInt(activeStatsDays);
      });

      const chartEntries = [...filtered].sort((a, b) => new Date(a.date) - new Date(b.date));

      // 1. Avg Mood & Trend
      let totalMood = 0;
      chartEntries.forEach(e => totalMood += (e.mood || 5));
      const avgMood = chartEntries.length > 0 ? (totalMood / chartEntries.length).toFixed(1) : '--';
      document.getElementById('stats-kpi-avg').innerText = avgMood !== '--' ? `${avgMood} / 10` : '--';

      const trendEl = document.getElementById('stats-kpi-trend');
      if (chartEntries.length >= 4) {
        const mid = Math.floor(chartEntries.length / 2);
        const firstHalf = chartEntries.slice(0, mid);
        const secondHalf = chartEntries.slice(mid);
        const avg1 = firstHalf.reduce((acc, c) => acc + (c.mood || 5), 0) / firstHalf.length;
        const avg2 = secondHalf.reduce((acc, c) => acc + (c.mood || 5), 0) / secondHalf.length;
        const diff = (avg2 - avg1).toFixed(1);
        if (diff > 0.3) trendEl.innerHTML = `<span class="text-emerald-500 font-bold">+${diff} ↑ Steigend</span>`;
        else if (diff < -0.3) trendEl.innerHTML = `<span class="text-rose-500 font-bold">${diff} ↓ Sinkend</span>`;
        else trendEl.innerHTML = `<span class="text-slate-400 font-medium">±0.0 → Stabil</span>`;
      } else {
        trendEl.innerText = 'Mehr Daten für Trend nötig';
      }

      // 2. Avg Sleep
      let sleepSum = 0;
      let sleepQualSum = 0;
      let sleepCount = 0;
      chartEntries.forEach(e => {
        if (e.sleep && e.sleep.durationHours > 0) {
          sleepSum += e.sleep.durationHours;
          sleepQualSum += (e.sleep.quality || 3);
          sleepCount++;
        }
      });
      const avgSleep = sleepCount > 0 ? (sleepSum / sleepCount).toFixed(1) : '--';
      const avgSleepQual = sleepCount > 0 ? (sleepQualSum / sleepCount).toFixed(1) : '--';
      document.getElementById('stats-kpi-sleep').innerText = avgSleep !== '--' ? `${avgSleep} h` : '--';
      document.getElementById('stats-kpi-sleep-qual').innerText = avgSleepQual !== '--' ? `Ø ${avgSleepQual} / 5 Qualität` : '--';

      // 3. Avg Steps
      let stepsSum = 0;
      let stepsCount = 0;
      chartEntries.forEach(e => {
        if (typeof e.steps === 'number') {
          stepsSum += e.steps;
          stepsCount++;
        }
      });
      const avgSteps = stepsCount > 0 ? Math.round(stepsSum / stepsCount) : '--';
      document.getElementById('stats-kpi-steps').innerText = avgSteps !== '--' ? avgSteps.toLocaleString('de-DE') : '--';
      document.getElementById('stats-kpi-steps-total').innerText = `${stepsSum.toLocaleString('de-DE')} Schritte gesamt`;

      // 4. Med Adherence
      let medsDays = 0;
      chartEntries.forEach(e => {
        if (Array.isArray(e.medications) && e.medications.length > 0) medsDays++;
      });
      const adherencePct = chartEntries.length > 0 ? Math.round((medsDays / chartEntries.length) * 100) : 0;
      document.getElementById('stats-kpi-meds').innerText = `${adherencePct}%`;

      // 5. Avg Focus
      let focusSum = 0;
      let focusCount = 0;
      chartEntries.forEach(e => {
        if (e.adhs && e.adhs.focus) {
          focusSum += e.adhs.focus;
          focusCount++;
        }
      });
      const avgFocus = focusCount > 0 ? (focusSum / focusCount).toFixed(1) : '--';
      document.getElementById('stats-kpi-focus').innerText = avgFocus !== '--' ? `${avgFocus} / 10` : '--';

      // 6. Streak
      const allSortedDates = Array.from(new Set(entries.map(e => e.date))).sort().reverse();
      let streak = 0;
      let checkDate = new Date();
      checkDate.setHours(0, 0, 0, 0);

      for (const dStr of allSortedDates) {
        const d = new Date(dStr);
        d.setHours(0, 0, 0, 0);
        const diff = Math.round((checkDate - d) / (1000 * 60 * 60 * 24));
        if (diff === 0 || diff === 1) {
          streak++;
          checkDate = d;
        } else {
          break;
        }
      }
      document.getElementById('stats-kpi-streak').innerText = streak > 0 ? `${streak} d` : '0 d';

      // Charts & Insights
      renderDualTimelineChart(chartEntries);
      renderWeekdayTendency(entries);
      renderTopEmotions(filtered);
      renderNeuroInsights(chartEntries);
    }

    // Render Dual-Line Responsive SVG Chart (Mood & Focus)
    function renderDualTimelineChart(items) {
      const container = document.getElementById('stats-chart-container');
      if (!container) return;

      if (items.length < 2) {
        container.innerHTML = `
          <div class="text-xs text-slate-400 italic py-8 text-center">
            Mindestens 2 Tage im Zeitraum erforderlich für den Kurvenverlauf.
          </div>
        `;
        return;
      }

      const w = Math.max(260, container.clientWidth || 300);
      const h = 180;
      const padL = 24;
      const padR = 12;
      const padT = 16;
      const padB = 26;

      const innerW = w - padL - padR;
      const innerH = h - padT - padB;
      const stepX = innerW / (items.length - 1);

      // Mood Points
      const moodPoints = items.map((item, idx) => {
        const x = padL + (idx * stepX);
        const val = item.mood || 5;
        const y = padT + (innerH - ((val - 1) / 9) * innerH);
        return { x, y, val: val, date: item.date };
      });

      // Focus Points
      const focusPoints = items.map((item, idx) => {
        const x = padL + (idx * stepX);
        const val = (item.adhs && item.adhs.focus) ? item.adhs.focus : 5;
        const y = padT + (innerH - ((val - 1) / 9) * innerH);
        return { x, y, val: val, date: item.date };
      });

      const polyMood = moodPoints.map(p => `${p.x.toFixed(1)},${p.y.toFixed(1)}`).join(' ');
      const polyFocus = focusPoints.map(p => `${p.x.toFixed(1)},${p.y.toFixed(1)}`).join(' ');

      container.innerHTML = `
        <svg viewBox="0 0 ${w} ${h}" class="w-full h-full overflow-hidden block">
          <!-- Horizontal Grid Lines -->
          <line x1="${padL}" y1="${padT}" x2="${w - padR}" y2="${padT}" stroke="#94a3b8" stroke-dasharray="2 3" stroke-opacity="0.3"/>
          <text x="${padL - 4}" y="${padT + 3}" fill="#94a3b8" font-size="9" text-anchor="end" font-weight="600">10</text>

          <line x1="${padL}" y1="${padT + innerH / 2}" x2="${w - padR}" y2="${padT + innerH / 2}" stroke="#94a3b8" stroke-dasharray="2 3" stroke-opacity="0.3"/>
          <text x="${padL - 4}" y="${padT + innerH / 2 + 3}" fill="#94a3b8" font-size="9" text-anchor="end" font-weight="600">5</text>

          <line x1="${padL}" y1="${padT + innerH}" x2="${w - padR}" y2="${padT + innerH}" stroke="#94a3b8" stroke-dasharray="2 3" stroke-opacity="0.3"/>
          <text x="${padL - 4}" y="${padT + innerH + 3}" fill="#94a3b8" font-size="9" text-anchor="end" font-weight="600">1</text>

          <!-- Polylines -->
          <polyline points="${polyMood}" fill="none" stroke="#10b981" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
          <polyline points="${polyFocus}" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="4 3" stroke-linecap="round" stroke-linejoin="round"/>

          <!-- Circles for Mood -->
          ${moodPoints.map((p, idx) => `
            <g class="cursor-pointer" onclick="showToast('${formatDateDE(p.date)}: Stimmung ${p.val}/10')">
              <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="3.5" fill="#ffffff" stroke="#10b981" stroke-width="2"/>
              <text x="${p.x.toFixed(1)}" y="${h - 6}" fill="#64748b" font-size="8.5" text-anchor="middle" font-weight="500">
                ${p.date ? p.date.substring(8, 10) + '.' : ''}
              </text>
            </g>
          `).join('')}

          <!-- Circles for Focus -->
          ${focusPoints.map((p, idx) => `
            <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="3" fill="#ffffff" stroke="#8b5cf6" stroke-width="2" class="cursor-pointer" onclick="showToast('${formatDateDE(p.date)}: ADHS-Fokus ${p.val}/10')"/>
          `).join('')}
        </svg>
      `;
    }

    function renderWeekdayTendency(entries) {
      const container = document.getElementById('stats-weekday-bars');
      if (!container) return;

      const days = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'];
      const stats = [
        { sum: 0, count: 0 }, { sum: 0, count: 0 }, { sum: 0, count: 0 },
        { sum: 0, count: 0 }, { sum: 0, count: 0 }, { sum: 0, count: 0 }, { sum: 0, count: 0 }
      ];

      entries.forEach(e => {
        if (!e.date) return;
        const d = new Date(e.date);
        let dayIdx = d.getDay() - 1;
        if (dayIdx === -1) dayIdx = 6;
        stats[dayIdx].sum += (e.mood || 5);
        stats[dayIdx].count += 1;
      });

      container.innerHTML = days.map((dayName, idx) => {
        const item = stats[idx];
        const avg = item.count > 0 ? (item.sum / item.count).toFixed(1) : 0;
        const pct = item.count > 0 ? (avg / 10) * 100 : 0;
        return `
          <div class="flex items-center gap-2 text-xs">
            <span class="w-6 font-bold text-slate-600 dark:text-slate-400">${dayName}</span>
            <div class="flex-1 bg-slate-100 dark:bg-slate-800 h-3 rounded-full overflow-hidden flex">
              <div class="bg-gradient-to-r from-emerald-500 to-teal-500 rounded-full transition-all duration-300" style="width: ${pct}%"></div>
            </div>
            <span class="w-10 text-right font-bold text-slate-700 dark:text-slate-300">${item.count > 0 ? avg : '-'}</span>
          </div>
        `;
      }).join('');
    }

    function renderTopEmotions(entries) {
      const container = document.getElementById('stats-top-emotions');
      if (!container) return;

      const counts = {};
      entries.forEach(e => {
        (e.emotions || []).forEach(emo => {
          counts[emo] = (counts[emo] || 0) + 1;
        });
      });

      const sorted = Object.entries(counts).sort((a, b) => b[1] - a[1]).slice(0, 5);
      if (sorted.length === 0) {
        container.innerHTML = `<div class="text-xs text-slate-400 italic py-4">Noch keine Emotionen erfasst.</div>`;
        return;
      }

      const maxCount = sorted[0][1] || 1;
      container.innerHTML = sorted.map(([emo, count]) => {
        const pct = Math.round((count / maxCount) * 100);
        const isPleasant = PLEASANT_EMOTIONS.includes(emo);
        return `
          <div class="space-y-1 text-xs">
            <div class="flex justify-between items-center font-medium">
              <span class="text-slate-800 dark:text-slate-200 font-semibold">${escapeHtml(emo)}</span>
              <span class="text-slate-500">${count}x</span>
            </div>
            <div class="w-full bg-slate-100 dark:bg-slate-800 h-2.5 rounded-full overflow-hidden flex">
              <div class="${isPleasant ? 'bg-emerald-500' : 'bg-amber-500'} rounded-full transition-all duration-300" style="width: ${pct}%"></div>
            </div>
          </div>
        `;
      }).join('');
    }

    function renderNeuroInsights(items) {
      const el = document.getElementById('stats-insight-text');
      if (!el) return;

      if (items.length < 3) {
        el.innerText = 'Trage mindestens 3 Tage lang deine Medis, Mahlzeiten, Schlaf und Schritte ein, um automatisierte Auswertungen über dein Nervensystem zu erhalten.';
        return;
      }

      // Check sleep vs focus correlation
      const goodSleepEntries = items.filter(e => e.sleep && e.sleep.durationHours >= 7);
      const lowSleepEntries = items.filter(e => e.sleep && e.sleep.durationHours > 0 && e.sleep.durationHours < 7);

      let insight = '';
      if (goodSleepEntries.length > 0 && lowSleepEntries.length > 0) {
        const avgGoodFocus = (goodSleepEntries.reduce((acc, c) => acc + ((c.adhs && c.adhs.focus) || 5), 0) / goodSleepEntries.length).toFixed(1);
        const avgLowFocus = (lowSleepEntries.reduce((acc, c) => acc + ((c.adhs && c.adhs.focus) || 5), 0) / lowSleepEntries.length).toFixed(1);
        insight += `<strong>Schlaf & Fokus:</strong> An Tagen mit ≥ 7 Std Schlaf lag dein mentaler Fokus im Schnitt bei <strong>${avgGoodFocus}/10</strong> (gegenüber ${avgLowFocus}/10 bei Schlafmangel). `;
      }

      // Check steps vs mood
      const highSteps = items.filter(e => (e.steps || 0) >= 8000);
      if (highSteps.length > 0) {
        const avgMoodActive = (highSteps.reduce((acc, c) => acc + (c.mood || 5), 0) / highSteps.length).toFixed(1);
        insight += `<br><strong>Bewegung:</strong> An Tagen mit über 8.000 Schritten lag deine durchschnittliche Stimmung bei <strong>${avgMoodActive}/10</strong>.`;
      }

      if (!insight) {
        insight = 'Deine Daten zeigen eine solide Ausgeglichenheit. Achte weiterhin auf ausreichend Wasser und proteinreiche Mahlzeiten vor deiner Medikation!';
      }

      el.innerHTML = insight;
    }

    function printStatsSummary() {
      window.print();
    }

    // ==========================================
    // HELPERS & TOAST
    // ==========================================
    function formatDateDE(dateStr) {
      if (!dateStr) return '';
      try {
        if (typeof dateStr === 'string' && dateStr.includes('-')) {
          const parts = dateStr.split('T')[0].split('-');
          if (parts.length === 3) {
            return `${parts[2]}.${parts[1]}.${parts[0]}`;
          }
        }
        const d = new Date(dateStr);
        if (!isNaN(d.getTime())) {
          return d.toLocaleDateString('de-DE', { day: '2-digit', month: '2-digit', year: 'numeric' });
        }
        return String(dateStr);
      } catch (e) {
        return String(dateStr);
      }
    }

    function escapeHtml(str) {
      if (!str) return '';
      return String(str).replace(/[&<>"']/g, function(m) {
        return {
          '&': '&amp;',
          '<': '&lt;',
          '>': '&gt;',
          '"': '&quot;',
          "'": '&#039;'
        }[m];
      });
    }

    let toastTimeout = null;
    function showToast(message, isSuccess = true) {
      const toast = document.getElementById('toast');
      const msgEl = document.getElementById('toast-message');
      const iconEl = document.getElementById('toast-icon');

      if (!toast) return;
      msgEl.innerText = message;
      iconEl.innerText = isSuccess ? '✓' : 'ℹ';
      iconEl.className = isSuccess ? 'text-emerald-400 font-bold' : 'text-sky-400 font-bold';

      toast.classList.remove('-translate-y-20', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');

      if (toastTimeout) clearTimeout(toastTimeout);
      toastTimeout = setTimeout(() => {
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('-translate-y-20', 'opacity-0');
      }, 2300);
    }

    // PWA Service Worker Registration
    function registerServiceWorker() {
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('sw.js?v=16').then((reg) => {
          reg.update().catch(() => {});
          reg.addEventListener('updatefound', () => {
            const newWorker = reg.installing;
            if (newWorker) {
              newWorker.addEventListener('statechange', () => {
                if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                  showToast('App aktualisiert! Lade neu...');
                  setTimeout(() => window.location.reload(), 1000);
                }
              });
            }
          });
        }).catch(err => {
          console.log('SW notice:', err);
        });

        let refreshing = false;
        navigator.serviceWorker.addEventListener('controllerchange', () => {
          if (!refreshing) {
            refreshing = true;
            window.location.reload();
          }
        });
      }
    }

    async function forceAppUpdate() {
      showToast('Cache wird geleert...');
      try {
        if ('caches' in window) {
          const keys = await caches.keys();
          await Promise.all(keys.map(k => caches.delete(k)));
        }
        if ('serviceWorker' in navigator) {
          const regs = await navigator.serviceWorker.getRegistrations();
          for (let reg of regs) await reg.unregister();
        }
      } catch (e) {
        console.error(e);
      }
      setTimeout(() => {
        window.location.href = window.location.pathname + '?v=' + Date.now();
      }, 400);
    }

    let deferredPrompt = null;
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      deferredPrompt = e;
      const installBtn = document.getElementById('btn-pwa-install');
      if (installBtn) installBtn.classList.remove('hidden');
    });

    function triggerPwaInstall() {
      if (deferredPrompt) {
        deferredPrompt.prompt();
        deferredPrompt.userChoice.then((choiceResult) => {
          deferredPrompt = null;
          const installBtn = document.getElementById('btn-pwa-install');
          if (installBtn) installBtn.classList.add('hidden');
        });
      } else {
        alert('Tippe im Browser-Menü auf "Zum Startbildschirm hinzufügen" oder "App installieren".');
      }
    }

    window.addEventListener('appinstalled', () => {
      showToast('Erfolgreich als App installiert!');
      const installBtn = document.getElementById('btn-pwa-install');
      if (installBtn) installBtn.classList.add('hidden');
      deferredPrompt = null;
    });
  </script>
</body>
</html>
'''
