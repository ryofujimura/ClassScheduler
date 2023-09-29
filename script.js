// Define class_schedule_info as before

document.addEventListener('DOMContentLoaded', () => {
    generateCombinations();
});

function generateCombinations() {
    const personalScheduleInput = document.getElementById('personal-schedule-input');
    const personalSchedule = personalScheduleInput.value;

    // Send the personal schedule to the server and get combinations
    fetch('/generate_combinations', {
        method: 'POST',
        body: JSON.stringify({ personalSchedule }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => displayCombinations(data));
}

function displayCombinations(combinations) {
    const combinationsDiv = document.getElementById('combinations');
    combinationsDiv.innerHTML = '';

    combinations.forEach((combination, index) => {
        const combinationDiv = document.createElement('div');
        combinationDiv.innerHTML = `<strong>Combination ${index + 1}:</strong><br>`;

        combination.forEach(section => {
            const classInfo = `Class: ${section[1]}, Time: ${section[0][0]}-${section[0][1]}, Day: ${section[1]}`;
            combinationDiv.innerHTML += classInfo + '<br>';
        });

        combinationsDiv.appendChild(combinationDiv);
    });
}
