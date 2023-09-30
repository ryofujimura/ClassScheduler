// Define your schedules
const schedules = [
    {
        "341": { "day": ["Friday"], "time": [1200, 1430] },
        "325": { "day": ["Monday", "Wednesday"], "time": [1800, 1915] },
        "491A": { "day": ["Monday", "Wednesday"], "time": [1400, 1515] },
        "326": { "day": ["Tuesday", "Thursday"], "time": [1700, 1815] },
        "342": { "day": ["Tuesday", "Thursday"], "time": [1230, 1345] }
      },
      {
        "341": { "day": ["Friday"], "time": [1200, 1430] },
        "325": { "day": ["Monday", "Wednesday"], "time": [1800, 1915] },
        "491A": { "day": ["Monday", "Wednesday"], "time": [1400, 1515] },
        "326": { "day": ["Tuesday", "Thursday"], "time": [1700, 1815] },
        "342": { "day": ["Tuesday", "Thursday"], "time": [930, 1045] }
      },
];

function createTimetable(schedule, scheduleNumber) {
    const tableContainer = document.getElementById("scheduleTables");

    // Create an <h2> heading for the schedule number
    const h2 = document.createElement("h2");
    h2.textContent = `Schedule ${scheduleNumber}`;
    tableContainer.appendChild(h2);

    const table = document.createElement("table");
    table.id = `schedule${scheduleNumber}`;

    for (let i = 8; i <= 21; i++) {
        const row = document.createElement("tr");
        const timeCell = document.createElement("td");
        timeCell.textContent = i < 10 ? "0" + i + ":00" : i + ":00";
        row.appendChild(timeCell);

        for (let j = 0; j < 7; j++) {
            const day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][j];
            let cellContent = "";
            let cellClass = "free"; // Default to free/busy

            for (const classId in schedule) {
                const classSchedule = schedule[classId];
                if (classSchedule.day.includes(day) && classSchedule.time[0] <= i * 100 && classSchedule.time[1] >= i * 100) {
                    cellContent = classId;
                    cellClass = "busy"; // Mark as busy
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

// Create timetables for each schedule
for (let i = 0; i < schedules.length; i++) {
    createTimetable(schedules[i], i + 1);
}
