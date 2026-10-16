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
       THEME COLOR PROFILES (16-TOKEN COMPLETE PALETTES)
       Rich, tangible, unmistakable tones in BOTH Light & Dark mode
       ========================================================== */
    :root, [data-theme-profile="stoic"] {
      --app-bg: #F7F5EE;
      --app-text: #1C1917;
      --text-muted: #78716C;
      --card-bg: #FFFFFF;
      --card-border: rgba(28, 25, 23, 0.12);
      --surface-subtle: #EFECE3;
      --surface-subtle-hover: #E5E1D5;
      --border-subtle: rgba(28, 25, 23, 0.08);
      --input-bg: #F4F1E9;
      --input-border: rgba(28, 25, 23, 0.16);
      --accent-primary: #385E4F;
      --accent-text: #FFFFFF;
      --accent-soft: rgba(56, 94, 79, 0.14);
      --accent-soft-border: rgba(56, 94, 79, 0.32);
      --badge-bg: #E8E4DA;
      --badge-text: #284739;
    }
    .dark, .dark[data-theme-profile="stoic"], [data-theme-profile="stoic"].dark {
      --app-bg: #121110;
      --app-text: #F5F3EF;
      --text-muted: #A8A29E;
      --card-bg: #191816;
      --card-border: rgba(245, 243, 239, 0.08);
      --surface-subtle: #22201D;
      --surface-subtle-hover: #2A2723;
      --border-subtle: rgba(245, 243, 239, 0.06);
      --input-bg: #22201D;
      --input-border: rgba(245, 243, 239, 0.12);
      --accent-primary: #6E9E8B;
      --accent-text: #121110;
      --accent-soft: rgba(110, 158, 139, 0.18);
      --accent-soft-border: rgba(110, 158, 139, 0.35);
      --badge-bg: #252320;
      --badge-text: #A1C9B9;
    }

    /* 2. Warm Sepia / Vintage Journal */
    [data-theme-profile="sepia"] {
      --app-bg: #EFE4D2;
      --app-text: #2D2015;
      --text-muted: #7A624E;
      --card-bg: #F8F2E7;
      --card-border: rgba(110, 72, 40, 0.22);
      --surface-subtle: #E5D5BF;
      --surface-subtle-hover: #DAC7AD;
      --border-subtle: rgba(110, 72, 40, 0.15);
      --input-bg: #ECE0CE;
      --input-border: rgba(110, 72, 40, 0.26);
      --accent-primary: #8C4A1D;
      --accent-text: #FFFFFF;
      --accent-soft: rgba(140, 74, 29, 0.16);
      --accent-soft-border: rgba(140, 74, 29, 0.38);
      --badge-bg: #DFCEB7;
      --badge-text: #723712;
    }
    .dark[data-theme-profile="sepia"], [data-theme-profile="sepia"].dark {
      --app-bg: #17120E;
      --app-text: #EFE5DC;
      --text-muted: #A89686;
      --card-bg: #221A14;
      --card-border: rgba(239, 229, 220, 0.09);
      --surface-subtle: #2D221A;
      --surface-subtle-hover: #382B21;
      --border-subtle: rgba(239, 229, 220, 0.06);
      --input-bg: #2D221A;
      --input-border: rgba(239, 229, 220, 0.14);
      --accent-primary: #C9783D;
      --accent-text: #17120E;
      --accent-soft: rgba(201, 120, 61, 0.2);
      --accent-soft-border: rgba(201, 120, 61, 0.38);
      --badge-bg: #31251D;
      --badge-text: #E09A67;
    }

    /* 3. Forest & Sage */
    [data-theme-profile="sage"] {
      --app-bg: #DCECE1;
      --app-text: #12241A;
      --text-muted: #4F6E5A;
      --card-bg: #ECF5EF;
      --card-border: rgba(32, 75, 52, 0.22);
      --surface-subtle: #D0E5D7;
      --surface-subtle-hover: #C0DCC9;
      --border-subtle: rgba(32, 75, 52, 0.15);
      --input-bg: #D9EDE1;
      --input-border: rgba(32, 75, 52, 0.26);
      --accent-primary: #225F40;
      --accent-text: #FFFFFF;
      --accent-soft: rgba(34, 95, 64, 0.16);
      --accent-soft-border: rgba(34, 95, 64, 0.38);
      --badge-bg: #C6DFCF;
      --badge-text: #18472E;
    }
    .dark[data-theme-profile="sage"], [data-theme-profile="sage"].dark {
      --app-bg: #0B140F;
      --app-text: #DCE9E0;
      --text-muted: #82A28F;
      --card-bg: #121E17;
      --card-border: rgba(220, 233, 224, 0.09);
      --surface-subtle: #192B21;
      --surface-subtle-hover: #22382C;
      --border-subtle: rgba(220, 233, 224, 0.06);
      --input-bg: #192B21;
      --input-border: rgba(220, 233, 224, 0.14);
      --accent-primary: #5BA47F;
      --accent-text: #0B140F;
      --accent-soft: rgba(91, 164, 127, 0.2);
      --accent-soft-border: rgba(91, 164, 127, 0.38);
      --badge-bg: #1E3328;
      --badge-text: #86C5A4;
    }

    /* 4. Nordic Slate */
    [data-theme-profile="nordic"] {
      --app-bg: #D9E6F2;
      --app-text: #101E2E;
      --text-muted: #4E6B88;
      --card-bg: #EAF2F9;
      --card-border: rgba(28, 68, 102, 0.22);
      --surface-subtle: #CDDFEF;
      --surface-subtle-hover: #BDD2E6;
      --border-subtle: rgba(28, 68, 102, 0.15);
      --input-bg: #D6E5F3;
      --input-border: rgba(28, 68, 102, 0.26);
      --accent-primary: #1D5584;
      --accent-text: #FFFFFF;
      --accent-soft: rgba(29, 85, 132, 0.16);
      --accent-soft-border: rgba(29, 85, 132, 0.38);
      --badge-bg: #C3D9EC;
      --badge-text: #133E62;
    }
    .dark[data-theme-profile="nordic"], [data-theme-profile="nordic"].dark {
      --app-bg: #0A1118;
      --app-text: #DBE5F0;
      --text-muted: #7D98B2;
      --card-bg: #111A24;
      --card-border: rgba(219, 229, 240, 0.09);
      --surface-subtle: #192533;
      --surface-subtle-hover: #213042;
      --border-subtle: rgba(219, 229, 240, 0.06);
      --input-bg: #192533;
      --input-border: rgba(219, 229, 240, 0.14);
      --accent-primary: #5594C9;
      --accent-text: #0A1118;
      --accent-soft: rgba(85, 148, 201, 0.2);
      --accent-soft-border: rgba(85, 148, 201, 0.38);
      --badge-bg: #1C2B3B;
      --badge-text: #82B5DE;
    }

    /* 5. Terracotta & Sand */
    [data-theme-profile="terracotta"] {
      --app-bg: #F3DFD2;
      --app-text: #2C180E;
      --text-muted: #7F5844;
      --card-bg: #FBEEE5;
      --card-border: rgba(130, 52, 22, 0.22);
      --surface-subtle: #E8CEBD;
      --surface-subtle-hover: #DDBFA9;
      --border-subtle: rgba(130, 52, 22, 0.15);
      --input-bg: #EFD5C5;
      --input-border: rgba(130, 52, 22, 0.26);
      --accent-primary: #A4421B;
      --accent-text: #FFFFFF;
      --accent-soft: rgba(164, 66, 27, 0.16);
      --accent-soft-border: rgba(164, 66, 27, 0.38);
      --badge-bg: #E2C3AF;
      --badge-text: #823110;
    }
    .dark[data-theme-profile="terracotta"], [data-theme-profile="terracotta"].dark {
      --app-bg: #170D07;
      --app-text: #EFE0D4;
      --text-muted: #A58574;
      --card-bg: #21130C;
      --card-border: rgba(239, 224, 212, 0.09);
      --surface-subtle: #2D1C12;
      --surface-subtle-hover: #3A2519;
      --border-subtle: rgba(239, 224, 212, 0.06);
      --input-bg: #2D1C12;
      --input-border: rgba(239, 224, 212, 0.14);
      --accent-primary: #DB6C3F;
      --accent-text: #170D07;
      --accent-soft: rgba(219, 108, 63, 0.2);
      --accent-soft-border: rgba(219, 108, 63, 0.38);
      --badge-bg: #311F15;
      --badge-text: #ECA17C;
    }

    /* 6. Lavender Dusk */
    [data-theme-profile="lavender"] {
      --app-bg: #E8DBF4;
      --app-text: #241334;
      --text-muted: #6C4C82;
      --card-bg: #F5ECFC;
      --card-border: rgba(88, 38, 122, 0.22);
      --surface-subtle: #DCC8F0;
      --surface-subtle-hover: #CEB5E6;
      --border-subtle: rgba(88, 38, 122, 0.15);
      --input-bg: #E4D3F4;
      --input-border: rgba(88, 38, 122, 0.26);
      --accent-primary: #692E96;
      --accent-text: #FFFFFF;
      --accent-soft: rgba(105, 46, 150, 0.16);
      --accent-soft-border: rgba(105, 46, 150, 0.38);
      --badge-bg: #D5BCEE;
      --badge-text: #4E1F72;
    }
    .dark[data-theme-profile="lavender"], [data-theme-profile="lavender"].dark {
      --app-bg: #110817;
      --app-text: #EADEF0;
      --text-muted: #9A7BAF;
      --card-bg: #1A1023;
      --card-border: rgba(234, 222, 240, 0.09);
      --surface-subtle: #241631;
      --surface-subtle-hover: #2F1E40;
      --border-subtle: rgba(234, 222, 240, 0.06);
      --input-bg: #241631;
      --input-border: rgba(234, 222, 240, 0.14);
      --accent-primary: #9D63CB;
      --accent-text: #110817;
      --accent-soft: rgba(157, 99, 203, 0.2);
      --accent-soft-border: rgba(157, 99, 203, 0.38);
      --badge-bg: #2B1A3A;
      --badge-text: #C496E6;
    }

    /* 7. Matcha & Cream */
    [data-theme-profile="matcha"] {
      --app-bg: #DFEBCE;
      --app-text: #1A2810;
      --text-muted: #556E42;
      --card-bg: #EEF6E3;
      --card-border: rgba(58, 92, 26, 0.22);
      --surface-subtle: #D2E4BD;
      --surface-subtle-hover: #C2DAA8;
      --border-subtle: rgba(58, 92, 26, 0.15);
      --input-bg: #DBE9C9;
      --input-border: rgba(58, 92, 26, 0.26);
      --accent-primary: #447120;
      --accent-text: #FFFFFF;
      --accent-soft: rgba(68, 113, 32, 0.16);
      --accent-soft-border: rgba(68, 113, 32, 0.38);
      --badge-bg: #C7DEAE;
      --badge-text: #2F5213;
    }
    .dark[data-theme-profile="matcha"], [data-theme-profile="matcha"].dark {
      --app-bg: #0D1407;
      --app-text: #E1EAD6;
      --text-muted: #869B72;
      --card-bg: #16200F;
      --card-border: rgba(225, 234, 214, 0.09);
      --surface-subtle: #1E2B15;
      --surface-subtle-hover: #28381D;
      --border-subtle: rgba(225, 234, 214, 0.06);
      --input-bg: #1E2B15;
      --input-border: rgba(225, 234, 214, 0.14);
      --accent-primary: #77A34A;
      --accent-text: #0D1407;
      --accent-soft: rgba(119, 163, 74, 0.2);
      --accent-soft-border: rgba(119, 163, 74, 0.38);
      --badge-bg: #23321A;
      --badge-text: #A5CC7C;
    }

    /* 8. Rose Quartz */
    [data-theme-profile="rose"] {
      --app-bg: #F5D6DE;
      --app-text: #2D141E;
      --text-muted: #7E4B5C;
      --card-bg: #FCE8ED;
      --card-border: rgba(135, 42, 68, 0.22);
      --surface-subtle: #EBC2CD;
      --surface-subtle-hover: #DEAFBC;
      --border-subtle: rgba(135, 42, 68, 0.15);
      --input-bg: #F2CDD6;
      --input-border: rgba(135, 42, 68, 0.26);
      --accent-primary: #9E2D4D;
      --accent-text: #FFFFFF;
      --accent-soft: rgba(158, 45, 77, 0.16);
      --accent-soft-border: rgba(158, 45, 77, 0.38);
      --badge-bg: #E3B6C2;
      --badge-text: #7D1E38;
    }
    .dark[data-theme-profile="rose"], [data-theme-profile="rose"].dark {
      --app-bg: #16080E;
      --app-text: #EEDFE3;
      --text-muted: #A47786;
      --card-bg: #211017;
      --card-border: rgba(238, 223, 227, 0.09);
      --surface-subtle: #2D1821;
      --surface-subtle-hover: #3B202C;
      --border-subtle: rgba(238, 223, 227, 0.06);
      --input-bg: #2D1821;
      --input-border: rgba(238, 223, 227, 0.14);
      --accent-primary: #C7597A;
      --accent-text: #16080E;
      --accent-soft: rgba(199, 89, 122, 0.2);
      --accent-soft-border: rgba(199, 89, 122, 0.38);
      --badge-bg: #331C26;
      --badge-text: #E595AE;
    }

    /* 9. OLED Obsidian (Pure Black) */
    [data-theme-profile="obsidian"] {
      --app-bg: #E2E6EE;
      --app-text: #09090B;
      --text-muted: #4B5262;
      --card-bg: #F1F4F9;
      --card-border: rgba(15, 23, 42, 0.25);
      --surface-subtle: #D4DCE8;
      --surface-subtle-hover: #C3CDDC;
      --border-subtle: rgba(15, 23, 42, 0.18);
      --input-bg: #DCE3EF;
      --input-border: rgba(15, 23, 42, 0.3);
      --accent-primary: #0F172A;
      --accent-text: #FFFFFF;
      --accent-soft: rgba(15, 23, 42, 0.16);
      --accent-soft-border: rgba(15, 23, 42, 0.38);
      --badge-bg: #CBD4E2;
      --badge-text: #0F172A;
    }
    .dark[data-theme-profile="obsidian"], [data-theme-profile="obsidian"].dark {
      --app-bg: #000000;
      --app-text: #FAFAFA;
      --text-muted: #A1A1AA;
      --card-bg: #0A0A0A;
      --card-border: rgba(255, 255, 255, 0.14);
      --surface-subtle: #141416;
      --surface-subtle-hover: #1F1F22;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --input-bg: #141414;
      --input-border: rgba(255, 255, 255, 0.18);
      --accent-primary: #FFFFFF;
      --accent-text: #000000;
      --accent-soft: rgba(255, 255, 255, 0.16);
      --accent-soft-border: rgba(255, 255, 255, 0.32);
      --badge-bg: #1A1A1D;
      --badge-text: #FAFAFA;
    }

    /* 10. E-Ink Pure Paper (Monochrome High Contrast) */
    [data-theme-profile="eink"] {
      --app-bg: #ECECEC;
      --app-text: #000000;
      --text-muted: #333333;
      --card-bg: #FFFFFF;
      --card-border: #000000;
      --surface-subtle: #E0E0E0;
      --surface-subtle-hover: #D0D0D0;
      --border-subtle: #888888;
      --input-bg: #FFFFFF;
      --input-border: #000000;
      --accent-primary: #000000;
      --accent-text: #FFFFFF;
      --accent-soft: #D4D4D4;
      --accent-soft-border: #555555;
      --badge-bg: #DDDDDD;
      --badge-text: #000000;
    }
    .dark[data-theme-profile="eink"], [data-theme-profile="eink"].dark {
      --app-bg: #080808;
      --app-text: #FFFFFF;
      --text-muted: #BBBBBB;
      --card-bg: #101010;
      --card-border: #888888;
      --surface-subtle: #181818;
      --surface-subtle-hover: #242424;
      --border-subtle: #444444;
      --input-bg: #181818;
      --input-border: #888888;
      --accent-primary: #FFFFFF;
      --accent-text: #000000;
      --accent-soft: #282828;
      --accent-soft-border: #AAAAAA;
      --badge-bg: #202020;
      --badge-text: #FFFFFF;
    }

    /* ==========================================================
       UNIVERSAL DYNAMIC THEMING OVERRIDES
       ========================================================== */
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

    /* Cards & Containers */
    .shadcn-card,
    .checkin-card,
    .diary-page-card,
    .notebook-container,
    .sheet-paper {
      background-color: var(--card-bg) !important;
      border: 1px solid var(--card-border) !important;
      color: var(--app-text) !important;
      border-radius: 1.25rem;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02), 0 8px 24px -4px rgba(0, 0, 0, 0.03);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .dark .shadcn-card,
    .dark .checkin-card,
    .dark .diary-page-card,
    .dark .notebook-container,
    .dark .sheet-paper {
      box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.4);
    }

    /* Subtle Inner Surfaces & Panels */
    .theme-subtle,
    .inner-panel,
    #diary-customization-hint,
    #settings-tab-modules > .p-3,
    #settings-tab-general > .p-3,
    #settings-tab-appearance > .p-3,
    .settings-panel-row,
    #settings-card-order-container > div,
    #custom-option-modal .shadcn-card {
      background-color: var(--surface-subtle) !important;
      border-color: var(--border-subtle) !important;
      color: var(--app-text) !important;
    }

    #settings-modal .shadcn-card {
      background-color: var(--card-bg) !important;
      border-color: var(--card-border) !important;
      color: var(--app-text) !important;
    }

    /* ==========================================================
       DRAG AND DROP REORDERING STYLES
       ========================================================== */
    .diary-card-drag-handle,
    .settings-drag-handle {
      touch-action: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: grab;
    }
    .diary-card-drag-handle:active,
    .settings-drag-handle:active {
      cursor: grabbing;
    }
    .is-dragging {
      opacity: 0.55 !important;
      transform: scale(0.99) !important;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.25) !important;
      border: 2px dashed var(--accent-primary) !important;
      transition: none !important;
    }
    .drop-target-above {
      border-top: 3px solid var(--accent-primary) !important;
    }
    .drop-target-below {
      border-bottom: 3px solid var(--accent-primary) !important;
    }

    /* Form Controls: Inputs, Textareas, Selects */
    input:not([type="checkbox"]):not([type="radio"]):not([type="range"]),
    select,
    textarea,
    .shadcn-input,
    .notebook-input-area {
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

    input:not([type="checkbox"]):not([type="radio"]):not([type="range"]):focus,
    select:focus,
    textarea:focus,
    .shadcn-input:focus,
    .notebook-input-area:focus {
      border-color: var(--accent-primary) !important;
      box-shadow: 0 0 0 3px var(--accent-soft) !important;
      outline: none;
    }

    textarea.shadcn-input {
      min-height: 4.5rem;
      resize: vertical;
      line-height: 1.6;
    }

    /* Primary Buttons */
    .btn-primary-theme,
    button[onclick*="saveCurrentDiaryEntry"],
    button[onclick*="saveCurrentMemo"],
    button[onclick*="saveCustomOptionFromModal"] {
      background-color: var(--accent-primary) !important;
      color: var(--accent-text) !important;
      border-color: transparent !important;
    }

    /* Brand Logo Icon */
    #brand-logo-icon {
      background-color: var(--accent-primary) !important;
      color: var(--accent-text) !important;
    }

    /* Mode Switcher at Top Header */
    header .inline-flex.rounded-full {
      background-color: var(--surface-subtle) !important;
      border-color: var(--border-subtle) !important;
    }
    #mode-btn-schema.active,
    #mode-btn-diary.active {
      background-color: var(--card-bg) !important;
      color: var(--accent-primary) !important;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08) !important;
    }

    /* Section Navigation Buttons */
    .sec-nav-btn {
      background-color: var(--surface-subtle) !important;
      border: 1px solid var(--border-subtle) !important;
      color: var(--text-muted) !important;
    }
    .sec-nav-btn.active {
      background-color: var(--accent-primary) !important;
      border-color: var(--accent-primary) !important;
      color: var(--accent-text) !important;
    }

    /* Badges & Summary Counts */
    [id^="badge-summary-"],
    #nap-badge,
    #meds-count-badge,
    #positive-things-counter,
    #caffeine-total-badge,
    #steps-display-badge,
    #current-profile-badge,
    #current-lang-badge,
    #diary-count-badge,
    #settings-active-count-badge {
      background-color: var(--surface-subtle) !important;
      border: 1px solid var(--border-subtle) !important;
      color: var(--accent-primary) !important;
    }

    /* Universal Tag Chips & Pill Buttons */
    .tag-chip,
    .emotion-chip,
    .emotion-chip-custom,
    .custom-schema-chip,
    .qf-btn,
    .nap-quick-btn,
    #quick-meds-chips-container button,
    #quick-meds-chips-container span,
    #pleasant-emotions-chips button,
    #challenging-emotions-chips button,
    #meal-tags-container button,
    #sleep-factors-chips-container button,
    #memory-tags-container button,
    #activities-chips-container button,
    #schema-step1-chips button,
    #schema-step2-chips button,
    #schema-step3-chips button {
      background-color: var(--surface-subtle) !important;
      border: 1px solid var(--border-subtle) !important;
      color: var(--app-text) !important;
      transition: all 0.15s ease;
    }
    .tag-chip:hover,
    .emotion-chip:hover,
    .qf-btn:hover,
    .nap-quick-btn:hover,
    #quick-meds-chips-container button:hover,
    #pleasant-emotions-chips button:hover,
    #challenging-emotions-chips button:hover,
    #meal-tags-container button:hover,
    #sleep-factors-chips-container button:hover,
    #memory-tags-container button:hover,
    #activities-chips-container button:hover,
    #schema-step1-chips button:hover,
    #schema-step2-chips button:hover,
    #schema-step3-chips button:hover {
      background-color: var(--surface-subtle-hover) !important;
      border-color: var(--card-border) !important;
    }

    /* Active Tag Chips */
    .tag-chip.active,
    .emotion-chip.active,
    .qf-btn.active,
    .nap-quick-btn.active,
    button[data-tag].active {
      background-color: var(--accent-soft) !important;
      border-color: var(--accent-soft-border) !important;
      color: var(--accent-primary) !important;
      font-weight: 600 !important;
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

    /* Bottom Navigation Active State */
    .bottom-nav-btn {
      color: var(--text-muted) !important;
    }
    .bottom-nav-btn.active {
      color: var(--app-text) !important;
    }
    .bottom-nav-btn.active .nav-icon-wrapper {
      background-color: var(--accent-soft) !important;
      color: var(--accent-primary) !important;
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
