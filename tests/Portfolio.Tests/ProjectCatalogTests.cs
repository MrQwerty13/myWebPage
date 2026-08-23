using Portfolio.Services;

namespace Portfolio.Tests;

public sealed class ProjectCatalogTests
{
    private readonly ProjectCatalog _catalog = new();

    [Fact]
    public void Featured_projects_all_meet_the_quality_threshold()
    {
        var featured = _catalog.GetFeatured();

        Assert.NotEmpty(featured);
        Assert.All(featured, project => Assert.True(project.Score >= 8m));
    }

    [Fact]
    public void Catalog_uses_unique_slugs_and_valid_scores()
    {
        var projects = _catalog.GetAll();

        Assert.Equal(projects.Count, projects.Select(project => project.Slug).Distinct().Count());
        Assert.All(projects, project => Assert.InRange(project.Score, 0m, 10m));
    }

    [Fact]
    public void Catalog_contains_the_five_reviewed_projects()
    {
        var projects = _catalog.GetFeatured();

        Assert.Equal(5, projects.Count);
        Assert.Equal("CupIT", projects[0].Name);
    }

    [Theory]
    [InlineData("cupit", "CupIT")]
    [InlineData("CUPIT", "CupIT")]
    [InlineData("chatic", "Chatic")]
    public void Find_is_case_insensitive(string slug, string expectedName)
    {
        Assert.Equal(expectedName, _catalog.Find(slug)?.Name);
    }
}
