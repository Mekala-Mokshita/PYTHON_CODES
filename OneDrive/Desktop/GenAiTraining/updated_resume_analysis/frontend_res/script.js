document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("resumeForm");
    const loading = document.getElementById("loading");
    const resultDiv = document.getElementById("result");
    const analyzeBtn = form.querySelector("button");
    const downloadBtn = document.getElementById("downloadBtn");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const fileInput = document.getElementById("fileInput");

        if (!fileInput.files.length) {
            alert("Please select a resume file");
            return;
        }

        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        // UI state
        analyzeBtn.disabled = true;
        analyzeBtn.innerText = "Analyzing...";
        loading.classList.remove("hidden");
        loading.innerText = "⏳ Analyzing your resume...";
        resultDiv.classList.add("hidden");

        try {
            const response = await fetch("http://127.0.0.1:8000/result", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                throw new Error("Server error");
            }

            const data = await response.json();

            // --- SCORE ---
            let score = Number(data.score);
            if (isNaN(score)) score = 0;
            score = Math.max(0, Math.min(100, score));

            document.getElementById("score").innerText = score;

            const progressBar = document.getElementById("progressBar");
            progressBar.style.width = score + "%";

            // Color logic
            if (score >= 75) {
                progressBar.style.background = "#2ecc71"; // green
            } else if (score >= 50) {
                progressBar.style.background = "#f39c12"; // orange
            } else {
                progressBar.style.background = "#e74c3c"; // red
            }

            // --- LISTS ---
            fillList("strengths", data.strengths);
            fillList("weaknesses", data.weaknesses);
            fillList("roles", data.job_roles);
            fillList("improvements", data.improvements);

            loading.classList.add("hidden");
            resultDiv.classList.remove("hidden");

        } catch (error) {
            loading.innerText = "❌ Failed to analyze resume. Try again.";
            console.error(error);
        } finally {
            analyzeBtn.disabled = false;
            analyzeBtn.innerText = "Analyze Resume";
        }
    });

    function fillList(id, items) {
        const ul = document.getElementById(id);
        ul.innerHTML = "";

        if (!Array.isArray(items) || items.length === 0) {
            const li = document.createElement("li");
            li.textContent = "No data available";
            ul.appendChild(li);
            return;
        }

        items.forEach(item => {
            const li = document.createElement("li");
            li.textContent = item;
            ul.appendChild(li);
        });
    }

    // --- PDF DOWNLOAD ---
    if (downloadBtn) {
        downloadBtn.addEventListener("click", () => {
            const element = document.getElementById("result");

            const options = {
                margin: 0.5,
                filename: "ATS_Resume_Report.pdf",
                image: { type: "jpeg", quality: 0.98 },
                html2canvas: { scale: 2 },
                jsPDF: { unit: "in", format: "a4", orientation: "portrait" }
            };

            html2pdf().set(options).from(element).save();
        });
    }
});
