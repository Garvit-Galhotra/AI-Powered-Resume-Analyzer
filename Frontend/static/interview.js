    // ✅ Load Live2D Model (Standalone, No VTube Studio)
    function initializeLive2D() {
        const app = new PIXI.Application({
            view: document.getElementById("live2dCanvas"),
            width: 600,
            height: 600,
            transparent: true
        });

        PIXI.live2d.Live2DModel.from("/static/models/kei_basic_free.model3.json").then(model => {
            model.scale.set(0.75);
            model.anchor.set(0.5, 1);
            model.position.set(app.screen.width / 2, app.screen.height * 1.02);
            app.stage.addChild(model);
            window.live2DModel = model;
        }).catch(error => {
            console.log("❌ Failed to load Live2D model:", error);
        });
    }

    document.addEventListener("DOMContentLoaded", initializeLive2D);

    // ✅ Traffic Light Control
    let currentTrafficLight = null;

    function setTrafficLight(color) {
        currentTrafficLight = color;

        const states = {
            red: { selector: ".red", text: "AI is Speaking" },
            yellow: { selector: ".yellow", text: "Processing Answer" },
            green: { selector: ".green", text: "Listening" }
        };

        Object.keys(states).forEach(light => {
            document.querySelector(states[light].selector).style.opacity = (light === color) ? "1" : "0.2";
        });

        document.querySelectorAll(".light-text").forEach(text => {
            text.style.display = "none";
            text.classList.remove("highlight-text");
        });

        const activeText = document.querySelector(states[color].selector)?.nextElementSibling;
        if (activeText) {
            activeText.style.display = "block";
            activeText.classList.add("highlight-text");
        }
    }

    // ✅ Reset Traffic Light
    function resetTrafficLight() {
        currentTrafficLight = null;
        document.querySelectorAll(".light").forEach(light => light.style.opacity = "0.2");
        document.querySelectorAll(".light-text").forEach(text => text.style.display = "none");
    }

    document.addEventListener("DOMContentLoaded", function () {
        let lockJobButton = document.getElementById("lockJobButton");
        let lockNumButton = document.getElementById("lockNumButton");
        let jobSelectionContainer = document.getElementById("jobSelectionContainer");
        let numQuestionsPanel = document.getElementById("numQuestionsPanel");
        let rightPanel = document.getElementById("rightPanel");

        if (jobSelectionContainer) jobSelectionContainer.style.display = "block";
        if (numQuestionsPanel) numQuestionsPanel.style.display = "none"; // Hide until job is selected

        if (lockJobButton) {
            lockJobButton.addEventListener("click", function () {
                let jobSelection = document.getElementById("jobSelection");
                let jobErrorMessage = document.getElementById("job-error-message");

                if (!jobSelection || !jobErrorMessage || !numQuestionsPanel || !jobSelectionContainer) return;

                if (!jobSelection.value) {
                    jobErrorMessage.innerText = "Please select a job.";
                    jobErrorMessage.style.display = "block";
                    return;
                }

                jobErrorMessage.style.display = "none";
                jobSelectionContainer.style.display = "none";
                numQuestionsPanel.style.display = "block";
            });
        }

        if (lockNumButton) {
            lockNumButton.addEventListener("click", function () {
                let numQuestionsInput = document.getElementById("numQuestions");
                let numQuestions = parseInt(numQuestionsInput?.value);
                let numErrorMessage = document.getElementById("num-error-message");

                if (!numQuestionsInput || !numErrorMessage || !numQuestionsPanel) return;

                if (isNaN(numQuestions) || numQuestions < 1 || numQuestions > 10) {
                    numErrorMessage.innerText = "Please enter a number between 1 and 10.";
                    numErrorMessage.style.display = "block";
                    return;
                }

                numErrorMessage.style.display = "none";
                numQuestionsPanel.style.display = "none";

                let jobSelection = document.getElementById("jobSelection").value;
                loadQuestions(jobSelection, numQuestions);

                // ✅ Hide Right Panel After Selection
                rightPanel.style.display = "none";
            });
        }
    });

    // ✅ Fetch questions based on the selected job
    let questions = [];
    let currentQuestionIndex = 0;

    async function loadQuestions(jobRole, numQuestions) {
        try {
            let response = await fetch(`/api/get_questions?job_role=${jobRole}&num_questions=${numQuestions}`);

            if (!response.ok) {
                throw new Error(`HTTP Error! Status: ${response.status}`);
            }

            let data = await response.json();
            questions = data.questions;
            currentQuestionIndex = 0;

            if (questions.length > 0) {
                askQuestion();
            }
        } catch (error) {
            console.error("❌ Error fetching questions:", error);
        }
    }

    // ✅ AI Speaks the Question
    function askQuestion() {
        if (currentQuestionIndex >= questions.length) return;

        const question = questions[currentQuestionIndex];
        setTrafficLight("red"); // AI is speaking

        const utterance = new SpeechSynthesisUtterance(question);
        utterance.lang = "en-US";
        utterance.rate = 1.0;

        utterance.onend = function () {
            setTrafficLight("green"); // ✅ Mic Opens after AI speaks
            startListening();
        };

        utterance.onboundary = function (event) {
            const phoneme = event.charIndex; // This is a placeholder for phoneme tracking (specific to SpeechSynthesis API).
            if (window.live2DModel) {
                updateLipSync(phoneme); // Update the lip sync based on phoneme
            }
        };

        speechSynthesis.speak(utterance);
    }

    // ✅ Update Lip Sync for Live2D Model
    function updateLipSync(phoneme) {
        if (!window.live2DModel || !window.live2DModel.setParam) return;

        const lipSyncParams = ["mouthOpen", "mouthClose"];
        if (phoneme === 'A') {
            window.live2DModel.setParam("MouthOpen", 1.0);
        } else {
            window.live2DModel.setParam("MouthOpen", 0.0);
        }
    }

    // ✅ Speech Recognition (User Response)
    function startListening() {
        let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = "en-US";
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        recognition.onstart = function () {
            setTrafficLight("green"); // AI is listening
        };

        recognition.onresult = function (event) {
            let userResponse = event.results[0][0].transcript;
            console.log("🎤 User Answer:", userResponse);

            setTrafficLight("yellow"); // Processing Answer

            // ✅ Evaluate Answer (Confidence, Relevancy, Clarity)
            evaluateAnswer(userResponse);
        };

        recognition.onerror = function (event) {
            console.error("❌ Speech recognition error:", event.error);
        };

        recognition.start();
    }

    // ✅ Evaluate Answer
    async function evaluateAnswer(userResponse) {
        try {
            const response = await fetch("/api/evaluate_answer", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ question: questions[currentQuestionIndex], answer: userResponse })
            });

            if (!response.ok) throw new Error(`HTTP Error! Status: ${response.status}`);

            const result = await response.json();
            console.log("📌 Evaluation Results:", result);

            // ✅ Display Results in a Pop-up
            displayInterviewResultInPopup(result);

            // ✅ Move to Next Question after 5 seconds
            setTimeout(() => {
                if (currentQuestionIndex < questions.length - 1) {
                    currentQuestionIndex++;
                    askQuestion();
                }
                
            }, 5000);

        } catch (error) {
            console.error("❌ Error evaluating answer:", error);
        }
    }

    // ✅ Display Interview Results in a Pop-up Window with Meters
    function displayInterviewResultInPopup(result) {
        let resultWindow = window.open("", "_blank", "width=500,height=600");

        resultWindow.document.write(`
            <html>
                <head>
                    <title>Interview Results</title>
                    <style>
                        body { font-family: Arial, sans-serif; padding: 20px; text-align: center; }
                        h1 { color: #4CAF50; }
                        .meter-container { position: relative; width: 200px; height: 100px; margin: 20px auto; }
                        .meter-bg { width: 100%; height: 100px; border-radius: 100px 100px 0 0; background: linear-gradient(to right, red, yellow, green); position: absolute; top: 0; left: 0; }
                        .meter-needle { width: 10px; height: 50px; background: black; position: absolute; bottom: 0; left: 50%; transform-origin: bottom center; transition: transform 0.3s ease-out; }
                        .message { font-size: 16px; font-weight: bold; margin-top: 10px; color: #333; }
                        .loading { color: #ff9800; font-size: 18px; font-weight: bold; }
                    </style>
                </head>
                <body>
                    <h1>Analyzing Your Interview...</h1>
                    <p class="message" id="loading-message">Processing responses...</p>

                    <div class="meter-container">
                        <div class="meter-bg"></div>
                        <div class="meter-needle" id="confidence-needle"></div>
                    </div>
                    <p><strong>Confidence:</strong> <span id="confidence-value" class="loading">Calculating...</span></p>

                    <div class="meter-container">
                        <div class="meter-bg"></div>
                        <div class="meter-needle" id="clarity-needle"></div>
                    </div>
                    <p><strong>Clarity:</strong> <span id="clarity-value" class="loading">Checking...</span></p>

                    <div class="meter-container">
                        <div class="meter-bg"></div>
                        <div class="meter-needle" id="relevance-needle"></div>
                    </div>
                    <p><strong>Relevance:</strong> <span id="relevance-value" class="loading">Evaluating...</span></p>

                    <div class="feedback">
                        <p><strong>Feedback:</strong> <span id="feedback-text" class="loading">Finalizing report...</span></p>
                    </div>

                    <script>
                        function startNeedleAnimation(needleId) {
                            let interval = setInterval(() => {
                                let randomAngle = Math.random() * 180 - 90;
                                document.getElementById(needleId).style.transform = "rotate(" + randomAngle + "deg)";
                            }, 500);
                            document.getElementById(needleId).setAttribute("data-interval", interval);
                        }

                        function stopNeedleAnimation(needleId, value) {
                            clearInterval(document.getElementById(needleId).getAttribute("data-interval"));
                            let finalAngle = (value / 100) * 180 - 90;
                            setTimeout(() => {
                                document.getElementById(needleId).style.transition = "transform 1s ease-in-out";
                                document.getElementById(needleId).style.transform = "rotate(" + finalAngle + "deg)";
                            }, 1000);
                        }

                        function startLoadingAnimation() {
                            let messages = [
                                "Evaluating answer structure...",
                                "Checking speech clarity...",
                                "Assessing confidence level...",
                                "Comparing with top performers...",
                                "Finalizing results...",
                            ];
                            let index = 0;
                            let interval = setInterval(() => {
                                document.getElementById("loading-message").textContent = messages[index];
                                index = (index + 1) % messages.length;
                            }, 2000);
                            document.getElementById("loading-message").setAttribute("data-interval", interval);
                        }

                        function stopLoadingAnimation() {
                            clearInterval(document.getElementById("loading-message").getAttribute("data-interval"));
                            document.getElementById("loading-message").textContent = "Interview Analysis Complete!";
                        }

                        startLoadingAnimation();
                        startNeedleAnimation("confidence-needle");
                        startNeedleAnimation("clarity-needle");
                        startNeedleAnimation("relevance-needle");

                        setTimeout(() => {
                            stopLoadingAnimation();
                            stopNeedleAnimation("confidence-needle", ${result.confidence});
                            stopNeedleAnimation("clarity-needle", ${result.clarity});
                            stopNeedleAnimation("relevance-needle", ${result.relevancy});

                            document.getElementById("confidence-value").textContent = "${result.confidence}%";
                            document.getElementById("clarity-value").textContent = "${result.clarity}%";
                            document.getElementById("relevance-value").textContent = "${result.relevancy}%";
                        }, 8000); // Delay final result by 8 seconds to build suspense
                    </script>
                </body>
            </html>
        `);

        resultWindow.document.close();
    }
