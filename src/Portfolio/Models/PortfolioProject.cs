namespace Portfolio.Models;

public sealed record PortfolioProject(
    string Slug,
    string Name,
    string Eyebrow,
    string Tagline,
    string Description,
    decimal Score,
    int Year,
    string RepositoryUrl,
    string Accent,
    IReadOnlyList<string> Technologies,
    IReadOnlyList<string> Highlights,
    bool Featured = true);
