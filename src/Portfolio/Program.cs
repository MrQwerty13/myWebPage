using Portfolio.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSingleton<ProjectCatalog>();

var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();

app.MapGet("/api/projects", (ProjectCatalog catalog) => catalog.GetAll());

app.MapGet("/api/projects/{slug}", (string slug, ProjectCatalog catalog) =>
    catalog.Find(slug) is { } project
        ? Results.Ok(project)
        : Results.NotFound(new { message = $"Project '{slug}' was not found." }));

app.MapGet("/health", () => Results.Ok(new
{
    status = "healthy",
    service = "portfolio",
    timestamp = DateTimeOffset.UtcNow
}));

app.MapFallbackToFile("index.html");

app.Run();

public partial class Program;
