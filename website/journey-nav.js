document.querySelectorAll("[data-journey-nav-toggle]").forEach((toggle) => {
  const navigation = document.getElementById(toggle.getAttribute("aria-controls"));
  const header = toggle.closest(".portal-topbar");

  if (!navigation || !header) return;

  header.classList.add("journey-nav-ready");

  const closeNavigation = () => {
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-label", "Open navigation");
    toggle.setAttribute("title", "Open navigation");
    navigation.classList.remove("is-open");
  };

  toggle.addEventListener("click", () => {
    const isOpen = toggle.getAttribute("aria-expanded") === "true";
    if (isOpen) {
      closeNavigation();
      return;
    }

    toggle.setAttribute("aria-expanded", "true");
    toggle.setAttribute("aria-label", "Close navigation");
    toggle.setAttribute("title", "Close navigation");
    navigation.classList.add("is-open");
  });

  navigation.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeNavigation();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeNavigation();
  });
});
