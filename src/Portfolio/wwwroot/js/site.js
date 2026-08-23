const projectGrid = document.querySelector('[data-project-grid]');
const projectTemplate = document.querySelector('#project-card-template');
const loadStatus = document.querySelector('[data-load-status]');
const header = document.querySelector('[data-header]');
const menuButton = document.querySelector('[data-menu-button]');
const navLinks = document.querySelector('[data-nav-links]');

document.querySelector('[data-year]').textContent = new Date().getFullYear();

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add('visible');
    revealObserver.unobserve(entry.target);
  });
}, { threshold: 0.12 });

function observeReveals(scope = document) {
  scope.querySelectorAll('.reveal:not(.visible)').forEach((item) => revealObserver.observe(item));
}

function buildList(items, parent) {
  const fragment = document.createDocumentFragment();
  items.forEach((item) => {
    const li = document.createElement('li');
    li.textContent = item;
    fragment.append(li);
  });
  parent.append(fragment);
}

function createProjectCard(project) {
  const card = projectTemplate.content.firstElementChild.cloneNode(true);
  card.dataset.accent = project.accent;
  card.querySelector('[data-project-eyebrow]').textContent = `${project.eyebrow} · ${project.year}`;
  card.querySelector('[data-project-score]').textContent = `${project.score.toFixed(1)} / 10`;
  card.querySelector('[data-project-name]').textContent = project.name;
  card.querySelector('[data-project-tagline]').textContent = project.tagline;
  card.querySelector('[data-project-description]').textContent = project.description;
  buildList(project.highlights, card.querySelector('[data-project-highlights]'));
  buildList(project.technologies, card.querySelector('[data-project-tech]'));
  const link = card.querySelector('[data-project-link]');
  link.href = project.repositoryUrl;
  link.setAttribute('aria-label', `Open ${project.name} on GitHub`);
  return card;
}

async function loadProjects() {
  try {
    const response = await fetch('./projects.json');
    if (!response.ok) throw new Error(`Request failed with status ${response.status}`);
    const projects = await response.json();
    const fragment = document.createDocumentFragment();
    projects.filter((project) => project.featured && project.score >= 8).forEach((project) => fragment.append(createProjectCard(project)));
    projectGrid.replaceChildren(fragment);
    loadStatus.textContent = '';
    observeReveals(projectGrid);
  } catch (error) {
    projectGrid.replaceChildren();
    loadStatus.textContent = 'The project catalog is temporarily unavailable. Please refresh the page.';
    console.error('Could not load portfolio projects.', error);
  }
}

window.addEventListener('scroll', () => header.classList.toggle('scrolled', window.scrollY > 10), { passive: true });

menuButton.addEventListener('click', () => {
  const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!isOpen));
  navLinks.classList.toggle('open', !isOpen);
  header.classList.toggle('menu-open', !isOpen);
});

navLinks.addEventListener('click', (event) => {
  if (!(event.target instanceof HTMLAnchorElement)) return;
  menuButton.setAttribute('aria-expanded', 'false');
  navLinks.classList.remove('open');
  header.classList.remove('menu-open');
});

observeReveals();
loadProjects();
