const header = require('./components/header');
const footer = require('./components/footer');

document.addEventListener('DOMContentLoaded', () => {
    // Initialize header and footer
    const headerElement = header();
    const footerElement = footer();

    document.body.insertAdjacentHTML('afterbegin', headerElement);
    document.body.insertAdjacentHTML('beforeend', footerElement);

    // Add event listeners for navigation links
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            const targetPage = link.getAttribute('href');
            loadPage(targetPage);
        });
    });
});

// Simple UI: mobile menu toggle and footer year
document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.getElementById('menu-toggle');
  const nav = document.getElementById('main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
});

function loadPage(page) {
    fetch(page)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(html => {
            document.body.innerHTML = html;
            // Re-initialize header and footer after loading new page
            const headerElement = header();
            const footerElement = footer();
            document.body.insertAdjacentHTML('afterbegin', headerElement);
            document.body.insertAdjacentHTML('beforeend', footerElement);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}