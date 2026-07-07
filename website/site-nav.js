(() => {
  "use strict";

  const navigationToggle = document.querySelector(".nav-toggle");
  const primaryNavigation = document.querySelector("#primary-navigation");
  const header = document.querySelector(".site-header");

  if (!navigationToggle || !primaryNavigation || !header) return;

  header.classList.add("nav-ready");

  const closeNavigation = () => {
    navigationToggle.setAttribute("aria-expanded", "false");
    navigationToggle.setAttribute("aria-label", "Open navigation");
    navigationToggle.setAttribute("title", "Open navigation");
    primaryNavigation.classList.remove("is-open");
  };

  navigationToggle.addEventListener("click", () => {
    const isOpen = navigationToggle.getAttribute("aria-expanded") === "true";
    navigationToggle.setAttribute("aria-expanded", String(!isOpen));
    navigationToggle.setAttribute("aria-label", isOpen ? "Open navigation" : "Close navigation");
    navigationToggle.setAttribute("title", isOpen ? "Open navigation" : "Close navigation");
    primaryNavigation.classList.toggle("is-open", !isOpen);
  });

  primaryNavigation.addEventListener("click", (event) => {
    if (!event.target.closest("a")) return;
    closeNavigation();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;
    closeNavigation();
  });
})();
