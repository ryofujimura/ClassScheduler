// Fetch data from output.json from outside the templates folder
fetch('../ClassScheduler/data/output.json')
.then(response => response.json())
.then(data => {
    // Once the JSON data is loaded, call createTimetables with the data
    createTimetables(data);
})
.catch(error => {
    console.error('Error loading data from output.json:', error);
}); 

// Define a color-coding scheme based on class ID
const classColors = {
    "341": "color-one",
    "325": "color-two",
    "491A": "color-three",
    "326": "color-four",
    "342": "color-five",
};

// Function to format time from "1400" to "14:00"
function formatTime(time) {
    if (time.length === 3) {
        // Add a leading zero for single-digit minutes
        return `${time.charAt(0)}:${time.substr(1)}`;
    } else if (time.length === 4) {
        // Add a colon between hours and minutes
        return `${time.substr(0, 2)}:${time.substr(2)}`;
    }
    return time; // Return unchanged if not in expected format
}
// ... Previous JavaScript code ...

function createTimetables(schedules) {
    const tableContainer = document.getElementById("scheduleTables");

    // Loop through each schedule
    for (let i = 0; i < schedules.length; i++) {
        const schedule = schedules[i];

        // Create an <h2> heading for the schedule number
        const h2 = document.createElement("h2");
        h2.textContent = `Schedule ${i + 1}`;
        tableContainer.appendChild(h2);

        const table = document.createElement("table");
        table.id = `schedule${i + 1}`;

        // Create a row for weekday labels
        const weekdayLabelRow = document.createElement("tr");
        const weekdayLabels = ["time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
        weekdayLabels.forEach(weekdayLabel => {
            const weekdayLabelCell = document.createElement("th");
            weekdayLabelCell.textContent = weekdayLabel;
            weekdayLabelRow.appendChild(weekdayLabelCell);
        });
        table.appendChild(weekdayLabelRow);

        for (let j = 8; j <= 21; j++) {
            const row = document.createElement("tr");
            const timeCell = document.createElement("td");
            timeCell.textContent = j < 10 ? "0" + j + ":00" : j + ":00";
            row.appendChild(timeCell);

            for (let k = 0; k < 7; k++) {
                const day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][k];
                let cellContent = "";
                let cellClass = "free"; // Default to free/busy

                // Loop through each class in the schedule
                for (const classId in schedule) {
                    const classSchedule = schedule[classId];
                    if (classSchedule.day.includes(day) && classSchedule.time[0] <= j * 100 && classSchedule.time[1] >= j * 100) {
                        const startTime = formatTime(classSchedule.time[0].toString());
                        const endTime = formatTime(classSchedule.time[1].toString());
                        cellContent = `${classId} - ${startTime}-${endTime}`;
                        cellClass = classColors[classId] || "busy";
                        break;
                    }
                }

                const cell = document.createElement("td");
                cell.className = cellClass;
                cell.textContent = cellContent;
                row.appendChild(cell);
            }

            table.appendChild(row);
        }

        tableContainer.appendChild(table);
    }
}

const addTimingButton = document.getElementById('addTiming');
const timingsContainer = document.getElementById('timings');
const form = document.querySelector('form');

addTimingButton.addEventListener('click', function () {
    createTimingInput();
});

form.addEventListener('submit', function (event) {
    event.preventDefault();
    const scheduleData = collectScheduleData();
    const formattedData = formatScheduleData(scheduleData);
    const jsonData = JSON.stringify(formattedData, null, 2);

    // Create a Blob containing the JSON data
    const blob = new Blob([jsonData], { type: 'application/json' });

    // Create a URL for the Blob
    const url = URL.createObjectURL(blob);

    // Create a link element for manual download
    const downloadLink = document.createElement('a');
    downloadLink.href = url;
    downloadLink.download = 'personal_schedule.json';

    // Trigger a click event to prompt manual download
    downloadLink.click();

    // Release the URL
    URL.revokeObjectURL(url);
});

timingsContainer.addEventListener('click', function (event) {
    if (event.target.classList.contains('deleteTiming')) {
        event.target.parentElement.remove();
    }
});

function createTimingInput() {
    const timingDiv = document.createElement('div');
    timingDiv.classList.add('timing');

    timingDiv.innerHTML = `
        <label for="timing">Timing (e.g., 800-1200):</label>
        <input type="text" name="timing" required>
        <label for="days">Days (comma-separated, e.g., Monday, Tuesday):</label>
        <input type="text" name="days" required>
        <button type="button" class="deleteTiming">Delete</button>
    `;

    timingsContainer.appendChild(timingDiv);
}

function collectScheduleData() {
    const timingInputs = document.querySelectorAll('.timing');
    const scheduleData = [];

    timingInputs.forEach(function (timingInput) {
        const timing = timingInput.querySelector('input[name="timing"]').value;
        const days = timingInput.querySelector('input[name="days"]').value.split(',').map(day => day.trim());

        scheduleData.push({ timing, days });
    });

    return scheduleData;
}

function formatScheduleData(scheduleData) {
    return scheduleData.map(entry => [
        [parseTiming(entry.timing), entry.days],
    ]);
}

function parseTiming(timingString) {
    const [start, end] = timingString.split('-').map(time => parseInt(time.trim()));
    return [start, end];
}
