/**
 * VPD Calculation Module
 * Uses Tetens formula for saturation vapor pressure.
 */

/**
 * Saturation vapor pressure (SVP) using Tetens formula.
 * @param {number} tempC - Temperature in °C
 * @returns {number} SVP in kPa
 */
export function saturationVaporPressure(tempC) {
  return 0.6108 * Math.exp((17.27 * tempC) / (tempC + 237.3));
}

/**
 * Actual vapor pressure (AVP).
 * @param {number} svp - Saturation vapor pressure in kPa
 * @param {number} rh - Relative humidity in % (0–100)
 * @returns {number} AVP in kPa
 */
export function actualVaporPressure(svp, rh) {
  return svp * (rh / 100);
}

/**
 * Vapor Pressure Deficit.
 * @param {number} tempC - Air temperature in °C
 * @param {number} rh - Relative humidity in % (0–100)
 * @returns {number} VPD in kPa
 */
export function calculateVPD(tempC, rh) {
  const svp = saturationVaporPressure(tempC);
  const avp = actualVaporPressure(svp, rh);
  return Math.round((svp - avp) * 100) / 100;
}

/**
 * Leaf VPD — uses leaf surface temperature instead of air temp
 * for the saturation side, and air temp for the actual vapor pressure.
 * @param {number} airTempC - Air temperature in °C
 * @param {number} leafTempC - Leaf temperature in °C
 * @param {number} rh - Relative humidity in % (0–100)
 * @returns {number} Leaf VPD in kPa
 */
export function calculateLeafVPD(airTempC, leafTempC, rh) {
  const svpLeaf = saturationVaporPressure(leafTempC);
  const svpAir = saturationVaporPressure(airTempC);
  const avp = actualVaporPressure(svpAir, rh);
  return Math.round((svpLeaf - avp) * 100) / 100;
}

/**
 * VPD zone classification.
 * @param {number} vpd - VPD value in kPa
 * @returns {{ id: string, label: string, description: string }}
 */
export function getVPDZone(vpd) {
  if (vpd < 0.4) {
    return {
      id: "danger-low",
      label: "Zu niedrig",
      description: "Schimmelgefahr — Luftzirkulation erhöhen oder Luftfeuchtigkeit senken",
    };
  }
  if (vpd < 0.8) {
    return {
      id: "early-veg",
      label: "Stecklinge / Frühe Veg.",
      description: "Ideal für Stecklinge, Sämlinge und frühe Vegetationsphase",
    };
  }
  if (vpd < 1.2) {
    return {
      id: "late-veg",
      label: "Späte Veg. / Frühe Blüte",
      description: "Optimaler Bereich für späte Vegetations- und frühe Blütephase",
    };
  }
  if (vpd < 1.6) {
    return {
      id: "mid-flower",
      label: "Mittlere / Späte Blüte",
      description: "Geeignet für mittlere bis späte Blütephase",
    };
  }
  return {
    id: "danger-high",
    label: "Zu hoch",
    description: "Trockenstress — Luftfeuchtigkeit erhöhen oder Temperatur senken",
  };
}
