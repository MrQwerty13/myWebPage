using Portfolio.Models;

namespace Portfolio.Services;

public sealed class ProjectCatalog
{
    private static readonly IReadOnlyList<PortfolioProject> Projects =
    [
        new(
            "cupit", "CupIT", "Cafe intelligence",
            "Every receipt becomes a clearer decision.",
            "A local-first analytics platform that turns cafe sales data into useful KPIs, product rankings, trends, and AI-assisted recommendations without exposing raw business data.",
            9.5m, 2026, "https://github.com/MrQwerty13/CupIT", "lime",
            ["Python", "Flask", "Next.js", "TypeScript", "Docker", "Ollama"],
            ["10+ operational KPIs", "Private local AI", "Tested data pipeline"]),
        new(
            "fried-sausages", "FriedSausages", "Security operations",
            "Infrastructure risk, brought into focus.",
            "A full-stack security operations dashboard for assets, vulnerabilities, compliance, evidence archives, reporting, and scheduled checks, supported by a typed domain model and automated tests.",
            8.7m, 2026, "https://github.com/MrQwerty13/FriedSausages", "violet",
            ["React", "TypeScript", "Python", "PostgreSQL", "Docker"],
            ["Compliance workflows", "Integrity tooling", "Tested backend models"]),
        new(
            "chatic", "Chatic", "Realtime messaging",
            "Private conversations. Instantly familiar.",
            "A browser messenger with private chats, accounts, typing state, profiles, themes, and a resilient realtime layer that falls back from WebSockets to polling when hosting requires it.",
            8.5m, 2026, "https://github.com/MrQwerty13/chatic", "blue",
            ["Python", "Flask", "Socket.IO", "JavaScript", "HTML/CSS"],
            ["Realtime and polling", "Profile customization", "Deployment-ready"]),
        new(
            "aftertaste", "Aftertaste", "Social tasting journal",
            "Small opinions. Shared beautifully.",
            "A bilingual social journal for short takes on drinks, with a personal feed, accounts, comments, reactions, moderation, themes, and a live deployment.",
            8.2m, 2026, "https://github.com/MrQwerty13/Aftertaste", "orange",
            ["Python", "Flask", "SQLite", "Jinja", "JavaScript"],
            ["Live deployment", "English and Russian", "Custom themes"]),
        new(
            "task-tracker", "TaskTracker", "Focused productivity",
            "A simple list with a surprisingly solid core.",
            "A small task manager whose web and console interfaces share the same service layer, with atomic JSON persistence, migration support, and a compact HTTP API.",
            8.0m, 2026, "https://github.com/MrQwerty13/TaskTrackerPyVersion", "coral",
            ["Python", "Flask", "JavaScript", "JSON"],
            ["Web and console UI", "Atomic persistence", "Layered architecture"])
    ];

    public IReadOnlyList<PortfolioProject> GetAll() => Projects;

    public IReadOnlyList<PortfolioProject> GetFeatured() =>
        Projects.Where(project => project.Featured && project.Score >= 8m).ToArray();

    public PortfolioProject? Find(string slug) =>
        Projects.FirstOrDefault(project =>
            string.Equals(project.Slug, slug, StringComparison.OrdinalIgnoreCase));
}
