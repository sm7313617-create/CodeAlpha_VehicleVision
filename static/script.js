document.getElementById("predictionForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const fuelType = document.querySelector('input[name="fuel"]:checked')?.value || "Petrol";

  const data = {
    present_price: parseFloat(document.getElementById("present_price").value),
    kms_driven: parseInt(document.getElementById("kms_driven").value),
    year: parseInt(document.getElementById("year").value),
    owner: parseInt(document.getElementById("owner").value),
    fuel_type: fuelType,
    seller_type: document.getElementById("seller_type").value,
    transmission: document.getElementById("transmission").value
  };

  console.log("Sending data:", data);

  const priceValue = document.getElementById("priceValue");
  if (priceValue) priceValue.innerText = "Calculating...";

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();

    if (result.predicted_price !== null && result.predicted_price !== undefined) {
      if (priceValue) priceValue.innerText = result.predicted_price;
      console.log("Prediction received:", result.predicted_price);
    } else {
      if (priceValue) priceValue.innerText = "Error";
      console.error("No prediction in response:", result);
    }
  } catch (error) {
    console.error("Fetch error:", error);
    if (priceValue) priceValue.innerText = "Error";
  }
});
