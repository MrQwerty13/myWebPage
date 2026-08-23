# To-do file for Codex
# — Step 1 —
    1. Learn my github page: https://github.com/MrQwerty13/
    2. Create description of all my projects
    3. Make a conclusion about every project (rate it from 0-10)

# — Step 2 —
    1. According to rating, choose all projects with 8+ rating
    2. Create HTML+JS files for chosen projects and a unified CSS
    3. Style it like Apple's official website

# — Step 3 —
    1. Create a new ASP.NET Core project via `dotnet new webapi` (or `webapp` for Razor Pages)
    2. Set up the simplest project structure (Controllers/Pages, wwwroot for static HTML/CSS/JS)

# — Step 4 —
    1. Build the web page as your portfolio based on Step 2, served via ASP.NET Core static files / views
    2. Get your IP address on the Wi-Fi network and configure Kestrel to listen on that host with port 8080
       (e.g. `dotnet run --urls http://<your-ip>:8080` or set it in `launchSettings.json` / `Program.cs`)

# — Step 5 —
    1. Wrap the project into a Tart VM (github.com/openai/tart) for isolated builds/testing on Apple Silicon
       — `brew install openai/tools/tart`, clone a base Linux/macOS image, and run the dotnet build/serve
         commands inside the VM
    2. Note: Tart is Apple Silicon host-only — this step applies when building from your Mac, not your
       Linux machine

# — Step 6 —
    1. Once the page is working, write tests for every part of the project (xUnit/NUnit) to reduce error probability during development
    2. Once dev is finalized, create ROADMAP.md, TECH_STACK.md and README.md
