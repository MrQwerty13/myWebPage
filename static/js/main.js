(() => {
  const likeText = document.body.dataset.i18nLike || "Like";
  const likedText = document.body.dataset.i18nLiked || "Liked";
  const likeError = document.body.dataset.i18nLikeError || "Could not update like. Try again.";

  document.querySelectorAll(".like-btn[data-post-id]").forEach((button) => {
    button.addEventListener("click", async () => {
      if (button.disabled) return;

      const postId = button.dataset.postId;
      button.disabled = true;

      try {
        const response = await fetch(`/posts/${postId}/like`, {
          method: "POST",
          headers: { Accept: "application/json" },
        });

        if (response.status === 401 || response.redirected) {
          window.location.href = "/login";
          return;
        }

        if (!response.ok) {
          throw new Error("Could not update like.");
        }

        const data = await response.json();
        const label = button.querySelector(".like-label");
        const count = button.querySelector("[data-count]");

        button.dataset.liked = data.liked ? "true" : "false";
        button.classList.toggle("is-liked", data.liked);
        if (label) label.textContent = data.liked ? likedText : likeText;
        if (count) count.textContent = String(data.like_count);

        button.classList.remove("pop");
        void button.offsetWidth;
        button.classList.add("pop");
      } catch (error) {
        console.error(error);
        alert(likeError);
      } finally {
        button.disabled = false;
      }
    });
  });

  // Close Look panel when clicking outside.
  const look = document.querySelector("details.look");
  if (look) {
    document.addEventListener("click", (event) => {
      if (!look.open) return;
      if (!look.contains(event.target)) look.open = false;
    });
  }
})();
