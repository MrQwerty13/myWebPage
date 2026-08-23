# Mikhail's Portfolio

A responsive developer portfolio that presents the strongest projects from
[MrQwerty13's GitHub profile](https://github.com/MrQwerty13). The site combines
an Apple-inspired visual language with a small ASP.NET Core backend that serves
the frontend and exposes the project catalog as JSON.

## Current release

The first release reviews 12 public repositories and features the five projects
that scored 8.0 or higher for implementation depth, architecture, engineering
quality, documentation, and product polish:

| Project | Score | Focus |
| --- | ---: | --- |
| [CupIT](https://github.com/MrQwerty13/CupIT) | 9.5 | Local-first cafe analytics |
| [FriedSausages](https://github.com/MrQwerty13/FriedSausages) | 8.7 | Security operations |
| [Chatic](https://github.com/MrQwerty13/chatic) | 8.5 | Realtime private messaging |
| [Aftertaste](https://github.com/MrQwerty13/Aftertaste) | 8.2 | Social tasting journal |
| [TaskTracker](https://github.com/MrQwerty13/TaskTrackerPyVersion) | 8.0 | Focused task management |

The complete review and scoring rationale are available in
[PROJECT_ASSESSMENT.md](PROJECT_ASSESSMENT.md).

## Features

- Responsive single-page portfolio for desktop, tablet, and mobile
- Project content supplied by a typed C# catalog
- JSON endpoints for the complete catalog and individual projects
- Health endpoint for local and hosted monitoring
- Accessible navigation, semantic content, and keyboard skip link
- Reduced-motion support for visitors who request it
- Mobile navigation and touch-friendly controls
- Local network hosting through Kestrel on port `8080`
- Automated tests for selection rules and catalog integrity

## Quick start

### Requirements

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
- A modern browser

### Run the portfolio

```bash
git clone https://github.com/MrQwerty13/myWebPage.git
cd myWebPage
dotnet restore MyWebPage.slnx
dotnet run --project src/Portfolio/Portfolio.csproj
```

Open [http://localhost:8080](http://localhost:8080).

The application listens on `0.0.0.0:8080`, so it can also be opened from a
device on the same trusted network at `http://<computer-ip>:8080`.

## Test and build

```bash
dotnet build MyWebPage.slnx --no-restore
dotnet test MyWebPage.slnx --no-build
```

The current test suite contains six checks covering the featured-project
threshold, score range, slug uniqueness, expected selection, and project lookup.

## API

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/health` | Return service health and the current UTC timestamp |
| `GET` | `/api/projects` | Return the complete portfolio catalog |
| `GET` | `/api/projects/{slug}` | Return one project or a `404` response |

Example:

```bash
curl http://localhost:8080/api/projects/cupit
```

## Project structure

```text
myWebPage/
├── src/Portfolio/
│   ├── Models/                 Project response model
│   ├── Services/               Curated project catalog
│   ├── wwwroot/
│   │   ├── css/site.css        Shared responsive design system
│   │   ├── js/site.js          Catalog rendering and interactions
│   │   └── index.html          Portfolio page
│   ├── Program.cs              ASP.NET Core application and endpoints
│   └── Portfolio.csproj
├── tests/Portfolio.Tests/      xUnit test project
├── MyWebPage.slnx              .NET solution
├── PROJECT_ASSESSMENT.md       Review of all public projects
├── TECH_STACK.md               Technology and architecture decisions
├── ROADMAP.md                  Delivery status and planned work
├── DEVELOPMENT.md              Local development and testing instructions
└── DEPLOYMENT.md               LAN and release hosting instructions
```

## Documentation

- [Technology stack and architecture](TECH_STACK.md)
- [Development roadmap](ROADMAP.md)
- [Local development instructions](DEVELOPMENT.md)
- [Deployment instructions](DEPLOYMENT.md)
- [Public project assessment](PROJECT_ASSESSMENT.md)

## Status

The portfolio foundation is working and tested. The next release will add real
project imagery, richer case-study pages, integration tests, SEO metadata, and a
repeatable deployment package. See [ROADMAP.md](ROADMAP.md) for the full plan.

## License

Licensed under the [Apache License 2.0](LICENSE).
