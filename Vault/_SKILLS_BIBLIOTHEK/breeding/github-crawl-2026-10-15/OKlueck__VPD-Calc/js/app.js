import { calculateVPD, calculateLeafVPD, getVPDZone } from "./vpd.js";

const tempInput = document.getElementById("temperature");
const humidityInput = document.getElementById("humidity");
const humiditySlider = document.getElementById("humidity-slider");
const leafOffsetInput = document.getElementById("leaf-offset");
const vpdValueEl = document.getElementById("vpd-value");
const leafVpdValueEl = document.getElementById("leaf-vpd-value");
const leafVpdContainer = document.getElementById("leaf-vpd-container");
const zoneIndicator = document.getElementById("zone-indicator");
const zoneLabelEl = document.getElementById("zone-label");
const zoneDescriptionEl = document.getElementById("zone-description");
const zonePointer = document.getElementById("zone-pointer");
const leafDetails = document.querySelector("details");

function update() {
  const temp = parseFloat(tempInput.value);
  const rh = parseFloat(humidityInput.value);
  const leafOffset = parseFloat(leafOffsetInput.value) || 0;

  if (isNaN(temp) || isNaN(rh)) {
    vpdValueEl.textContent = "—";
    vpdValueEl.removeAttribute("data-zone");
    zoneIndicator.removeAttribute("data-zone");
    zoneLabelEl.textContent = "";
    zoneDescriptionEl.textContent = "";
    return;
  }

  const vpd = calculateVPD(temp, rh);
  const zone = getVPDZone(vpd);

  vpdValueEl.textContent = vpd.toFixed(2);
  vpdValueEl.setAttribute("data-zone", zone.id);
  zoneIndicator.setAttribute("data-zone", zone.id);
  zoneLabelEl.textContent = zone.label;
  zoneDescriptionEl.textContent = zone.description;

  // Leaf VPD
  if (leafDetails.open) {
    const leafTemp = temp + leafOffset;
    const leafVpd = calculateLeafVPD(temp, leafTemp, rh);
    leafVpdValueEl.textContent = leafVpd.toFixed(2);
    const leafZone = getVPDZone(leafVpd);
    leafVpdValueEl.setAttribute("data-zone", leafZone.id);
    leafVpdContainer.hidden = false;
  } else {
    leafVpdContainer.hidden = true;
  }

  // Position the zone pointer (0–2.0+ kPa mapped to bar width)
  const clamped = Math.max(0, Math.min(vpd, 2.0));
  const percent = (clamped / 2.0) * 100;
  zonePointer.style.marginLeft = `calc(${percent}% - 4px)`;
}

// Sync slider ↔ number input
humiditySlider.addEventListener("input", () => {
  humidityInput.value = humiditySlider.value;
  update();
});

humidityInput.addEventListener("input", () => {
  humiditySlider.value = humidityInput.value;
  update();
});

tempInput.addEventListener("input", update);
leafOffsetInput.addEventListener("input", update);
leafDetails.addEventListener("toggle", update);

// Initial calculation
update();

// Register service worker
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("sw.js").catch(() => {});
}
