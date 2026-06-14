# Frontend Rules -- RD2100 Agent Runtime v2

> Domain: frontend code (HTML, CSS, JS, React, Vue, mini-apps)
> Phase 0-5: reference only (agent-acceptance has no frontend code)
> These rules activate when working on projects with frontend surfaces.

---

## RULE fe-001: No XSS Vectors

- **Priority**: P0 (Hard Stop)
- **Trigger**: Writing HTML rendering, innerHTML, dangerouslySetInnerHTML, v-html
- **Scope**: All frontend code
- **Rule**: Never use `innerHTML`, `dangerouslySetInnerHTML`, `v-html`, or `document.write` with unsanitized user input. Use text content APIs (`textContent`, `innerText`, template bindings) instead.
- **Verification**: Grep for `innerHTML`, `dangerouslySetInnerHTML`, `v-html`, `document.write`.
- **Conflict Handling**: If a library requires raw HTML insertion, the input must be sanitized with a proven library (DOMPurify).

---

## RULE fe-002: No Unsanitized User Input in URLs

- **Priority**: P0 (Hard Stop)
- **Trigger**: Constructing URLs that include user input
- **Scope**: All frontend code
- **Rule**: User input must not be directly interpolated into `href`, `src`, `action`, or `fetch()` URLs. Validate and encode. Use `URL` constructor or URL-safe templating.
- **Verification**: Grep for URL construction patterns with variable interpolation.
- **Conflict Handling**: If dynamic URLs are required, use `encodeURIComponent` on each user-supplied segment.

---

## RULE fe-003: Component Isolation

- **Priority**: P1 (Scope Control)
- **Trigger**: Creating or modifying a UI component
- **Scope**: All frontend code
- **Rule**: Components must not rely on global state, global selectors, or DOM structure outside their subtree. Use props/events for parent-child communication. Use provided state management for cross-tree state.
- **Verification**: Component review: no `document.querySelector` outside component root; no `window.*` mutation.
- **Conflict Handling**: Third-party component exceptions must be documented.

---

## RULE fe-004: Responsive Baseline

- **Priority**: P3 (Domain)
- **Trigger**: Creating new UI layout
- **Scope**: All frontend code
- **Rule**: New layouts must function at 320px minimum width without horizontal scroll. Use relative units (rem, %, vw) over fixed px where reasonable.
- **Verification**: Visual check or automated screenshot at 320px, 768px, 1024px.
- **Conflict Handling**: Data-dense interfaces (tables, dashboards) may require higher minimum width with documented reason.

---

## RULE fe-005: Accessible Markup

- **Priority**: P3 (Domain)
- **Trigger**: Writing interactive elements
- **Scope**: All frontend code
- **Rule**: Interactive elements must be keyboard accessible. Buttons use `<button>`, not `<div onclick>`. Form inputs have associated `<label>`. Images have `alt` attributes (empty for decorative).
- **Verification**: Axe or Lighthouse accessibility audit.
- **Conflict Handling**: Custom interactive widgets must implement ARIA roles and keyboard handlers.

---

## RULE fe-006: No Inline Styles

- **Priority**: P4 (Style)
- **Trigger**: Writing visual styling
- **Scope**: All frontend code
- **Rule**: Prefer CSS classes or CSS-in-JS over inline `style` attributes. Inline styles are acceptable only for dynamically computed values (e.g., progress bar width).
- **Verification**: Grep for `style=` in HTML/JSX.
- **Conflict Handling**: Animation and dynamic positioning may require inline styles.
