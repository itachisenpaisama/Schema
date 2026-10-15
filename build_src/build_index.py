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

  <!-- Google Fonts: Plus Jakarta Sans (UI) + Inter + Kalam & Caveat (Handwritten Look) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Inter:wght@400;500;600;700;800&family=Kalam:wght@400;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
            sheet: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
            handKalam: ['Kalam', 'cursive'],
            handCaveat: ['Caveat', 'cursive']
          },
          colors: {
            brand: {
              50: '#f0f9ff',
              100: '#e0f2fe',
              500: '#0284c7',
              600: '#0369a1',
              700: '#075985',
              900: '#0c4a6e',
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

    /* shadcn Card Container */
    .shadcn-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 1rem;
      box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.03);
      transition: border-color 0.15s ease;
    }
    .dark .shadcn-card {
      background: #0f172a;
      border-color: #1e293b;
      box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.2);
    }

    /* shadcn Input Base */
    .shadcn-input {
      display: block;
      width: 100%;
      max-width: 100%;
      box-sizing: border-box;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 0.75rem;
      padding: 0.55rem 0.75rem;
      font-size: 0.875rem;
      line-height: 1.4;
      color: #0f172a;
      transition: all 0.15s ease;
      outline: none;
    }
    .dark .shadcn-input {
      background: rgba(30, 41, 59, 0.6);
      border-color: #334155;
      color: #f8fafc;
    }
    .shadcn-input:focus {
      background: #ffffff;
      border-color: #0284c7;
      box-shadow: 0 0 0 2px rgba(2, 132, 199, 0.15);
    }
    .dark .shadcn-input:focus {
      background: #0f172a;
      border-color: #38bdf8;
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
    }

    /* Dedicated Textarea styling: guarantee block layout and clean height */
    textarea.shadcn-input {
      display: block;
      width: 100%;
      max-width: 100%;
      box-sizing: border-box;
      min-height: 4.25rem;
      resize: vertical;
      line-height: 1.5;
    }

    /* Notebook Input Area */
    .notebook-input-area {
      width: 100%;
      background: #f8fafc;
      border: 1.5px solid #cbd5e1;
      border-radius: 0.75rem;
      padding: 0.65rem 0.85rem;
      font-size: 0.9rem;
      color: #0f172a;
      transition: all 0.2s ease;
    }
    .dark .notebook-input-area {
      background: #0f172a;
      border-color: #334155;
      color: #f8fafc;
    }
    .notebook-input-area:focus {
      outline: none;
      background: #ffffff;
      border-color: #059669;
      box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.15);
    }
    .dark .notebook-input-area:focus {
      background: #0f172a;
      border-color: #10b981;
      box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.25);
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
      background: #e2e8f0;
      transition: background 0.2s ease;
    }
    .dark input[type=range]::-webkit-slider-runnable-track {
      background: #334155;
    }
    input[type=range]::-webkit-slider-thumb {
      -webkit-appearance: none;
      height: 18px;
      width: 18px;
      border-radius: 50%;
      background: #ffffff;
      border: 2px solid #0284c7;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.15);
      margin-top: -6px;
      transition: transform 0.1s ease;
    }
    input[type=range]:active::-webkit-slider-thumb {
      transform: scale(1.15);
    }

    /* Worksheet Paper Styling */
    .sheet-paper {
      background-color: #ffffff;
      color: #0f172a;
      box-shadow: 0 2px 10px -2px rgba(0, 0, 0, 0.05);
      border: 1px solid #e2e8f0;
      position: relative;
    }
    .dark .sheet-paper {
      background-color: #0f172a;
      color: #f8fafc;
      border-color: #1e293b;
      box-shadow: 0 2px 10px -2px rgba(0, 0, 0, 0.35);
    }

    /* Dotted Line Rule */
    .dotted-rule {
      border-bottom: 1.5px dotted #64748b;
      min-height: 24px;
      display: flex;
      align-items: flex-end;
      padding-bottom: 2px;
      width: 100%;
    }
    .dark .dotted-rule {
      border-bottom-color: #475569;
    }

    /* Bottom Navigation Active Glow */
    .bottom-nav-btn.active {
      color: #0284c7;
    }
    .dark .bottom-nav-btn.active {
      color: #38bdf8;
    }
    .bottom-nav-btn.active .nav-icon-wrapper {
      background-color: #e0f2fe;
    }
    .dark .bottom-nav-btn.active .nav-icon-wrapper {
      background-color: rgba(14, 165, 233, 0.2);
    }

    /* Diary Book Entry Styling */
    .diary-page-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 1rem;
      box-shadow: 0 1px 4px -1px rgba(0, 0, 0, 0.03);
      position: relative;
    }
    .dark .diary-page-card {
      background: #0f172a;
      border-color: #1e293b;
      box-shadow: 0 1px 4px -1px rgba(0, 0, 0, 0.25);
    }

    /* Interactive Notebook Styling */
    .notebook-container {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 1rem;
      box-shadow: 0 1px 4px -1px rgba(0, 0, 0, 0.03);
      position: relative;
      overflow: hidden;
    }
    .dark .notebook-container {
      background: #0f172a;
      border-color: #1e293b;
      box-shadow: 0 1px 4px -1px rgba(0, 0, 0, 0.25);
    }

    .notebook-segment {
      padding: 1rem;
      border-bottom: 1px solid #f1f5f9;
      position: relative;
      transition: background-color 0.2s ease;
    }
    .dark .notebook-segment {
      border-bottom-color: #1e293b;
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
<body class="bg-slate-50 dark:bg-slate-950 text-slate-800 dark:text-slate-100 min-h-screen font-sans transition-colors duration-200">
'''
