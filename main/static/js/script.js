// script.js
document.addEventListener("DOMContentLoaded", function () {
  const categoryButtons = document.getElementById("category-buttons");
  const videoContainer = document.getElementById("video-container");
  const videoCardTemplate = document.getElementById("video-card-template");

  const categories = ["Action", "Comedy", "Drama", "Documentary"];
  const videoData = {
    Action: [
      {
        title: "Epic Car Chase",
        src: "https://www.youtube.com/embed/6XMuUVw7TOM",
      },
      {
        title: "Superhero Battle",
        src: "https://www.youtube.com/embed/FkTybqcX-Yo",
      },
      {
        title: "Convict",
        src: "https://www.youtube.com/embed/ySL7P-lYPvc?si=AHA2nwrOpKHl9zvG",
      },
      {
        title: "Martial Arts Showdown",
        src: "https://www.youtube.com/embed/M7XM597XO94",
      },
    ],
    Comedy: [
      {
        title: "Hilarious Misunderstanding",
        src: "https://www.youtube.com/embed/kn271kr_ks0",
      },
      {
        title: "Office Pranks Gone Wild",
        src: "https://www.youtube.com/embed/1aHtJZXqgU4",
      },
      {
        title: "Awkward First Date",
        src: "https://www.youtube.com/embed/rxUm-2x-2dM?si=jmhrWgy5nNmkO3Dx",
      },
      {
        title: "Comedy",
        src: "https://www.youtube.com/embed/-hX89noO_2U?si=rAzkNWqXfrhzZf9N",
      },
    ],
    Drama: [
      {
        title: "Fat boy",
        src: "https://www.youtube.com/embed/vAGYjHkUZbE?si=bvRro-TD8GLr628s",
      },
      {
        title: "Courtroom Confrontation",
        src: "https://www.youtube.com/embed/ej3ioOneTy8",
      },
      {
        title: "Grow Up",
        src: "https://www.youtube.com/embed/dPuA0PsS67Q?si=FxwSudykyx4Ir6mF",
      },
      {
        title: "Curser",
        src: "https://www.youtube.com/embed/FIO4PlueHU4?si=Ps9nyiob7gx-SYYF",
      },
    ],
    Documentary: [
      {
        title: "Wonders of the Ocean",
        src: "https://www.youtube.com/embed/6zrn4-FfbXw",
      },
      {
        title: "Behind Bars",
        src: "https://www.youtube.com/embed/BCmcx9QQNZ4?si=j_elcrNUIh29IGCB",
      },
      {
        title: "Seven greatest hiddles",
        src: "https://www.youtube.com/embed/ncOr6JSTMlw?si=BmZg8Ypf9-PglAMM",
      },
      {
        title: "Fish Bombers",
        src: "https://www.youtube.com/embed/jQ5h7lHukxk?si=0T5pM8jQOmVdOkbg",
      },
    ],
  };

  categories.forEach((category) => {
    const button = document.createElement("button");
    button.textContent = category;
    button.classList.add("btn");
    button.addEventListener("click", () => {
      categoryButtons
        .querySelectorAll(".btn")
        .forEach((btn) => btn.classList.remove("active"));
      button.classList.add("active");
      loadVideos(category);
    });
    categoryButtons.appendChild(button);
  });

  function loadVideos(category) {
    videoContainer.innerHTML = "";
    const videos = videoData[category];

    if (!videos) {
      videoContainer.innerHTML = "<p>No videos found for this category.</p>";
      return;
    }

    videos.forEach((video) => {
      const videoCard = videoCardTemplate.content.cloneNode(true);

      const iframeElement = videoCard.querySelector("iframe");
      iframeElement.src = video.src;

      const titleElement = videoCard.querySelector("h3");
      titleElement.textContent = video.title;

      const commentForm = videoCard.querySelector(".comment-form");
      const commentsSection = videoCard.querySelector(".comments-section");

      commentForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const commentText = this.querySelector(".comment-box").value.trim();
        if (commentText) {
          const newCommentElement = document.createElement("div");
          newCommentElement.classList.add("comment");
          newCommentElement.innerHTML = `
            <div class="user-icon">
              <i class="fas fa-user-circle"></i>
            </div>
            <div class="comment-content">
              <strong>CurrentUser</strong>
              <p>${commentText}</p>
            </div>
          `;
          commentsSection.appendChild(newCommentElement);
          this.reset();
        } else {
          alert("Please enter a comment before submitting.");
        }
      });

      videoContainer.appendChild(videoCard);
    });
  }

  // Load default videos (Action category)
  categoryButtons.querySelector(".btn").classList.add("active");
  loadVideos("Action");
});
