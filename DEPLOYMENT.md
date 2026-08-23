# Deployment instructions

This guide covers public static hosting on GitHub Pages, trusted local-network
hosting, and a framework-dependent ASP.NET Release deployment.

## Deployment modes

| Mode | Intended use | Address |
| --- | --- | --- |
| GitHub Pages | Public portfolio | `https://mrqwerty13.github.io/myWebPage/` |
| Local only | Development on one computer | `http://127.0.0.1:8080` |
| Local network | Review from phones or other trusted devices | `http://<computer-ip>:8080` |
| Release process | Stable process behind a reverse proxy or private network | Host-specific |

## GitHub Pages hosting

The repository includes `.github/workflows/pages.yml`. It uploads
`src/Portfolio/wwwroot` and deploys it whenever `main` changes.

Enable it once on GitHub:

1. Open the repository's **Settings → Pages**.
2. Under **Build and deployment**, select **GitHub Actions** as the source.
3. Push this change to `main`, or run the workflow manually from **Actions**.
4. Open `https://mrqwerty13.github.io/myWebPage/` after deployment succeeds.

The Pages version is entirely static. Project cards load from `projects.json`,
so the portfolio works without a .NET process. The `/api/projects` and `/health`
routes are not available on Pages; they remain part of ASP.NET hosting.

## Local network hosting

The repository is configured to listen on all network interfaces at port `8080`:

```json
"Urls": "http://0.0.0.0:8080"
```

### 1. Find the computer's Wi-Fi address

On macOS, try:

```bash
ipconfig getifaddr en0
```

If Wi-Fi uses another interface, list the hardware ports first:

```bash
networksetup -listallhardwareports
```

On Linux:

```bash
hostname -I
```

Choose the private address associated with the trusted network, commonly in the
`192.168.x.x`, `10.x.x.x`, or `172.16.x.x`–`172.31.x.x` ranges.

### 2. Start the application

```bash
dotnet run --project src/Portfolio/Portfolio.csproj
```

The startup output should include:

```text
Now listening on: http://0.0.0.0:8080
```

### 3. Open it from another device

Connect the other device to the same Wi-Fi network and open:

```text
http://<computer-ip>:8080
```

Example only:

```text
http://192.168.1.25:8080
```

The address may change when reconnecting to Wi-Fi. Find it again rather than
hard-coding it in source control.

### 4. Troubleshoot LAN access

- Confirm the application still runs and responds at `http://localhost:8080`.
- Confirm the devices are on the same network and client isolation is disabled.
- Permit incoming connections for `dotnet` when the operating system asks.
- Check that a firewall is not blocking TCP port `8080`.
- Avoid guest, corporate, or public networks that prohibit device-to-device
  connections.

Listening on `0.0.0.0` exposes the application to devices that can reach the
computer. Use it only on a trusted network and stop the process when review is
finished.

## Create a Release build

From the repository root:

```bash
dotnet restore MyWebPage.slnx
dotnet test MyWebPage.slnx --configuration Release --no-restore
dotnet publish src/Portfolio/Portfolio.csproj \
  --configuration Release \
  --no-restore \
  --output /tmp/mikhail-portfolio
```

Run the published application:

```bash
dotnet /tmp/mikhail-portfolio/Portfolio.dll \
  --urls http://0.0.0.0:8080
```

Verify it from another terminal:

```bash
curl --fail http://localhost:8080/health
curl --fail http://localhost:8080/api/projects
```

## Environment configuration

ASP.NET Core supports environment variables and command-line overrides. Useful
examples:

```bash
ASPNETCORE_ENVIRONMENT=Production \
ASPNETCORE_URLS=http://127.0.0.1:8080 \
dotnet /tmp/mikhail-portfolio/Portfolio.dll
```

Bind to `127.0.0.1` when a reverse proxy on the same computer is the only client.
Bind to `0.0.0.0` only when direct network access is intended.

## Public ASP.NET hosting requirements

These requirements apply only when exposing the ASP.NET application and API to
the public internet instead of using the static Pages deployment:

1. Place Kestrel behind a maintained reverse proxy or managed .NET host.
2. Enable HTTPS with a trusted certificate and redirect HTTP to HTTPS.
3. Bind Kestrel to loopback when the reverse proxy runs on the same host.
4. Configure an explicit hostname instead of relying on `AllowedHosts: "*"`.
5. Add the security headers and production integration tests from the roadmap.
6. Configure service supervision so the process restarts after a failure or
   machine reboot.
7. Monitor `/health` from the hosting environment.
8. Keep the .NET runtime and operating system patched.

The repository does not yet include a reverse-proxy configuration, container
image, cloud manifest, or persistent service definition. Those should be created
for the selected host instead of publishing generic settings that are unsafe or
misleading.

## Apple Silicon isolation with Tart

The original project plan includes isolated verification with
[Tart](https://github.com/cirruslabs/tart), which requires an Apple Silicon Mac.
Treat this as a later build-verification layer, not as the primary hosting
environment.

Before adding Tart automation:

- select and document the exact base image;
- pin the .NET SDK version used inside the VM;
- copy or clone the repository into the VM;
- run restore, Release build, and tests inside the VM;
- publish the output as a normal build artifact;
- keep credentials and signing material outside the image.

Exact Tart commands should be added only after the base image and CI environment
are selected, because image names and host requirements are deployment-specific.

## Deployment checklist

- [ ] GitHub Pages uses **GitHub Actions** as its publishing source.
- [ ] The Pages workflow succeeds for the intended commit.
- [ ] The Pages URL loads CSS, JavaScript, and all five project cards.
- [ ] Repository is clean and the intended commit is checked out.
- [ ] Release restore, build, and tests pass.
- [ ] Static assets and all five project cards render.
- [ ] `/health` and `/api/projects` return `200`.
- [ ] The configured binding matches the intended exposure.
- [ ] Firewall rules permit only the required access.
- [ ] HTTPS and host filtering are configured for public hosting.
- [ ] The deployment process can restart the application.
- [ ] The deployed commit or release version is recorded.
