// =========================================================
// AJJAH Designs – Polished JS (accessible nav; minimal)
// =========================================================

(() => {
  const toggle = document.getElementById('menu-toggle');
  const menu = document.getElementById('primary-menu');
  if (!toggle || !menu) return;

  const mqDesktop = matchMedia('(min-width: 1000px)');
  const isOpen   = () => toggle.getAttribute('aria-expanded') === 'true';
  const open     = () => toggle.setAttribute('aria-expanded', 'true');
  const close    = () => toggle.setAttribute('aria-expanded', 'false');

  // Toggle click
  toggle.addEventListener('click', () => (isOpen() ? close() : open()));

  // Close when link chosen on mobile
  menu.addEventListener('click', (e) => {
    const t = e.target;
    if (!mqDesktop.matches && t && t.tagName === 'A') close();
  });

  // Click outside to close (mobile)
  document.addEventListener('click', (e) => {
    if (mqDesktop.matches) return;
    const within = e.target.closest('nav[aria-label="Primary"]');
    if (!within && isOpen()) close();
  });

  // Escape to close
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && isOpen()) { close(); toggle.focus(); }
  });

  // Keep attribute sane when resizing
  mqDesktop.addEventListener('change', close);
})();

/* ===== Theme toggle ===== */
(() => {
  const btn = document.getElementById('theme-toggle');
  if (!btn) return;

  const root = document.documentElement;
  const STORAGE_KEY = 'ajjah-theme'; // 'light' | 'dark'

  // Decide initial theme: stored value -> system pref -> default 'dark'
  const stored = localStorage.getItem(STORAGE_KEY);
  const systemPrefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
  const initial = stored || (systemPrefersLight ? 'light' : 'dark');
  applyTheme(initial);

  btn.addEventListener('click', () => {
    const next = (root.getAttribute('data-theme') === 'light') ? 'dark' : 'light';
    applyTheme(next);
    localStorage.setItem(STORAGE_KEY, next);
  });

  // If there's NO explicit override and system preference changes, follow it
  const mq = window.matchMedia('(prefers-color-scheme: light)');
  mq.addEventListener('change', e => {
    if (!localStorage.getItem(STORAGE_KEY)) {
      applyTheme(e.matches ? 'light' : 'dark');
    }
  });

  function applyTheme(theme){
    root.setAttribute('data-theme', theme);
    const isLight = theme === 'light';
    btn.setAttribute('aria-pressed', String(isLight)); // pressed = light mode
    btn.querySelector('.theme-toggle__icon').textContent = isLight ? '🌞' : '🌙';
    btn.querySelector('.theme-toggle__text').textContent  = isLight ? 'Light' : 'Dark';
    btn.setAttribute('aria-label', `Switch to ${isLight ? 'dark' : 'light'} theme`);
  }
})();
