// ===============================
// CREATE OVERLAY
// ===============================
const overlay = document.createElement("div");

overlay.style.position = "fixed";
overlay.style.bottom = "12%";
overlay.style.left = "50%";
overlay.style.transform = "translateX(-50%)";
overlay.style.background = "rgba(0, 0, 0, 0.65)";
overlay.style.color = "white";
overlay.style.padding = "8px 14px";
overlay.style.borderRadius = "6px";
overlay.style.fontSize = "14px";
overlay.style.fontFamily = "Arial, sans-serif";
overlay.style.zIndex = "999999";
overlay.style.display = "none";
overlay.style.pointerEvents = "none";
overlay.style.maxWidth = "80%";
overlay.style.textAlign = "center";

document.body.appendChild(overlay);

// ===============================
// SHOW / HIDE OVERLAY
// ===============================
function showOverlay(text) {
    overlay.innerText = text;
    overlay.style.display = "block";

    setTimeout(() => {
        overlay.style.display = "none";
    }, 6000);
}

// ===============================
// FETCH AI SUMMARY
// ===============================
async function fetchSummary() {
    try {
        const response = await fetch("https://localhost:5000/summary")
        const data = await response.json();

        const text = `Over ${data.over}: ${data.summary}`;
        showOverlay(text);

    } catch (error) {
        console.error("OverBrief error:", error);
    }
}

// ===============================
// TRIGGER (SIMULATED AD BREAK)
// ===============================
// For demo: show summary every 30 seconds
setInterval(() => {
    fetchSummary();
}, 30000);
