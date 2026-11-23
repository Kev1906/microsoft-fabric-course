/* RetailOps 360 · Microsoft Fabric Master Course interactions
   Sin dependencias. Todo degrada correctamente si algo no está disponible. */
(function () {
  "use strict";

  var root = document.documentElement;

  function read(key) {
    try {
      return window.localStorage.getItem(key);
    } catch (error) {
      return null;
    }
  }

  function write(key, value) {
    try {
      window.localStorage.setItem(key, value);
    } catch (error) {
      /* file:// o modo privado: seguimos sin persistencia */
    }
  }

  /* ---------- Tema ---------- */
  function applyTheme(theme) {
    if (theme === "dark") {
      root.setAttribute("data-theme", "dark");
    } else {
      root.removeAttribute("data-theme");
    }
    document.querySelectorAll(".theme-toggle").forEach(function (button) {
      var dark = theme === "dark";
      button.setAttribute("aria-pressed", String(dark));
      button.setAttribute(
        "aria-label",
        dark ? "Cambiar a tema claro" : "Cambiar a tema oscuro"
      );
      var label = button.querySelector(".theme-toggle__label");
      if (label) {
        label.textContent = dark ? "Claro" : "Oscuro";
      }
    });
  }

  var savedTheme = read("fabric-theme");
  var prefersDark =
    window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches;
  applyTheme(savedTheme === "dark" || (!savedTheme && prefersDark) ? "dark" : "light");

  document.querySelectorAll(".theme-toggle").forEach(function (button) {
    button.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      applyTheme(next);
      write("fabric-theme", next);
    });
  });

  /* ---------- Progreso de lectura ---------- */
  var progress = document.getElementById("readingProgress");
  if (progress) {
    var ticking = false;

    function updateProgress() {
      var height =
        document.documentElement.scrollHeight - window.innerHeight;
      var ratio = height > 0 ? window.scrollY / height : 0;
      progress.style.width = Math.min(100, Math.max(0, ratio * 100)) + "%";
      ticking = false;
    }

    window.addEventListener(
      "scroll",
      function () {
        if (!ticking) {
          ticking = true;
          window.requestAnimationFrame(updateProgress);
        }
      },
      { passive: true }
    );
    window.addEventListener("resize", updateProgress);
    updateProgress();
  }

  /* ---------- Botones de copiar ---------- */
  document.querySelectorAll(".code-block").forEach(function (block) {
    var head = block.querySelector(".code-head");
    var code = block.querySelector("pre code") || block.querySelector("pre");
    if (!head || !code) return;

    var button = document.createElement("button");
    button.type = "button";
    button.className = "copy-btn";
    button.textContent = "Copiar";
    button.setAttribute("aria-label", "Copiar bloque de código");
    head.appendChild(button);

    button.addEventListener("click", function () {
      var text = code.innerText.replace(/\n$/, "");

      function done() {
        button.textContent = "Copiado";
        button.classList.add("is-copied");
        window.setTimeout(function () {
          button.textContent = "Copiar";
          button.classList.remove("is-copied");
        }, 1600);
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, fallback);
      } else {
        fallback();
      }

      function fallback() {
        var area = document.createElement("textarea");
        area.value = text;
        area.setAttribute("readonly", "");
        area.style.position = "fixed";
        area.style.opacity = "0";
        document.body.appendChild(area);
        area.select();
        try {
          document.execCommand("copy");
          done();
        } catch (error) {
          button.textContent = "No disponible";
        }
        document.body.removeChild(area);
      }
    });
  });

  /* ---------- Checklists persistentes ---------- */
  var pageKey = (window.location.pathname.split("/").pop() || "index").replace(
    /\.html$/,
    ""
  );

  document
    .querySelectorAll('input[type="checkbox"][data-persist]')
    .forEach(function (checkbox) {
      if (!checkbox.id) return;
      var key = "fabric-check:" + pageKey + ":" + checkbox.id;
      if (read(key) === "1") {
        checkbox.checked = true;
      }
      checkbox.addEventListener("change", function () {
        write(key, checkbox.checked ? "1" : "0");
      });
    });

  /* ---------- TOC activo ---------- */
  var tocLinks = Array.prototype.slice.call(
    document.querySelectorAll('.toc ul a[href^="#"]')
  );

  if (tocLinks.length) {
    var sections = tocLinks
      .map(function (link) {
        return document.querySelector(link.getAttribute("href"));
      })
      .filter(Boolean);

    var tocTicking = false;

    function updateToc() {
      var current = sections[0];
      sections.forEach(function (section) {
        if (section.getBoundingClientRect().top <= 148) {
          current = section;
        }
      });

      if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 4) {
        current = sections[sections.length - 1];
      }

      tocLinks.forEach(function (link) {
        var active =
          current && link.getAttribute("href") === "#" + current.id;
        link.classList.toggle("is-active", active);
        if (active) {
          link.setAttribute("aria-current", "location");
        } else {
          link.removeAttribute("aria-current");
        }
      });

      tocTicking = false;
    }

    window.addEventListener(
      "scroll",
      function () {
        if (!tocTicking) {
          tocTicking = true;
          window.requestAnimationFrame(updateToc);
        }
      },
      { passive: true }
    );
    updateToc();
  }

  /* ---------- Año del footer ---------- */
  document.querySelectorAll("[data-year]").forEach(function (element) {
    element.textContent = String(new Date().getFullYear());
  });
})();
