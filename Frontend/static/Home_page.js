document.addEventListener("DOMContentLoaded", function () {
  const sections = document.querySelectorAll(".features");

  const observer = new IntersectionObserver(
      (entries, observer) => {
          entries.forEach(entry => {
              if (entry.isIntersecting) {
                  entry.target.classList.add("show");
                  observer.unobserve(entry.target);
              }
          });
      },
      { threshold: 0.9 } // Adjust the threshold as needed
  );

  sections.forEach(section => {
      section.classList.add("hidden");
      observer.observe(section);
  });
});
