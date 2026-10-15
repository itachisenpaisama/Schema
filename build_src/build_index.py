# -*- coding: utf-8 -*-

def get_head_and_styles():
    return '''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Schema-Memo & Daily Life Diary – Digitales Therapietagebuch & Neuro-Tracker</title>

  <!-- PWA & Mobile Web App Manifest & PNG Icons -->
  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#0f172a">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="SchemaMemo">
  <link rel="icon" type="image/png" sizes="192x192" href="icons/icon-192.png">
  <link rel="icon" type="image/png" sizes="512x512" href="icons/icon-512.png">
  <link rel="apple-touch-icon" sizes="192x192" href="icons/icon-192.png">

  <!-- Immediate Theme Initialization to prevent white flash / theme loss on restart -->
  <script>
    (function() {
      try {
        var rawSettings = localStorage.getItem('schema_settings_v1');
        var theme = 'auto';
        if (rawSettings) {
          var parsed = JSON.parse(rawSettings);
          if (parsed && parsed.theme) theme = parsed.theme;
        }
        if (theme === 'auto') {
          var legacy = localStorage.getItem('theme');
          if (legacy === 'dark' || legacy === 'light') theme = legacy;
        }
        var isDark = theme === 'dark' || (theme === 'auto' && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
        if (isDark) {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
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
       Mobile-First Polish & shadcn/ui Design Tokens
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

    /* Responsive auto-zoom prevention: ONLY on small mobile screens (<640px)
       On iPad/Tablet (>=640px) and Desktop, preserve exact typography without blowing up compact inputs */
    @media (max-width: 639px) {
      input:not([type="range"]):not([type="checkbox"]),
      select,
      textarea {
        font-size: 16px !important;
      }
    }

    /* Clean number inputs (hide bulky OS spin buttons that cause overflow on iPad) */
    input[type=number]::-webkit-inner-spin-button, 
    input[type=number]::-webkit-outer-spin-button { 
      -webkit-appearance: none; 
      margin: 0; 
    }
    input[type=number] {
      -moz-appearance: textfield;
    }

    /* Native date/time inputs on iOS/iPadOS Safari & Chrome */
    input[type="date"],
    input[type="time"] {
      min-height: 2.25rem;
      cursor: pointer;
    }

    /* Hide the small native clock icon on time inputs so clicking anywhere triggers the picker directly */
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

    /* Ensure all inputs and textareas have rigid box models and never overflow containers */
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

    /* shadcn Card Container - Stoic Warm Paper Elevation */
    .shadcn-card {
      background: #ffffff;
      border: 1px solid rgba(28, 25, 23, 0.08);
      border-radius: 1.25rem;
      box-shadow: 0 1px 2px rgba(28, 25, 23, 0.02), 0 8px 24px -4px rgba(28, 25, 23, 0.03);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .dark .shadcn-card {
      background: #181715;
      border-color: rgba(245, 243, 239, 0.07);
      box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.4);
    }

    /* shadcn Input Base - Tactile Natural Surfaces */
    .shadcn-input {
      display: block;
      width: 100%;
      max-width: 100%;
      box-sizing: border-box;
      background: #F4F2EC;
      border: 1px solid rgba(28, 25, 23, 0.1);
      border-radius: 0.85rem;
      padding: 0.6rem 0.85rem;
      font-size: 0.875rem;
      line-height: 1.45;
      color: #1C1917;
      transition: all 0.2s ease;
      outline: none;
    }
    .dark .shadcn-input {
      background: #1F1E1B;
      border-color: rgba(245, 243, 239, 0.1);
      color: #F5F3EF;
    }
    .shadcn-input:focus {
      background: #ffffff;
      border-color: #4A7264;
      box-shadow: 0 0 0 3px rgba(74, 114, 100, 0.14);
    }
    .dark .shadcn-input:focus {
      background: #181715;
      border-color: #7BA896;
      box-shadow: 0 0 0 3px rgba(123, 168, 150, 0.18);
    }

    /* Dedicated Textarea styling: guarantee block layout and clean height */
    textarea.shadcn-input {
      display: block;
      width: 100%;
      max-width: 100%;
      box-sizing: border-box;
      min-height: 4.5rem;
      resize: vertical;
      line-height: 1.6;
    }

    /* Notebook Input Area */
    .notebook-input-area {
      width: 100%;
      background: #F4F2EC;
      border: 1.5px solid rgba(28, 25, 23, 0.1);
      border-radius: 0.85rem;
      padding: 0.7rem 0.9rem;
      font-size: 0.9rem;
      color: #1C1917;
      transition: all 0.2s ease;
    }
    .dark .notebook-input-area {
      background: #1F1E1B;
      border-color: rgba(245, 243, 239, 0.1);
      color: #F5F3EF;
    }
    .notebook-input-area:focus {
      outline: none;
      background: #ffffff;
      border-color: #4A7264;
      box-shadow: 0 0 0 3px rgba(74, 114, 100, 0.14);
    }
    .dark .notebook-input-area:focus {
      background: #181715;
      border-color: #7BA896;
      box-shadow: 0 0 0 3px rgba(123, 168, 150, 0.18);
    }

    /* Range slider custom styling - Tactile Sage Track & Thumb */
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
      background: #E5E3DC;
      transition: background 0.2s ease;
    }
    .dark input[type=range]::-webkit-slider-runnable-track {
      background: #2B2926;
    }
    input[type=range]::-webkit-slider-thumb {
      -webkit-appearance: none;
      height: 20px;
      width: 20px;
      border-radius: 50%;
      background: #ffffff;
      border: 2.5px solid #4A7264;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.12);
      margin-top: -7px;
      transition: transform 0.15s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .dark input[type=range]::-webkit-slider-thumb {
      background: #181715;
      border-color: #7BA896;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    }
    input[type=range]:active::-webkit-slider-thumb {
      transform: scale(1.18);
    }

    /* Worksheet Paper Styling - Warm Tactile Parchment */
    .sheet-paper {
      background-color: #ffffff;
      color: #1C1917;
      box-shadow: 0 2px 14px -3px rgba(28, 25, 23, 0.06);
      border: 1px solid rgba(28, 25, 23, 0.08);
      position: relative;
    }
    .dark .sheet-paper {
      background-color: #181715;
      color: #F5F3EF;
      border-color: rgba(245, 243, 239, 0.07);
      box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.4);
    }

    /* Dotted Line Rule */
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

    /* Bottom Navigation Active State - Understated & Mindful */
    .bottom-nav-btn.active {
      color: #1C1917;
    }
    .dark .bottom-nav-btn.active {
      color: #F5F3EF;
    }
    .bottom-nav-btn.active .nav-icon-wrapper {
      background-color: rgba(74, 114, 100, 0.12);
      color: #35584D;
    }
    .dark .bottom-nav-btn.active .nav-icon-wrapper {
      background-color: rgba(123, 168, 150, 0.18);
      color: #9CC2B2;
    }

    /* Diary Book Entry Styling */
    .diary-page-card {
      background: #ffffff;
      border: 1px solid rgba(28, 25, 23, 0.08);
      border-radius: 1.25rem;
      box-shadow: 0 1px 3px rgba(28, 25, 23, 0.02), 0 6px 18px -4px rgba(28, 25, 23, 0.03);
      position: relative;
    }
    .dark .diary-page-card {
      background: #181715;
      border-color: rgba(245, 243, 239, 0.07);
      box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.35);
    }

    /* Interactive Notebook Styling */
    .notebook-container {
      background: #ffffff;
      border: 1px solid rgba(28, 25, 23, 0.08);
      border-radius: 1.25rem;
      box-shadow: 0 1px 3px rgba(28, 25, 23, 0.02), 0 6px 18px -4px rgba(28, 25, 23, 0.03);
      position: relative;
      overflow: hidden;
    }
    .dark .notebook-container {
      background: #181715;
      border-color: rgba(245, 243, 239, 0.07);
      box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.35);
    }

    .notebook-segment {
      padding: 1rem;
      border-bottom: 1px solid rgba(28, 25, 23, 0.06);
      position: relative;
      transition: background-color 0.2s ease;
    }
    .dark .notebook-segment {
      border-bottom-color: rgba(245, 243, 239, 0.06);
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
<body class="bg-[#FAF9F5] dark:bg-[#121110] text-[#1C1917] dark:text-[#F5F3EF] min-h-screen font-sans transition-colors duration-200">
'''
