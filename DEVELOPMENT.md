# Development instructions

This guide covers initial setup, the normal local workflow, content changes,
testing, and common problems.

## 1. Prerequisites

Install the following:

- Git
- .NET 10 SDK
- A modern browser
- Node.js only if you want to run the optional JavaScript syntax check

Confirm the required tools:

```bash
git --version
dotnet --version
```

The .NET version should start with `10.`. No database, frontend package manager,
API key, or external service is needed.

## 2. Clone and restore

```bash
git clone https://github.com/MrQwerty13/myWebPage.git
cd myWebPage
dotnet restore MyWebPage.slnx
```

Restore downloads the packages used by the xUnit test project. The application
itself depends only on the shared ASP.NET Core runtime.

## 3. Run locally

```bash
dotnet run --project src/Portfolio/Portfolio.csproj
```

Open [http://localhost:8080](http://localhost:8080).

Stop the server with `Control+C` in the terminal where it is running.

### Use another address or port

Command-line configuration overrides the repository default:

```bash
dotnet run --project src/Portfolio/Portfolio.csproj \
  --urls http://127.0.0.1:5000
```

## 4. Normal edit cycle

1. Start the application with `dotnet watch`:

   ```bash
   dotnet watch --project src/Portfolio/Portfolio.csproj
   ```

2. Edit the relevant source file.
3. Refresh the browser if the changed static asset is not refreshed
   automatically.
4. Run the focused tests.
5. Before finishing, run the full verification commands from section 7.

## 5. Change portfolio content

Project data lives in:

```text
src/Portfolio/wwwroot/projects.json
```

Each `PortfolioProject` requires:

- a unique URL-safe slug;
- display name, category, tagline, and description;
- a score between `0` and `10`;
- year, repository URL, and supported accent name;
- technology and highlight lists;
- an optional featured flag.

The public portfolio currently requires a score of at least `8.0` and
`Featured = true`. If the selection policy changes, update the catalog tests and
the documentation in the same change.

After changing content, verify the API:

```bash
curl http://localhost:8080/api/projects
curl http://localhost:8080/api/projects/cupit
```

## 6. Change the interface

| File | Change it when |
| --- | --- |
| `src/Portfolio/wwwroot/index.html` | Page structure, text, metadata, or reusable card template changes |
| `src/Portfolio/wwwroot/css/site.css` | Layout, typography, colors, animation, or breakpoints change |
| `src/Portfolio/wwwroot/js/site.js` | Catalog rendering, navigation, or browser interaction changes |

When editing the interface, check at least these widths:

- `1280px` desktop
- `768px` tablet
- `390px` phone

Also verify:

- there is no horizontal scrolling;
- the mobile menu opens, closes, and follows links;
- all five project cards render after the catalog request;
- project links have useful accessible names;
- keyboard focus remains visible;
- reduced-motion mode does not hide content;
- the browser console contains no errors.

## 7. Build and test

Run the complete verification sequence from the repository root:

```bash
dotnet restore MyWebPage.slnx
dotnet build MyWebPage.slnx --no-restore
dotnet test MyWebPage.slnx --no-build
```

Optional JavaScript syntax check:

```bash
node --check src/Portfolio/wwwroot/js/site.js
```

Optional coverage collection:

```bash
dotnet test MyWebPage.slnx \
  --collect:"XPlat Code Coverage" \
  --results-directory TestResults
```

Coverage output and normal .NET build folders are ignored by Git.

## 8. Add tests

Tests belong in `tests/Portfolio.Tests`. Use descriptive behavior-based test
names and keep test data local to the test unless it is the real catalog under
test.

Run one test class while iterating:

```bash
dotnet test tests/Portfolio.Tests/Portfolio.Tests.csproj \
  --filter FullyQualifiedName~ProjectCatalogTests
```

## 9. API behavior

Expected checks while the application is running:

```bash
curl --fail http://localhost:8080/health
curl --fail http://localhost:8080/api/projects
curl --fail http://localhost:8080/api/projects/chatic
curl --include http://localhost:8080/api/projects/not-a-project
```

The first three commands should return `200`. The final command should return
`404` with a JSON message.

## 10. Troubleshooting

### Port 8080 is already used

Run the application on another port:

```bash
dotnet run --project src/Portfolio/Portfolio.csproj \
  --urls http://127.0.0.1:8081
```

### Test packages cannot be downloaded

Check internet and proxy access to NuGet, then run:

```bash
dotnet nuget list source
dotnet restore MyWebPage.slnx
```

Do not commit generated `bin`, `obj`, or `TestResults` directories.

### The page loads but no projects appear

1. Open `http://localhost:8080/projects.json` directly.
2. Confirm it returns a JSON array.
3. Check the browser console for a fetch or JavaScript error.
4. Confirm `site.js` passes the syntax check.

### Another device cannot connect

Follow [DEPLOYMENT.md](DEPLOYMENT.md#local-network-hosting). Confirm both devices
use the same trusted network and that the operating-system firewall permits the
.NET process or TCP port `8080`.
