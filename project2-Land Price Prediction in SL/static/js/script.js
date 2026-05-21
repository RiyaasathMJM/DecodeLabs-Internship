/**
 * DecodeLabs - Project 2: Property Price Predictor
 * Frontend Logic
 */

const predictForm = document.getElementById('predictForm');
const predictBtn = document.getElementById('predictBtn');
const resultCard = document.getElementById('resultCard');
const resultPrice = document.getElementById('resultPrice');
const resultDetails = document.getElementById('resultDetails');
const errorCard = document.getElementById('errorCard');
const errorMessage = document.getElementById('errorMessage');
const propertyTypeSelect = document.getElementById('type');

// ============================================
// INITIALIZATION
// ============================================
document.addEventListener('DOMContentLoaded', function() {
    console.log('🏠 Property Price Predictor Initialized');
    loadLocations();
    setupPropertyTypeListener();
});

// ============================================
// LOAD LOCATIONS
// ============================================
async function loadLocations() {
    try {
        const response = await fetch('/api/locations');
        const data = await response.json();

        const locationSelect = document.getElementById('location');
        data.locations.forEach(location => {
            const option = document.createElement('option');
            option.value = location;
            option.textContent = location;
            locationSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Failed to load locations:', error);
        const fallbackLocations = [
            'Colombo', 'Kandy', 'Galle', 'Negombo', 'Kurunegala',
            'Matara', 'Jaffna', 'Anuradhapura', 'Ratnapura'
        ];
        const locationSelect = document.getElementById('location');
        fallbackLocations.forEach(location => {
            const option = document.createElement('option');
            option.value = location;
            option.textContent = location;
            locationSelect.appendChild(option);
        });
    }
}

// ============================================
// PROPERTY TYPE CHANGE
// ============================================
function setupPropertyTypeListener() {
    propertyTypeSelect.addEventListener('change', function() {
        updateFormForPropertyType(this.value);
    });
}

function updateFormForPropertyType(propertyType) {
    const bedBathRow = document.getElementById('bedBathRow');
    const houseSizeGroup = document.getElementById('houseSizeGroup');
    const bedroomsInput = document.getElementById('total_bedrooms');
    const bathroomsInput = document.getElementById('total_bathrooms');
    const houseSizeInput = document.getElementById('house_size_raw');
    const landSizeInput = document.getElementById('land_size_raw');
    const totalSizeInput = document.getElementById('total_size');

    if (propertyType === 'Land') {
        // Hide bedrooms/bathrooms
        bedBathRow.style.display = 'none';
        bedroomsInput.value = '0';
        bathroomsInput.value = '0';

        // Hide house size
        houseSizeGroup.style.display = 'none';
        houseSizeInput.value = '0';

        // Set land size default for land
        if (!landSizeInput.value || landSizeInput.value === '10') {
            landSizeInput.value = '20';
        }

        // Auto-calculate total_size from land size (perches → sqft)
        totalSizeInput.value = Math.round(parseFloat(landSizeInput.value || 20) * 272.25);

    } else if (propertyType === 'House' || propertyType === 'Villa' || propertyType === 'Bungalow') {
        // Show bedrooms/bathrooms
        bedBathRow.style.display = 'grid';
        if (bedroomsInput.value === '0') bedroomsInput.value = '3';
        if (bathroomsInput.value === '0') bathroomsInput.value = '2';

        // Show house size
        houseSizeGroup.style.display = 'block';
        if (houseSizeInput.value === '0') houseSizeInput.value = '1500';

        // Default land size
        if (landSizeInput.value === '20') landSizeInput.value = '10';

        // total_size = house size (the main building)
        totalSizeInput.value = houseSizeInput.value;

    } else if (propertyType === 'Apartment') {
        // Show bedrooms/bathrooms
        bedBathRow.style.display = 'grid';
        if (bedroomsInput.value === '0') bedroomsInput.value = '2';
        if (bathroomsInput.value === '0') bathroomsInput.value = '1';

        // Show house size
        houseSizeGroup.style.display = 'block';
        if (houseSizeInput.value === '0') houseSizeInput.value = '800';

        // Default land size
        if (landSizeInput.value === '20') landSizeInput.value = '5';

        // total_size = apartment size
        totalSizeInput.value = houseSizeInput.value;

    } else {
        // Commercial or other
        bedBathRow.style.display = 'grid';
        houseSizeGroup.style.display = 'block';
        totalSizeInput.value = houseSizeInput.value;
    }
}

// ============================================
// HANDLE FORM SUBMISSION
// ============================================
async function handleSubmit(event) {
    event.preventDefault();

    resultCard.style.display = 'none';
    errorCard.style.display = 'none';

    const formData = new FormData(predictForm);
    const data = {};
    formData.forEach((value, key) => {
        if (value && value !== '') {
            data[key] = value;
        }
    });

    if (!data.type) {
        showError('Please select a Property Type');
        return false;
    }
    if (!data.location) {
        showError('Please select a Location');
        return false;
    }

    predictBtn.disabled = true;
    predictBtn.innerHTML = '<span class="spinner"></span> Predicting...';

    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.success) {
            showResult(result, data);
        } else {
            showError(result.error || 'Prediction failed');
        }
    } catch (error) {
        showError('Could not connect to server');
        console.error('Error:', error);
    } finally {
        predictBtn.disabled = false;
        predictBtn.innerHTML = '<span class="btn-icon">🔮</span> Predict Price';
    }

    return false;
}

// ============================================
// SHOW RESULT
// ============================================
function showResult(result, inputData) {
    resultPrice.textContent = result.price_formatted;

    const type = inputData.type || 'Property';
    const location = inputData.location || 'Unknown';
    const bedrooms = inputData.total_bedrooms;
    const bathrooms = inputData.total_bathrooms;
    const landSize = inputData.land_size_raw;

    let detailsHTML = `<p>🏠 <strong>${type}</strong> in <strong>${location}</strong></p>`;

    if (type !== 'Land') {
        if (bedrooms && bedrooms !== '0') {
            detailsHTML += `<p>🛏️ ${bedrooms} Bedroom(s)</p>`;
        }
        if (bathrooms && bathrooms !== '0') {
            detailsHTML += `<p>🚿 ${bathrooms} Bathroom(s)</p>`;
        }
    }

    if (landSize && landSize !== '0') {
        detailsHTML += `<p>📐 ${landSize} Perches Land</p>`;
    }

    detailsHTML += `<p class="price-alt">${result.price_millions}</p>`;

    resultDetails.innerHTML = detailsHTML;
    resultCard.style.display = 'flex';
    resultCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// ============================================
// SHOW ERROR
// ============================================
function showError(message) {
    errorMessage.textContent = message;
    errorCard.style.display = 'flex';
    errorCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

window.handleSubmit = handleSubmit;