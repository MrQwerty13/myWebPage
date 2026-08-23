using Portfolio.Models;
using System.Text.Json;

namespace Portfolio.Services;

public sealed class ProjectCatalog
{
    private static readonly IReadOnlyList<PortfolioProject> Projects = LoadProjects();

    public IReadOnlyList<PortfolioProject> GetAll() => Projects;

    public IReadOnlyList<PortfolioProject> GetFeatured() =>
        Projects.Where(project => project.Featured && project.Score >= 8m).ToArray();

    public PortfolioProject? Find(string slug) =>
        Projects.FirstOrDefault(project =>
            string.Equals(project.Slug, slug, StringComparison.OrdinalIgnoreCase));

    private static IReadOnlyList<PortfolioProject> LoadProjects()
    {
        const string resourceName = "Portfolio.wwwroot.projects.json";
        using var stream = typeof(ProjectCatalog).Assembly.GetManifestResourceStream(resourceName)
            ?? throw new InvalidOperationException($"Embedded project catalog '{resourceName}' was not found.");

        return JsonSerializer.Deserialize<PortfolioProject[]>(stream, new JsonSerializerOptions(JsonSerializerDefaults.Web))
            ?? throw new InvalidOperationException("The embedded project catalog is empty or invalid.");
    }
}
