# -*- coding: utf-8 -*-

def get_head_and_styles():
    return '''<!DOCTYPE html>
<html lang="de" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <meta name="description" content="Schema-Memo & Daily Life Diary - Ganzheitliche Selbstreflexion, Schematherapie, Medikation & Neuro-Trends">
  <meta name="theme-color" content="#FAF9F5" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#121110" media="(prefers-color-scheme: dark)">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <title>Schema-Memo & Daily Diary</title>

  <!-- PWA Manifest & Icons -->
  <link rel="manifest" href="manifest.json">
  <link rel="icon" type="image/svg+xml" href="icons/favicon.svg">
  <link rel="apple-touch-icon" sizes="192x192" href="icons/icon-192.png">

  <!-- Immediate Theme & Color Profile Initialization to prevent white flash / theme loss on restart -->
  <script>
    (function() {
      try {
        var rawSettings = localStorage.getItem('schema_settings_v1');
        var theme = 'auto';
        var profile = 'stoic';
        if (rawSettings) {
          var parsed = JSON.parse(rawSettings);
          if (parsed) {
            if (parsed.theme) theme = parsed.theme;
            if (parsed.colorProfile) profile = parsed.colorProfile;
          }
        }
        if (theme === 'auto') {
          var legacy = localStorage.getItem('theme');
          if (legacy === 'dark' || legacy === 'light') theme = legacy;
        }
        var legacyProfile = localStorage.getItem('color_profile');
        if (legacyProfile) profile = legacyProfile;

        var isDark = theme === 'dark' || (theme === 'auto' && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
        if (isDark) {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
        document.documentElement.setAttribute('data-theme-profile', profile);
      } catch (e) {}
    })();
  </script>

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Google Fonts: Lora (Editorial & Humanist) + Plus Jakarta Sans (UI) + Inter + Kalam & Caveat (Handwritten Look) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Inter:wght@400;500;600;700;800&family=Kalam:wght@400;700&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
            serif: ['Lora', 'Georgia', 'serif'],
            sheet: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
            handKalam: ['Kalam', 'cursive'],
            handCaveat: ['Caveat', 'cursive']
          },
          colors: {
            stoic: {
              bg: '#FAF9F5',
              darkbg: '#121110',
              card: '#FFFFFF',
              darkcard: '#181715',
              ink: '#1C1917',
              lightink: '#F5F3EF',
              muted: '#78716C',
              darkmuted: '#A8A29E',
              sage: '#4A7264',
              sagedark: '#6B9A88',
              amber: '#C27838',
              border: 'rgba(28, 25, 23, 0.08)',
              darkborder: 'rgba(245, 243, 239, 0.08)'
            },
            brand: {
              50: '#f6f7f5',
              100: '#eceee9',
              500: '#4A7264',
              600: '#3D5F53',
              700: '#2F4B41',
              900: '#1C2E28',
            }
          }
        }
      }
    }
  </script>

  <style>
    /* ==========================================================
       Mobile-First Polish & Base Tokens
       ========================================================== */
    * {
      -webkit-tap-highlight-color: transparent;
      box-sizing: border-box;
    }

    html, body {
      max-width: 100vw;
      overflow-x: hidden;
    }

    html {
      scroll-padding-top: 105px;
    }

    body {
      padding-bottom: calc(68px + env(safe-area-inset-bottom, 12px));
    }

    /* Hide scrollbar for clean touch swipe horizontal bars */
    .no-scrollbar::-webkit-scrollbar {
      display: none;
    }
    .no-scrollbar {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }

    /* Responsive auto-zoom prevention: ONLY on small mobile screens (<640px) */
    @media (max-width: 639px) {
      input:not([type="range"]):not([type="checkbox"]),
      select,
      textarea {
        font-size: 16px !important;
      }
    }

    /* Clean number inputs (hide bulky OS spin buttons) */
    input[type=number]::-webkit-inner-spin-button, 
    input[type=number]::-webkit-outer-spin-button { 
      -webkit-appearance: none; 
      margin: 0; 
    }
    input[type=number] {
      -moz-appearance: textfield;
    }

    /* Native date/time inputs */
    input[type="date"],
    input[type="time"] {
      min-height: 2.25rem;
      cursor: pointer;
    }

    /* Hide small native clock icon so clicking anywhere on the input opens the picker */
    input[type="time"]::-webkit-calendar-picker-indicator {
      display: none !important;
      -webkit-appearance: none !important;
      opacity: 0 !important;
      width: 0 !important;
      height: 0 !important;
      margin: 0 !important;
      padding: 0 !important;
      pointer-events: none !important;
    }

    input, select, textarea {
      max-width: 100%;
      box-sizing: border-box;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
      width: 4px;
      height: 4px;
    }
    ::-webkit-scrollbar-track {
      background: transparent;
    }
    ::-webkit-scrollbar-thumb {
      background: #cbd5e1;
      border-radius: 9999px;
    }
    .dark ::-webkit-scrollbar-thumb {
      background: #334155;
    }

    /* ==========================================================
       THEME COLOR PROFILES (CSS CUSTOM PROPERTIES)
       ========================================================== */
    :root, [data-theme-profile="stoic"] {
      --app-bg: #FAF9F5;
      --app-text: #1C1917;
      --card-bg: #FFFFFF;
      --card-border: rgba(28, 25, 23, 0.08);
      --input-bg: #F4F2EC;
      --input-border: rgba(28, 25, 23, 0.1);
      --accent-primary: #4A7264;
    }
    .dark, .dark[data-theme-profile="stoic"], [data-theme-profile="stoic"].dark {
      --app-bg: #121110;
      --app-text: #F5F3EF;
      --card-bg: #181715;
      --card-border: rgba(245, 243, 239, 0.07);
      --input-bg: #1F1E1B;
      --input-border: rgba(245, 243, 239, 0.1);
      --accent-primary: #6B9A88;
    }

    /* 2. Warm Sepia / Vintage Journal */
    [data-theme-profile="sepia"] {
      --app-bg: #F5EFE6;
      --app-text: #2A1F18;
      --card-bg: #FAF6F0;
      --card-border: rgba(42, 31, 24, 0.09);
      --input-bg: #EDE3D5;
      --input-border: rgba(42, 31, 24, 0.12);
      --accent-primary: #965B32;
    }
    .dark[data-theme-profile="sepia"], [data-theme-profile="sepia"].dark {
      --app-bg: #1A1410;
      --app-text: #EAE0D5;
      --card-bg: #231B15;
      --card-border: rgba(234, 224, 213, 0.08);
      --input-bg: #2D231C;
      --input-border: rgba(234, 224, 213, 0.12);
      --accent-primary: #C57E47;
    }

    /* 3. Forest & Sage */
    [data-theme-profile="sage"] {
      --app-bg: #EFF4F1;
      --app-text: #16241C;
      --card-bg: #F7FAF8;
      --card-border: rgba(22, 36, 28, 0.09);
      --input-bg: #E1ECE5;
      --input-border: rgba(22, 36, 28, 0.12);
      --accent-primary: #33614C;
    }
    .dark[data-theme-profile="sage"], [data-theme-profile="sage"].dark {
      --app-bg: #0E1612;
      --app-text: #DEEAE2;
      --card-bg: #15201A;
      --card-border: rgba(222, 234, 226, 0.08);
      --input-bg: #1C2B23;
      --input-border: rgba(222, 234, 226, 0.12);
      --accent-primary: #59987A;
    }

    /* 4. Nordic Slate */
    [data-theme-profile="nordic"] {
      --app-bg: #EEF2F6;
      --app-text: #16202B;
      --card-bg: #F7FAFC;
      --card-border: rgba(22, 32, 43, 0.09);
      --input-bg: #E0E7EE;
      --input-border: rgba(22, 32, 43, 0.12);
      --accent-primary: #325B7E;
    }
    .dark[data-theme-profile="nordic"], [data-theme-profile="nordic"].dark {
      --app-bg: #0D131A;
      --app-text: #DDE5ED;
      --card-bg: #141C24;
      --card-border: rgba(221, 229, 237, 0.08);
      --input-bg: #1C2631;
      --input-border: rgba(221, 229, 237, 0.12);
      --accent-primary: #5289B5;
    }

    /* 5. Terracotta & Sand */
    [data-theme-profile="terracotta"] {
      --app-bg: #F8F2EC;
      --app-text: #2D1E16;
      --card-bg: #FCF8F4;
      --card-border: rgba(45, 30, 22, 0.09);
      --input-bg: #EFE2D6;
      --input-border: rgba(45, 30, 22, 0.12);
      --accent-primary: #A8512C;
    }
    .dark[data-theme-profile="terracotta"], [data-theme-profile="terracotta"].dark {
      --app-bg: #19110B;
      --app-text: #EFE0D5;
      --card-bg: #221710;
      --card-border: rgba(239, 224, 213, 0.08);
      --input-bg: #2D1F16;
      --input-border: rgba(239, 224, 213, 0.12);
      --accent-primary: #D16E44;
    }

    /* 6. Lavender Dusk */
    [data-theme-profile="lavender"] {
      --app-bg: #F4F1F7;
      --app-text: #22192A;
      --card-bg: #FAF8FC;
      --card-border: rgba(34, 25, 42, 0.09);
      --input-bg: #E9E1F0;
      --input-border: rgba(34, 25, 42, 0.12);
      --accent-primary: #634785;
    }
    .dark[data-theme-profile="lavender"], [data-theme-profile="lavender"].dark {
      --app-bg: #130E19;
      --app-text: #E8DEEE;
      --card-bg: #1C1523;
      --card-border: rgba(232, 222, 238, 0.08);
      --input-bg: #261D30;
      --input-border: rgba(232, 222, 238, 0.12);
      --accent-primary: #8E6BB8;
    }

    /* 7. Matcha & Cream */
    [data-theme-profile="matcha"] {
      --app-bg: #F2F5EC;
      --app-text: #1E2517;
      --card-bg: #F9FAF4;
      --card-border: rgba(30, 37, 23, 0.09);
      --input-bg: #E3E9D7;
      --input-border: rgba(30, 37, 23, 0.12);
      --accent-primary: #4A662C;
    }
    .dark[data-theme-profile="matcha"], [data-theme-profile="matcha"].dark {
      --app-bg: #10150C;
      --app-text: #E2E8D8;
      --card-bg: #182012;
      --card-border: rgba(226, 232, 216, 0.08);
      --input-bg: #212B1A;
      --input-border: rgba(226, 232, 216, 0.12);
      --accent-primary: #759B46;
    }

    /* 8. Rose Quartz */
    [data-theme-profile="rose"] {
      --app-bg: #F7F1F2;
      --app-text: #2A191E;
      --card-bg: #FBF7F8;
      --card-border: rgba(42, 25, 30, 0.09);
      --input-bg: #ECE0E3;
      --input-border: rgba(42, 25, 30, 0.12);
      --accent-primary: #8E3E53;
    }
    .dark[data-theme-profile="rose"], [data-theme-profile="rose"].dark {
      --app-bg: #180D11;
      --app-text: #EEDEE2;
      --card-bg: #221318;
      --card-border: rgba(238, 222, 226, 0.08);
      --input-bg: #2E1B21;
      --input-border: rgba(238, 222, 226, 0.12);
      --accent-primary: #BA5D75;
    }

    /* 9. OLED Obsidian (Pure Black) */
    [data-theme-profile="obsidian"] {
      --app-bg: #F6F7F9;
      --app-text: #050505;
      --card-bg: #FFFFFF;
      --card-border: rgba(0, 0, 0, 0.1);
      --input-bg: #EBEEF2;
      --input-border: rgba(0, 0, 0, 0.14);
      --accent-primary: #171717;
    }
    .dark[data-theme-profile="obsidian"], [data-theme-profile="obsidian"].dark {
      --app-bg: #000000;
      --app-text: #F8F8F8;
      --card-bg: #0A0A0A;
      --card-border: rgba(255, 255, 255, 0.12);
      --input-bg: #141414;
      --input-border: rgba(255, 255, 255, 0.18);
      --accent-primary: #FFFFFF;
    }

    /* 10. E-Ink Pure Paper (Monochrome High Contrast) */
    [data-theme-profile="eink"] {
      --app-bg: #FFFFFF;
      --app-text: #000000;
      --card-bg: #FFFFFF;
      --card-border: #000000;
      --input-bg: #F4F4F4;
      --input-border: #222222;
      --accent-primary: #000000;
    }
    .dark[data-theme-profile="eink"], [data-theme-profile="eink"].dark {
      --app-bg: #080808;
      --app-text: #FFFFFF;
      --card-bg: #101010;
      --card-border: #666666;
      --input-bg: #1A1A1A;
      --input-border: #888888;
      --accent-primary: #FFFFFF;
    }

    /* Core Dynamic Theming Binding */
    body {
      background-color: var(--app-bg) !important;
      color: var(--app-text) !important;
    }

    header.sticky {
      background-color: var(--app-bg) !important;
      border-color: var(--card-border) !important;
    }

    nav#app-bottom-nav {
      background-color: var(--app-bg) !important;
      border-color: var(--card-border) !important;
    }

    .shadcn-card {
      background-color: var(--card-bg) !important;
      border: 1px solid var(--card-border) !important;
      border-radius: 1.25rem;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02), 0 8px 24px -4px rgba(0, 0, 0, 0.03);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .dark .shadcn-card {
      box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.4);
    }

    .shadcn-input {
      display: block;
      width: 100%;
      max-width: 100%;
      box-sizing: border-box;
      background-color: var(--input-bg) !important;
      border: 1px solid var(--input-border) !important;
      border-radius: 0.85rem;
      padding: 0.6rem 0.85rem;
      font-size: 0.875rem;
      line-height: 1.45;
      color: var(--app-text) !important;
      transition: all 0.2s ease;
      outline: none;
    }
    .shadcn-input:focus {
      border-color: var(--accent-primary) !important;
      box-shadow: 0 0 0 3px rgba(74, 114, 100, 0.15);
    }

    textarea.shadcn-input {
      display: block;
      width: 100%;
      max-width: 100%;
      box-sizing: border-box;
      min-height: 4.5rem;
      resize: vertical;
      line-height: 1.6;
    }

    .notebook-input-area {
      width: 100%;
      background-color: var(--input-bg) !important;
      border: 1.5px solid var(--input-border) !important;
      border-radius: 0.85rem;
      padding: 0.7rem 0.9rem;
      font-size: 0.9rem;
      color: var(--app-text) !important;
      transition: all 0.2s ease;
    }
    .notebook-input-area:focus {
      outline: none;
      border-color: var(--accent-primary) !important;
      box-shadow: 0 0 0 3px rgba(74, 114, 100, 0.15);
    }

    /* Range slider custom styling */
    input[type=range] {
      -webkit-appearance: none;
      background: transparent;
      cursor: pointer;
    }
    input[type=range]:focus {
      outline: none;
    }
    input[type=range]::-webkit-slider-runnable-track {
      height: 6px;
      border-radius: 9999px;
      background: var(--input-border);
      transition: background 0.2s ease;
    }
    input[type=range]::-webkit-slider-thumb {
      -webkit-appearance: none;
      height: 20px;
      width: 20px;
      border-radius: 50%;
      background: var(--card-bg);
      border: 2.5px solid var(--accent-primary);
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
      margin-top: -7px;
      transition: transform 0.15s cubic-bezier(0.16, 1, 0.3, 1);
    }
    input[type=range]:active::-webkit-slider-thumb {
      transform: scale(1.18);
    }

    /* Worksheet Paper Styling */
    .sheet-paper {
      background-color: var(--card-bg) !important;
      color: var(--app-text) !important;
      box-shadow: 0 2px 14px -3px rgba(0, 0, 0, 0.06);
      border: 1px solid var(--card-border) !important;
      position: relative;
    }

    .dotted-rule {
      border-bottom: 1.5px dotted #78716C;
      min-height: 24px;
      display: flex;
      align-items: flex-end;
      padding-bottom: 2px;
      width: 100%;
    }
    .dark .dotted-rule {
      border-bottom-color: #57534E;
    }

    /* Bottom Navigation Active State */
    .bottom-nav-btn.active {
      color: var(--app-text);
    }
    .bottom-nav-btn.active .nav-icon-wrapper {
      background-color: rgba(74, 114, 100, 0.15);
      color: var(--accent-primary);
    }

    /* Diary Book Entry Styling */
    .diary-page-card {
      background-color: var(--card-bg) !important;
      border: 1px solid var(--card-border) !important;
      border-radius: 1.25rem;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02), 0 6px 18px -4px rgba(0, 0, 0, 0.03);
      position: relative;
    }

    /* Interactive Notebook Styling */
    .notebook-container {
      background-color: var(--card-bg) !important;
      border: 1px solid var(--card-border) !important;
      border-radius: 1.25rem;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02), 0 6px 18px -4px rgba(0, 0, 0, 0.03);
      position: relative;
      overflow: hidden;
    }

    .notebook-segment {
      padding: 1rem;
      border-bottom: 1px solid var(--card-border);
      position: relative;
      transition: background-color 0.2s ease;
    }
    .notebook-segment:last-child {
      border-bottom: none;
    }
    @media (min-width: 640px) {
      .notebook-segment {
        padding: 1.25rem;
      }
    }

    /* Print Styles: Exact Din A4 Output */
    @media print {
      @page {
        size: A4 portrait;
        margin: 12mm 14mm 10mm 14mm;
      }
      body {
        background: #ffffff !important;
        color: #000000 !important;
        margin: 0 !important;
        padding: 0 !important;
      }
      .no-print {
        display: none !important;
      }
      .sheet-paper, .diary-page-card {
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        padding: 14px !important;
        margin-bottom: 20px !important;
        page-break-inside: avoid;
        width: 100% !important;
        max-width: 100% !important;
      }
      .dotted-rule {
        border-bottom: 1.5px dotted #000000 !important;
      }
    }
  </style>
</head>
<body class="min-h-screen font-sans transition-colors duration-200">
'''

get_head_html = get_head_and_styles
