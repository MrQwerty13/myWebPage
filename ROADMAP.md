# Roadmap

The roadmap turns the original project to-do into small, verifiable releases.
Items are ordered by product value and dependency rather than by idea size.

## Release status

| Release | Status | Outcome |
| --- | --- | --- |
| 0.1 — Foundation | Complete | ASP.NET Core solution, static hosting, project API, and test project |
| 0.2 — Portfolio experience | Complete | Responsive visual design, dynamic cards, mobile navigation, and accessibility |
| 0.3 — Documentation | Complete | README, stack decisions, roadmap, development, and deployment instructions |
| 0.4 — Case studies | Next | Detailed pages and real visual material for every featured project |
| 0.5 — Production readiness | Planned | Integration tests, automation, observability, and repeatable packaging |
| 1.0 — Public release | Planned | Stable deployment, final content review, and launch checklist |

## Completed

### Repository assessment

- Reviewed all 12 public repositories.
- Wrote a description and conclusion for every project.
- Applied a consistent 0–10 scoring method.
- Selected five projects at or above the 8.0 threshold.

### Application foundation

- Created a .NET 10 ASP.NET Core project and solution.
- Added a typed `PortfolioProject` model and `ProjectCatalog` service.
- Added catalog, project-detail, and health endpoints.
- Configured static files and single-page fallback routing.
- Configured Kestrel to listen on port `8080` for LAN access.

### Portfolio interface

- Built one responsive HTML page with shared CSS and JavaScript.
- Added project cards populated from the backend API.
- Added desktop, tablet, and mobile layouts.
- Added responsive mobile navigation.
- Added semantic page landmarks, accessible labels, and a skip link.
- Added reduced-motion behavior and API failure messaging.
- Completed desktop and mobile visual verification.

### Quality baseline

- Added xUnit coverage for catalog rules and lookups.
- Verified the solution builds without warnings or errors.
- Verified all six automated tests pass.
- Verified API responses, JavaScript syntax, browser console, and horizontal
  overflow behavior.

### Static public hosting

- Added a single JSON catalog consumed by both the browser and ASP.NET API.
- Added repository-relative asset paths for project-site hosting.
- Added an automatic GitHub Pages deployment workflow.

## Next: release 0.4 — case studies

- [ ] Add a dedicated route and detail view for each featured project.
- [ ] Capture or create consistent hero imagery for all five projects.
- [ ] Document the problem, constraints, decisions, architecture, and result for
      each case study.
- [ ] Add links to live applications where stable public deployments exist.
- [ ] Add repository metadata such as current status and last meaningful update.
- [ ] Review all public-facing English copy with the project owner.
- [ ] Add a custom social-sharing image and favicon set.

### Definition of done

Every featured project has a visually consistent case-study page, accurate
content, working links, optimized imagery, and a useful mobile experience.

## Release 0.5 — production readiness

- [ ] Add HTTP integration tests for `/`, `/health`, and all project endpoints.
- [ ] Add automated browser checks for desktop and mobile navigation.
- [ ] Collect and enforce meaningful code coverage.
- [ ] Add a continuous-integration workflow for restore, build, test, and publish.
- [ ] Add cache headers and compression for production static assets.
- [ ] Add security headers, including a Content Security Policy.
- [ ] Add structured request logging and a deployment health check.
- [ ] Produce a versioned Release build artifact.
- [ ] Add a container image only if the final hosting target benefits from it.

## Release 1.0 — public launch

- [ ] Select the permanent domain and hosting environment.
- [ ] Configure HTTPS through a trusted reverse proxy or managed host.
- [ ] Validate metadata, sitemap, robots policy, and canonical URLs.
- [ ] Run accessibility checks against WCAG 2.2 AA expectations.
- [ ] Test current Safari, Chrome, Firefox, and Edge versions.
- [ ] Test representative phone and tablet sizes on real devices.
- [ ] Complete a final content and privacy review.
- [ ] Tag version `1.0.0` and publish release notes.

## Later opportunities

- Optional English/Russian language switcher
- Automated GitHub metadata refresh with a documented cache policy
- Writing or notes section
- Contact form with spam protection and explicit privacy behavior
- Privacy-respecting, opt-in traffic measurement
- Tart-based isolated build verification on Apple Silicon

Later opportunities are not commitments. They should enter a scheduled release
only when they support a clear visitor or maintenance need.
