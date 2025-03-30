document.addEventListener("DOMContentLoaded", function () {
    const dropArea = document.getElementById("drop-area");
    const fileInput = document.getElementById("file-input");
    const fileList = document.getElementById("file-list");
    const errorMessage = document.getElementById("error-message");
    const needle = document.getElementById("needle");
    const scoreText = document.getElementById("score-text");
    const retryButton = document.getElementById("retry-button");

    if (!fileList) {
        console.error("Error: file-list element is missing in HTML.");
        return;
    }

    retryButton.style.display = "none";

    function handleFiles(files) {
        fileList.innerHTML = "";
        errorMessage.textContent = "";

        for (const file of files) {
            const fileType = file.name.split(".").pop().toLowerCase();
            if (fileType !== "pdf" && fileType !== "docx") {
                errorMessage.textContent = "Only PDF and DOCX files are allowed!";
                return;
            }
            const fileItem = document.createElement("p");
            fileItem.classList.add("file-item");
            fileItem.textContent = `✅ ${file.name}`;
            fileList.appendChild(fileItem);
        }

        retryButton.style.display = "block";
        uploadAndFetchATSScore(files[0]);  // Send file to backend
    }

    function uploadAndFetchATSScore(file) {
        const formData = new FormData();
        formData.append("resume", file);
        formData.append("job_desc", "Looking for a Python Developer with expertise in ML and AI.");
        formData.append("required_skills", "Python, Machine Learning, AI, NLP, Data Science");

        startLoadingAnimation();
        startNeedleAnimation(); // Start moving the needle randomly

        fetch("http://127.0.0.1:5000/score_resume", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.final_resume_score !== undefined) {
                stopNeedleAnimation(data.final_resume_score); // Move needle to final score
            } else {
                scoreText.textContent = "Error fetching ATS score!";
                scoreText.style.color = "#ff4d4d";
            }
        })
        .catch(error => {
            console.error("Error:", error);
            scoreText.textContent = "Server Error!";
            scoreText.style.color = "#ff4d4d";
        });
    }

    function startLoadingAnimation() {
        let dots = 0;
        scoreText.textContent = "Loading";
        scoreText.style.opacity = 1;

        let loadingInterval = setInterval(() => {
            dots = (dots + 1) % 4;
            scoreText.textContent = "Loading" + ".".repeat(dots);
        }, 500);

        scoreText.setAttribute("data-loading-interval", loadingInterval);
    }

    function startNeedleAnimation() {
        let count = 0;
        let iterations = 8;

        let messageInterval = setInterval(() => {
            let messages = [
                "Analyzing resume keywords...",
                "Checking job match potential...",
                "Comparing against industry benchmarks...",
                "Optimizing ATS compatibility...",
                "Ensuring readability for recruiters...",
            ];
            let randomMessage = messages[Math.floor(Math.random() * messages.length)];
            scoreText.textContent = randomMessage;
        }, 2000);

        let interval = setInterval(() => {
            let randomAngle = Math.random() * 180 - 90;
            needle.style.transition = "transform 0.3s ease-out";
            needle.style.transform = `rotate(${randomAngle}deg)`;
            count++;
        }, 500);

        needle.setAttribute("data-interval", interval);
        needle.setAttribute("data-message-interval", messageInterval);
    }

    function stopNeedleAnimation(finalScore) {
        clearInterval(needle.getAttribute("data-interval"));
        clearInterval(needle.getAttribute("data-message-interval"));
        clearInterval(scoreText.getAttribute("data-loading-interval"));

        let finalAngle = (finalScore / 100) * 180 - 90;
        let color = finalScore < 40 ? "#ff4d4d" : finalScore < 55 ? "#ffa500" : "#28a745";

        setTimeout(() => {
            needle.style.transition = "transform 1s ease-in-out";
            needle.style.transform = `rotate(${finalAngle}deg)`;
        }, 1000);

        scoreText.textContent = `Your ATS Score: ${finalScore}%`;
        scoreText.style.color = color;

        retryButton.style.display = "block";
    }

    dropArea.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropArea.classList.add("dragover");
    });

    dropArea.addEventListener("dragleave", () => {
        dropArea.classList.remove("dragover");
    });

    dropArea.addEventListener("drop", (e) => {
        e.preventDefault();
        dropArea.classList.remove("dragover");
        handleFiles(e.dataTransfer.files);
    });

    fileInput.addEventListener("change", (e) => {
        handleFiles(e.target.files);
    });
});
