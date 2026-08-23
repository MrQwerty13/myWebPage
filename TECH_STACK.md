# Technology stack

This document records the technologies used by the portfolio, why they were
selected, and how the pieces fit together.

## Runtime and backend

| Technology | Version | Responsibility |
| --- | --- | --- |
| .NET | 10 | Runtime, build system, dependency management, and publishing |
| ASP.NET Core | 10 | HTTP server, static-file hosting, routing, and JSON serialization |
| C# | 14 / SDK default | Typed project model, catalog service, and API definitions |
| Kestrel | Bundled with ASP.NET Core | Local and LAN HTTP server on port `8080` |

ASP.NET Core Minimal APIs keep the server deliberately small. The portfolio does
not currently need MVC controllers, Razor rendering, a database, authentication,
or a separate Node.js frontend build.

## Frontend

| Technology | Responsibility |
| --- | --- |
| Semantic HTML5 | Page structure, accessibility landmarks, and project-card template |
| Modern CSS | Layout, responsive breakpoints, visual system, animations, and reduced motion |
| Vanilla JavaScript | Fetching project data, rendering cards, navigation, and reveal behavior |
| Fetch API | Communication with the ASP.NET Core project endpoint |
| Intersection Observer | Lightweight viewport-based reveal animation |

The frontend intentionally has no package manager or framework. This reduces
startup time, avoids a second build pipeline, and keeps the site deployable as
ordinary static assets served by ASP.NET Core.

## Testing

| Technology | Version | Responsibility |
| --- | --- | --- |
| xUnit | 2.9.3 | Unit tests for the project catalog and selection policy |
| Microsoft.NET.Test.Sdk | 17.14.1 | .NET test discovery and execution |
| xunit.runner.visualstudio | 3.1.4 | IDE and `dotnet test` integration |
| coverlet.collector | 6.0.4 | Optional code-coverage collection |

The first test layer protects the content rules that determine which repositories
appear in the portfolio. Endpoint integration tests and automated browser tests
are planned for the next quality milestone.

## Architecture

```text
Browser
  ├── GET /                 ──> wwwroot/index.html
  ├── GET /css, /js         ──> ASP.NET Core static files
  ├── GET /api/projects     ──> ProjectCatalog ──> PortfolioProject[]
  ├── GET /api/projects/:id ──> ProjectCatalog ──> PortfolioProject | 404
  └── GET /health           ──> Health response
```

### Application layers

1. **Presentation** — `wwwroot` contains the static page, shared CSS, and browser
   behavior.
2. **HTTP boundary** — `Program.cs` configures middleware and exposes the API.
3. **Application data** — `ProjectCatalog` owns the curated portfolio selection.
4. **Domain shape** — `PortfolioProject` defines the serialized project contract.

The browser does not duplicate project content. It receives a typed JSON payload
from the backend and creates the project cards from a reusable HTML template.

## Design system

The visual direction is inspired by the clarity of Apple's product pages without
copying a specific page or proprietary asset. Its main characteristics are:

- system typefaces for native rendering and fast loading;
- large editorial typography and generous spacing;
- neutral surfaces with one accent color per project;
- rounded product cards and restrained depth;
- progressive enhancement for animations;
- desktop, tablet, and mobile breakpoints at `980px` and `640px`;
- `prefers-reduced-motion` support.

## Configuration

`src/Portfolio/appsettings.json` contains the shared settings:

```json
{
  "Urls": "http://0.0.0.0:8080",
  "AllowedHosts": "*"
}
```

The URL can be overridden without editing the repository:

```bash
dotnet run --project src/Portfolio/Portfolio.csproj --urls http://127.0.0.1:5000
```

Production deployments should provide environment-specific logging and host
configuration outside source control.

## Deliberately excluded for now

- Database: project content is small, curated, and version-controlled.
- Frontend framework: the current interactions do not justify its runtime and
  build complexity.
- Authentication: the site exposes public portfolio content only.
- External analytics: privacy and measurement requirements are not defined yet.
- CDN and object storage: there are no large media assets in the first release.

These choices should be reconsidered only when a concrete roadmap item requires
them.
